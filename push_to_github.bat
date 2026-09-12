@echo off
set "PATH=%PATH%;C:\Users\BPS\AppData\Local\MinGit\cmd"
echo ===================================================
echo   SMARTGRAF - Push ke GitHub
echo ===================================================
echo.
set /p REPO_URL="Masukkan URL GitHub Repo (contoh: https://github.com/user/repo.git): "
if "%REPO_URL%"=="" (
    echo [ERROR] URL tidak boleh kosong.
    pause
    exit /b
)

git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main
echo.
echo Sedang mengunggah (push) ke GitHub...
git push -u origin main

echo.
echo Selesai!
pause
