@echo off
set floder=%1%
set p_path=%~dp0
python %p_path%\CompressPng.py -p %floder%
pause