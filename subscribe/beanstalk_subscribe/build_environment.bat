DON'T BOTHER WITH THIS SCRIPT

ECHO OFF
echo Creating virtual environment for beanstalk_publish...
SET VENV=.venv

echo python -m venv .venv
python -m venv .venv

echo .venv\Scripts\activate.bat
.venv\Scripts\activate.bat

rem have to put these in the actual activate.bat script, manually
rem SET PYTHONPATH=C:\Users\oggie\visual-studio-workspace-duke\pubsub\beanstalk_subscribe
rem echo PYTHONPATH: %PYTHONPATH%

pip install -r requirements.txt
