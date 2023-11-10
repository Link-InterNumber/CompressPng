@echo off

set path=%~d0%~p0

:start

for %%a in (%*) do  (
    "%path%ConvertPngToJpg_PIL_Single.exe" %1
)

shift
if NOT x%1==x goto start