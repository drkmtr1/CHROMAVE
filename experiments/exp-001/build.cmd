@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul
if errorlevel 1 exit /b 1
if not exist artifacts\exp-001\bin mkdir artifacts\exp-001\bin
cl /nologo /std:c++17 /EHsc /O2 /fp:precise /W4 /Foartifacts\exp-001\bin\candidate.obj /Feartifacts\exp-001\bin\candidate.exe experiments\exp-001\candidate\candidate.cpp
if errorlevel 1 exit /b 1
if exist experiments\exp-001\oracle\oracle.cpp cl /nologo /std:c++17 /EHsc /O2 /fp:precise /W4 /Foartifacts\exp-001\bin\oracle.obj /Feartifacts\exp-001\bin\oracle.exe experiments\exp-001\oracle\oracle.cpp
exit /b %errorlevel%
