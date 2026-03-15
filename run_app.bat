@echo off
REM Handwritten Equation Solver - Startup Script for Windows

echo.
echo ========================================
echo   Handwritten Equation Solver
echo   Powered by Gemini AI & Streamlit
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install/Update requirements
echo Installing dependencies...
pip install -r requirements.txt > nul 2>&1
echo.

REM Launch the app
echo.
echo ========================================
echo   Launching Streamlit App...
echo ========================================
echo.
echo The app will open in your browser at:
echo   http://localhost:8501
echo.
echo Press Ctrl+C to stop the app
echo.
echo ========================================
echo.

streamlit run app.py

pause
