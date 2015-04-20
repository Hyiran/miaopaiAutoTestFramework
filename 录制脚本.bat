@echo off
rem 获取路径
set a=%~dp0
set b="\monkeyrunnerTools\monkey_recorder.py"
set filepath=%a:~0,-1%%b:~1,-1%

rem 执行脚本
monkeyrunner %filepath%