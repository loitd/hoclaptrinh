@echo off
cls
echo This Emulator Starter script made by Tran Duc Loi (youtube.com/tranducloi)
echo version 1.0 on Windows
echo --------------------------------------------------------------------------
echo List of your avd(s):
%LOCALAPPDATA%\Android\Sdk\tools\emulator.exe -list-avds
echo Now run avd:
%LOCALAPPDATA%\Android\Sdk\tools\emulator.exe @5.0inch-7.1.1x86
pause