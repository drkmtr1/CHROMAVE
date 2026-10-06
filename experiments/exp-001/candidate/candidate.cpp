// Disposable EXP-001 candidate. Float circular history; no production plugin code.
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
namespace fs = std::filesystem;
constexpr double pi=3.141592653589793238462643383279502884;
int rounded(double x){return static_cast<int>(std::floor(x+.5));}
int intervals(double seconds,int rate){return std::max(1,rounded(seconds*rate));}
int styleCode(const std::string& s){if(s=="A")return 0;if(s=="B")return 1;if(s=="C")return 2;throw std::runtime_error("style");}
const char* styleName(int s){return s==0?"A":s==1?"B":"C";}
const char* modeName(int m){return m?"pingpong":"stereo";}
std::vector<std::string> split(const std::string& line){std::vector<std::string> r;std::stringstream in(line);std::string v;while(std::getline(in,v,','))r.push_back(v);return r;}
struct Config{
 std::string id,panel,source,schedule,partition,mutation;int style,mode,rate;double g,c;bool pre;
 explicit Config(const std::vector<std::string>& v){if(v.size()!=12)throw std::runtime_error("CSV fields");id=v[0];panel=v[1];style=styleCode(v[2]);mode=v[3]=="pingpong"?1:0;source=v[4];schedule=v[5];rate=std::stoi(v[6]);partition=v[7];g=std::stod(v[8]);c=std::stod(v[9]);pre=v[10]=="pre";mutation=v[11];if(id.empty()||id.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")!=std::string::npos)throw std::runtime_error("unsafe id");if(rate!=44100&&rate!=48000&&rate!=96000)throw std::runtime_error("rate");}
};
// kind: free duration, sync flag, BPM, beat division, style, routing.
struct Event{int n,kind;double value;};
std::vector<Event> makeEvents(const Config& c){
 std::vector<Event> e;auto add=[&](double t,int k,double v){e.push_back({rounded(t*c.rate),k,v});};const auto& s=c.schedule;
 if(s=="retarget"){add(1,0,.375);add(1.005,0,.125);add(1.009,0,.300);}
 else if(s=="timing_return"||s=="timing_repeat"){add(1,0,.375);add(1.002,0,s=="timing_return"?.250:.375);}
 else if(s=="routing"||s=="routing_return"||s=="routing_repeat"){add(1,5,1);if(s=="routing"){add(1.005,5,0);add(1.009,5,1);}else add(1.002,5,s=="routing_return"?0:1);}
 else if(s=="mode_collision"){add(1,1,1);add(1,3,1);add(1,2,120);add(1.005,2,90);add(1.009,2,std::numeric_limits<double>::quiet_NaN());add(1.009,3,.5);add(1.009,3,1);add(1.020,0,.250);add(1.020,1,0);add(1.020,4,c.style==2?0:2);}
 else if(s=="endpoint"){add(1,0,.375);add(1,5,1);e.push_back({c.rate+intervals(c.style==1?.005:.020,c.rate),0,.300});e.push_back({c.rate+intervals(.020,c.rate),5,0});}
 else if(s=="motion"){add(1,6,0);add(1.5,6,0);}else if(s!="static")throw std::runtime_error("schedule");
 std::stable_sort(e.begin(),e.end(),[](const Event&a,const Event&b){return a.n<b.n;});return e;
}
struct Desired{double free=.250,beat=1,bpm=120,lastSync=.500,delay=.250;bool sync=false,tempo=true;int style,route;};
void snapshot(Desired& d){d.tempo=std::isfinite(d.bpm)&&d.bpm>0;if(d.tempo)d.lastSync=std::clamp(60*d.beat/d.bpm,.010,2.0);d.delay=d.sync?d.lastSync:d.free;}
struct Time{
 double committed=.250,from=.250,to=.250;int committedStyle,destinationStyle,start=0,length=1;bool active=false;
 explicit Time(int s):committedStyle(s),destinationStyle(s){}
 double weight(int n)const{return active?std::clamp(double(n-start)/length,0.0,1.0):0;}
 double position(int n)const{return active&&destinationStyle==2?(1-weight(n))*from+weight(n)*to:committed;}
 bool retire(int n){if(active&&n>=start+length){committed=to;committedStyle=destinationStyle;active=false;return true;}return false;}
 void launch(int n,double old,double target,int sty,int rate){from=old;to=target;destinationStyle=sty;start=n;length=intervals(sty==1?.005:.020,rate);active=true;}
 bool update(int n,const Desired& d,int rate){
  if(active&&destinationStyle!=2)return false;
  if(active){if(d.delay==to&&d.style==destinationStyle)return false;double now=position(n);launch(n,now,d.delay,d.style,rate);return true;}
  if(d.delay==committed&&d.style==committedStyle)return false;launch(n,committed,d.delay,d.style,rate);return true;
 }
 bool pending(const Desired& d)const{return active&&destinationStyle!=2&&(d.delay!=to||d.style!=destinationStyle);}
};
struct Routing{
 int committed,to,start=0,length=1;double from=0;bool active=false;
 explicit Routing(int mode):committed(mode),to(mode),from(mode){}
 bool retire(int n){if(active&&n>=start+length){committed=to;active=false;return true;}return false;}
 bool update(int n,int wanted,int rate){if(active||wanted==committed)return false;from=committed;to=wanted;start=n;length=intervals(.020,rate);active=true;return true;}
 double weight(int n)const{return active?(1-double(n-start)/length)*from+double(n-start)/length*to:double(committed);}
};
struct Circular{
 std::vector<std::array<float,2>> samples;
 explicit Circular(int rate):samples(static_cast<size_t>(2*rate+4),{0,0}){}
 double sample(int64_t absolute,int64_t n,int channel)const{if(absolute<0)return 0;if(absolute>=n||n-absolute>=static_cast<int64_t>(samples.size()))throw std::runtime_error("causality/capacity");return samples[static_cast<size_t>(absolute%static_cast<int64_t>(samples.size()))][channel];}
 float read(int n,double seconds,int rate,int channel,bool wrongDelay)const{double q=n-seconds*rate-(wrongDelay?1:0);auto k=static_cast<int64_t>(std::floor(q));double u=q-k;return static_cast<float>((1-u)*sample(k,n,channel)+u*sample(k+1,n,channel));}
 void put(int n,float l,float r){samples[static_cast<size_t>(n)%samples.size()]={l,r};}
};
std::array<double,2> input(const Config& c,int n){
 if(c.source.rfind("impulse_",0)==0){if(n)return {0,0};if(c.source=="impulse_center")return {.125,.125};if(c.source=="impulse_left")return {.125,0};if(c.source=="impulse_right")return {0,.125};if(c.source=="impulse_stereo")return {.125,-.0625};if(c.source=="impulse_antiphase")return {.125,-.125};throw std::runtime_error("impulse");}
 double t=double(n)/c.rate,v=0;if(c.source=="step")v=t<2?.125:0;else if(c.source=="sine")v=t<2?.125*std::sin(2*pi*1000*t):0;else if(c.source=="pluck"){for(int onset=0;onset<2;++onset){double tau=t-onset;if(tau>=0&&tau<1)v+=.04*std::exp(-8*tau)*(std::sin(2*pi*220*tau)+std::sin(2*pi*330*tau)+std::sin(2*pi*440*tau));}}else throw std::runtime_error("source");return {v,v};
}
struct Trace{
 int sample,style,destStyle,committedStyle,routeDest,routeCommitted;double desired,oldRead,newRead,alpha,dest,committed,routeWeight;bool active,pending,routeActive,routePending,tempo;double pendingDelay;int pendingStyle,pendingRoute;
};
void writeTrace(std::ostream& o,const Trace& x){o<<x.sample<<",audit,"<<x.desired<<','<<styleName(x.style)<<','<<x.oldRead<<','<<x.newRead<<','<<x.alpha<<','<<x.active<<','<<x.dest<<','<<styleName(x.destStyle)<<','<<x.pending<<','<<x.pendingDelay<<','<<(x.pending?styleName(x.pendingStyle):"none")<<','<<x.committed<<','<<styleName(x.committedStyle)<<','<<x.routeWeight<<','<<x.routeActive<<','<<modeName(x.routeDest)<<','<<x.routePending<<','<<(x.routePending?modeName(x.pendingRoute):"none")<<','<<modeName(x.routeCommitted)<<','<<x.tempo<<'\n';}
void render(const Config& c,const fs::path& dir,std::ostream& metrics){
 const int frames=20*c.rate;Circular memory(c.rate);Time timing(c.style);int initialRoute=(c.schedule.rfind("routing",0)==0||c.schedule=="endpoint")?0:c.mode;Routing routing(initialRoute);Desired desired;desired.style=c.style;desired.route=initialRoute;const auto events=makeEvents(c);size_t cursor=0;const bool motion=c.schedule=="motion";bool finite=true;double statePeak=0,outputPeak=0,el=0,er=0,ef=0;
 std::ofstream audio(dir/(c.id+".f32"),std::ios::binary),trace(dir/(c.id+".trace.csv"));if(!audio||!trace)throw std::runtime_error("output open");trace<<std::setprecision(17)<<"sample,reason,desired_delay,desired_style,read_old,read_new,timing_alpha,timing_active,timing_destination,timing_destination_style,timing_pending,timing_pending_delay,timing_pending_style,committed_delay,committed_style,route_weight,route_active,route_destination,route_pending,route_pending_mode,committed_route,tempo_available\n";
 std::array<std::array<float,2>,4096> chunk{};size_t used=0;Trace previous{};bool hasPrevious=false;int lastWritten=-1,auditNext=-1;const std::array<int,4> irregular={17,113,29,251};size_t blockIndex=0;int n=0;
 while(n<frames){int block=c.partition=="irregular"?irregular[blockIndex++%4]:std::stoi(c.partition);block=std::min(block,frames-n);for(int offset=0;offset<block;++offset,++n){
  bool boundary=timing.retire(n);boundary=routing.retire(n)||boundary;bool event=false,repeat=false;
  while(cursor<events.size()&&events[cursor].n==n){event=true;const Event e=events[cursor++];switch(e.kind){case 0:desired.free=e.value;repeat=true;break;case 1:desired.sync=e.value!=0;break;case 2:desired.bpm=e.value;break;case 3:desired.beat=e.value;break;case 4:desired.style=static_cast<int>(e.value);break;case 5:desired.route=static_cast<int>(e.value);break;case 6:break;default:throw std::runtime_error("event");}}
  if(event)snapshot(desired);
  if(c.mutation=="drop_pending"&&event&&timing.active&&timing.destinationStyle!=2&&desired.delay==timing.committed){desired.delay=timing.to;desired.free=timing.to;}
  if(c.mutation=="restart_repeat"&&repeat&&timing.active&&desired.delay==timing.to&&desired.style==timing.destinationStyle){timing.launch(n,timing.committed,timing.to,timing.destinationStyle,c.rate);boundary=true;}
  boundary=timing.update(n,desired,c.rate)||boundary;boundary=routing.update(n,desired.route,c.rate)||boundary;
  double oldDelay=timing.active?timing.from:timing.committed,newDelay=timing.active?timing.to:timing.committed,alpha=timing.weight(n);
  if(timing.active&&timing.destinationStyle==2){oldDelay=timing.position(n);newDelay=oldDelay;}
  if(motion){const double t=double(n)/c.rate;oldDelay=t<1?.250:t<1.5?.250+.050*(t-1):.275;newDelay=oldDelay;alpha=0;}
  const double rw=routing.weight(n);std::array<float,2> wet{},colored{},stored{},out{};const auto source=input(c,n);
  for(int ch=0;ch<2;++ch){float oldSample=memory.read(n,oldDelay,c.rate,ch,c.mutation=="off_by_one");float newSample=memory.read(n,newDelay,c.rate,ch,c.mutation=="off_by_one");wet[ch]=timing.active&&timing.destinationStyle!=2&&!motion?static_cast<float>((1-alpha)*oldSample+alpha*newSample):oldSample;colored[ch]=static_cast<float>(c.c*wet[ch]);out[ch]=c.pre?wet[ch]:colored[ch];}
  double injectedL=(1-rw)*source[0]+rw*.5*(source[0]+source[1]),injectedR=(1-rw)*source[1];if(c.mutation=="wrong_side")std::swap(injectedL,injectedR);
  stored[0]=static_cast<float>(injectedL+c.g*((1-rw)*colored[0]+rw*colored[1]));stored[1]=static_cast<float>(injectedR+c.g*((1-rw)*colored[1]+rw*colored[0]));memory.put(n,stored[0],stored[1]);
  for(int ch=0;ch<2;++ch){finite=finite&&std::isfinite(stored[ch])&&std::isfinite(out[ch]);statePeak=std::max(statePeak,std::abs(double(stored[ch])));outputPeak=std::max(outputPeak,std::abs(double(out[ch])));}el+=double(out[0])*out[0];er+=double(out[1])*out[1];double fold=.5*(double(out[0])+out[1]);ef+=fold*fold;
  chunk[used++]=out;if(used==chunk.size()){audio.write(reinterpret_cast<const char*>(chunk.data()),static_cast<std::streamsize>(used*sizeof(chunk[0])));used=0;}
  const bool pending=timing.pending(desired),routePending=routing.active&&desired.route!=routing.to;
  Trace row{n,desired.style,timing.active?timing.destinationStyle:timing.committedStyle,timing.committedStyle,routing.active?routing.to:routing.committed,routing.committed,desired.delay,oldDelay,newDelay,alpha,timing.active?timing.to:timing.committed,timing.committed,rw,timing.active,pending,routing.active,routePending,desired.tempo,pending?desired.delay:0,pending?desired.style:0,routePending?desired.route:0};
  if(event||boundary||n==0||n==frames-1){if(hasPrevious&&previous.sample>lastWritten){writeTrace(trace,previous);lastWritten=previous.sample;}if(n>lastWritten){writeTrace(trace,row);lastWritten=n;}auditNext=n+1;}else if(n==auditNext&&n>lastWritten){writeTrace(trace,row);lastWritten=n;}previous=row;hasPrevious=true;
  if(!finite||statePeak>1.25001)throw std::runtime_error("finite/state envelope; retained partial render "+c.id);
 }}
 if(used)audio.write(reinterpret_cast<const char*>(chunk.data()),static_cast<std::streamsize>(used*sizeof(chunk[0])));if(!audio||!trace)throw std::runtime_error("output write");
 metrics<<c.id<<','<<frames<<','<<finite<<','<<statePeak<<','<<outputPeak<<','<<el<<','<<er<<','<<ef<<'\n';
}
int main(int argc,char**argv){try{if(argc!=3)throw std::runtime_error("usage: candidate manifest.csv outputDir");fs::path dir=argv[2];if(fs::exists(dir)&&(!fs::is_directory(dir)||fs::directory_iterator(dir)!=fs::directory_iterator{}))throw std::runtime_error("refusing nonempty output directory; retain prior attempt");fs::create_directories(dir);std::ifstream manifest(argv[1]);if(!manifest)throw std::runtime_error("manifest");std::ofstream metrics(dir/"metrics.csv");metrics<<std::setprecision(17)<<"id,frames,finite,state_peak,output_peak,left_energy,right_energy,fold_energy\n";std::string line;std::getline(manifest,line);int count=0;while(std::getline(manifest,line)){if(!line.empty()&&line.back()=='\r')line.pop_back();if(line.empty())continue;render(Config(split(line)),dir,metrics);if(++count%10==0)std::cout<<"candidate completed "<<count<<std::endl;}std::cout<<"candidate complete "<<count<<std::endl;return 0;}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
