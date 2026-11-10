@echo off
setlocal
echo ===================================================
echo   PrepWise - Push to GitHub
echo ===================================================
echo.
set /p REPO_URL="Enter your GitHub repository URL (e.g. https://github.com/tanishka180405/prepwise.git): "
if "%REPO_URL%"=="" (
    echo Error: Repository URL cannot be empty.
    pause
    exit /b 1
)

git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main
echo.
echo Pushing to GitHub...
git push -u origin main
echo.
if %errorlevel% equ 0 (
    echo [OK] Successfully uploaded to GitHub!
) else (
    echo [!] Push failed. Please check your GitHub repository URL and credentials.
)
pause
