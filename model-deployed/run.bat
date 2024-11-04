@echo off

REM Check if Python is installed
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    exit /b
)

REM Check for the virtual environment
IF EXIST ".venv" (
    echo Activating the virtual environment...
    call .venv\Scripts\activate.bat
) ELSE (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate.bat
)

REM Install dependencies
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt not found. Skipping dependency installation.
)

REM Run the main script
echo Running Streamlit App...
python -m streamlit run main.py

@REM REM Urge to open localhost webpage
@REM echo Please open your web browser and go to http://localhost:8000 or your respective port.
