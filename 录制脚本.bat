@echo off
rem ��ȡ·��
set a=%~dp0
set b="\monkeyrunnerTools\monkey_recorder.py"
set filepath=%a:~0,-1%%b:~1,-1%

rem ִ�нű�
monkeyrunner %filepath%