@echo off
rem 获取录制脚本路径
set a=%~dp0
set b=template2.py
set filepath=%a%%b%

rem 执行脚本
start monkeyrunner %filepath%