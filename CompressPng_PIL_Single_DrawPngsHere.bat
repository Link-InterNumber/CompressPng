@echo off

set path=%~d0%~p0

:start

for %%a in (%*) do  (
    "%path%CompressPng_PIL_Single.exe" %%a
)

pause