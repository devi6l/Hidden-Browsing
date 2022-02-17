@echo off
chcp 65001 >nul
title devil boy anon V0.1
color 2
pip install ascii_magic
cls
:logo
color 2
echo INSTALL TOR 1
echo VPN 2
echo MAC ADDRESS CHANGER 3
set /p mode=Choose the mode : 
if %mode% == 1 goto TOR
if %mode% == 2 goto VPN
if %mode% == 3 goto MAC
cls
goto logo
:TOR
python tor.py
start torbrowser-install-win64-11.0.2_en-US.exe
cls
goto logo
:VPN
python vpn.py
start psiphon3.exe
cls
goto logo
:MAC
python CHANGER.py
start TMACv6.0.7_Setup.exe
cls
goto logo