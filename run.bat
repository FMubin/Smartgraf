@echo off
echo ===================================================
echo   MEMULAI INFOGRAFIS GENERATOR KECAMATAN
echo ===================================================
echo.
echo Server lokal sedang dijalankan di http://localhost:8000
echo Tekan Ctrl+C di jendela ini untuk menghentikan server.
echo.
start "" "http://localhost:8000"
py -m http.server 8000
pause
