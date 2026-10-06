"""Independently authored EXP-001 matrix;204 primary and4 negative controls."""
import argparse,csv,itertools,math
from collections import Counter
from pathlib import Path
FIELDS=['id','panel','style','mode','source','schedule','rate','partition','feedback','char_gain','tap','mutation']
STYLES=('A','B','C');MODES=('stereo','pingpong');RATES=(44100,48000,96000);PARTITIONS=('1','64','512','irregular')
IMPULSES=('impulse_center','impulse_left','impulse_right','impulse_stereo','impulse_antiphase')
EXPECTED={'P1':60,'P2':24,'P3':3,'P4':3,'P5':72,'P6':12,'P7':6,'P8':6,'P9':12,'P10':6}
def half_up(t,rate):return math.floor(t*rate+.5)
def fade_frames(style,rate):return max(1,half_up(.005 if style=='B' else .020,rate))
def make_id(row):return '__'.join(str(row[k]).replace('.','p') for k in FIELDS if k!='id')
def make_row(panel,style='A',mode='stereo',source='sine',schedule='static',rate=48000,partition='irregular',feedback=.5,char_gain=1,tap='post',mutation='none'):
 r=dict(panel=panel,style=style,mode=mode,source=source,schedule=schedule,rate=rate,partition=partition,feedback=format(feedback,'.12g'),char_gain=format(char_gain,'.12g'),tap=tap,mutation=mutation);r['id']=make_id(r);assert all(c.isascii() and(c.isalnum() or c=='_') for c in r['id']);return r
def primary_rows():
 r=[]
 for src,tap,mode,rate in itertools.product(IMPULSES,('pre','post'),MODES,RATES):r.append(make_row('P1',source=src,tap=tap,mode=mode,rate=rate,partition='64',char_gain=.5))
 for sched,sty,mode in itertools.product(('retarget','mode_collision','timing_return','timing_repeat'),STYLES,MODES):r.append(make_row('P2',schedule=sched,style=sty,mode=mode))
 for sty in STYLES:r.append(make_row('P3',schedule='endpoint',style=sty))
 for sched in('routing','routing_return','routing_repeat'):r.append(make_row('P4',source='step',schedule=sched))
 for sty,mode,rate,part in itertools.product(STYLES,MODES,RATES,PARTITIONS):r.append(make_row('P5',schedule='retarget',style=sty,mode=mode,rate=rate,partition=part,feedback=.9))
 for rate,part in itertools.product(RATES,PARTITIONS):r.append(make_row('P6',source='step',schedule='routing',rate=rate,partition=part,feedback=.9))
 for sty,mode in itertools.product(STYLES,MODES):r.append(make_row('P7',schedule='retarget',style=sty,mode=mode,feedback=0))
 for mode,g in itertools.product(MODES,(0,.5,.9)):r.append(make_row('P8',source='impulse_center',mode=mode,feedback=g,partition='64'))
 for rate,part in itertools.product(RATES,PARTITIONS):r.append(make_row('P9',schedule='motion',rate=rate,partition=part,feedback=0))
 for sty,mode in itertools.product(STYLES,MODES):r.append(make_row('P10',source='pluck',schedule='retarget',style=sty,mode=mode))
 assert Counter(x['panel'] for x in r)==Counter(EXPECTED);assert len(r)==204;assert sum(20*x['rate']*8 for x in r)==1933632000;return r
def negative_rows(primary):
 selections=(('N1','wrong_side',dict(panel='P1',source='impulse_center',tap='post',mode='pingpong',rate=48000)),('N2','off_by_one',dict(panel='P1',source='impulse_center',tap='post',mode='pingpong',rate=48000)),('N3','drop_pending',dict(panel='P2',style='A',mode='stereo',schedule='timing_return')),('N4','restart_repeat',dict(panel='P2',style='A',mode='stereo',schedule='timing_repeat')));r=[]
 for panel,mutation,criteria in selections:
  matches=[x for x in primary if all(x[k]==v for k,v in criteria.items())];assert len(matches)==1;row=dict(matches[0]);row.update(panel=panel,mutation=mutation);row['id']=make_id(row);r.append(row)
 return r
def ordered_events(row):
 rate,sty,sched=row['rate'],row['style'],row['schedule'];events=[]
 def at(sample,control,payload):events.append((sample,len(events),control,str(payload)))
 def sec(t,control,payload):at(half_up(t,rate),control,payload)
 for control,payload in [('initial_free','0.250'),('initial_sync_division','1'),('initial_bpm','120'),('initial_style',sty),('initial_route',row['mode'])]:at(0,control,payload)
 if sched=='retarget':
  for t,v in [(1,'0.375'),(1.005,'0.125'),(1.009,'0.300')]:sec(t,'free',v)
 elif sched=='mode_collision':
  for t,k,v in [(1,'division','1'),(1,'bpm','120'),(1,'select','sync'),(1.005,'bpm','90'),(1.009,'bpm','INVALID_TEMPO_NONFINITE'),(1.009,'division','0.5'),(1.009,'division','1'),(1.020,'free','0.250'),(1.020,'select','free'),(1.020,'style','A' if sty=='C' else 'C')]:sec(t,k,v)
 elif sched in('timing_return','timing_repeat'):sec(1,'free','0.375');sec(1.002,'free','0.250' if sched=='timing_return' else '0.375')
 elif sched=='routing':sec(1,'route','pingpong');sec(1.005,'route','stereo');sec(1.009,'route','pingpong')
 elif sched in('routing_return','routing_repeat'):sec(1,'route','pingpong');sec(1.002,'route','stereo' if sched=='routing_return' else 'pingpong')
 elif sched=='endpoint':
  n=half_up(1,rate);at(n,'free','0.375');at(n,'route','pingpong');at(n+fade_frames(sty,rate),'free','0.300');at(n+fade_frames('A',rate),'route','stereo')
 elif sched=='motion':sec(1,'motion','ramp_0.250_to_0.275_until_1.500');sec(1.5,'motion','hold_0.275')
 elif sched!='static':raise ValueError(sched)
 events.sort(key=lambda e:(e[0],e[1]));orders=Counter();result=[]
 for sample,_,control,payload in events:order=orders[sample];orders[sample]+=1;result.append(dict(id=row['id'],sample=sample,order=order,control=control,payload=payload))
 return result
def write_csv(path,fields,data):
 if path.exists():raise RuntimeError(f'Refusing to overwrite manifest {path}')
 with path.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
def main():
 p=argparse.ArgumentParser();p.add_argument('manifest',type=Path);a=p.parse_args();primary=primary_rows();negative=negative_rows(primary);data=primary+negative;assert len(data)==208 and len({x['id'] for x in data})==208;a.manifest.parent.mkdir(parents=True,exist_ok=True)
 write_csv(a.manifest,FIELDS,data);write_csv(a.manifest.with_name('primary.csv'),FIELDS,primary);write_csv(a.manifest.with_name('negative.csv'),FIELDS,negative);write_csv(a.manifest.with_name('events.csv'),('id','sample','order','control','payload'),[e for row in data for e in ordered_events(row)]);print('204 primary;4 negative;primary raw bytes1933632000')
if __name__=='__main__':main()
