@echo off
set source="C:\Users\user\Documents\projects\AI-and-ML-learning\batch-script\python_version.txt"
set destination="C:\Users\user\Documents\projects\AI-and-ML-learning\python_version.txt"

copy %source% %destination%

echo File copied from %source% to %destination%
pause
