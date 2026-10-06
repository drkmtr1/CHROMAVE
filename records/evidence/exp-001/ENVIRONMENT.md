# EXP-001 execution environment

Observed2026-10-05, coordinator local preflight. Windows11 build10.0.26200; runtime machineAMD64. Processor identifier: ARMv8 (64-bit) Family8 ModelD4B Revision0, Qualcomm Technologies Inc;8 logical processors reported by environment. This is an x64 MSVC/Python runtime on an ARM machine; native-x64 support/performance was not tested. Full CPU model/OS CIM metadata query denied; unknown beyond these runtime identifiers.

Existing Python C:\Python313\python.exe,3.13.5 [MSC v.1943 64bit AMD64]; existing NumPy2.5.0. Visual Studio2022 BuildTools, MSVC directory14.44.35207; actual cl identifies19.44.35228 forx64. /std:c++17 /EHsc /O2 /fp:precise /W4. No dependency/tool installation. Compiler version obtained through existing vcvars64.bat environment and cl banner; no performance claim follows.

C: free40.87GiB at preflight. Accepted primary data1.80GiB float +3.60GiB double, negatives/traces/listening additional; task budget15GiB. Hashes, exact commands and raw file sizes recorded separately. State memory bounded per render; no process-wide peak-memory benchmark performed. System locale/driver/audio-device/FL Studio metadata not inspected because standalone numerical outputs do not use an audio device/host.

Actual outputs are binary little-endian IEEE754 stereo float32(candidate) / float64(reference),20fs frames each. Candidate writes platform-native float bytes on this observed little-endian x64 runtime; reference explicitly emits little-endian bytes. Encoding/byte counts are checked against the independently emitted reference. Candidate writer portability to another byte order is not claimed. All rendering is offline; real-time deadline/native plugin/VST3/FL Studio conformance remains untested.
