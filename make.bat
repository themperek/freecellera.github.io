@ECHO OFF

if "%PELICAN%" == "" (
	set PELICAN=pelican
)

set INPUTDIR=content
set OUTPUTDIR=output
set PUBLISHCONF=publishconf.py
set PELICANOPTS=


if "%1" == "publish" (
	%PELICAN% %INPUTDIR% -o %OUTPUTDIR% -s %PUBLISHCONF% %PELICANOPTS% 
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %OUTPUTDIR%.
	goto end
)

if "%1" == "clean" (
	rmdir /q /s %OUTPUTDIR%
	rmdir /q /s cache
	goto end
)

if "%1" == "server" (
	cd %OUTPUTDIR%
	python -m SimpleHTTPServer
)



:end
