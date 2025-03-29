@echo off
call C:/OSGeo4W/bin/o4w_env.bat
@echo on

C:/OSGeo4W/apps/Python312/Scripts/pyrcc5.exe -o resources.py resources.qrc

xcopy C:\dev\geodms_qgis\geodms C:\OSGeo4W\apps\qgis\python\plugins\geodms /E /H /C /I

