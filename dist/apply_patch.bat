@echo off
chcp 65001 > nul
echo =======================================================================
echo   라쳇 & 클랭크: 사이즈 매터스 (공구들고 바캉스) 한글 패치 v1.0
echo =======================================================================
echo.

set XDELTA=xdelta3.exe
set PATCH=Ratchet_Clank_Size_Matters_KR_v1.0.xdelta
set SRC=Ratchet & Clank - Size Matters (Korea).iso
set OUT=Ratchet & Clank - Size Matters (Korea) (Updated).iso

if not exist "%XDELTA%" (
    echo [오류] %XDELTA% 파일이 같은 폴더에 없습니다.
    pause
    exit /b 1
)

if not exist "%PATCH%" (
    echo [오류] %PATCH% 패치 파일이 없습니다.
    pause
    exit /b 1
)

if not exist "%SRC%" (
    echo [안내] 원본 ISO 파일("%SRC%")을 찾을 수 없습니다.
    echo 이 배치 파일이 있는 폴더에 한국 정발판 원본 ISO를 두고
    echo 파일 이름을 "%SRC%"로 변경해주세요.
    echo.
    pause
    exit /b 1
)

echo [*] 패치를 적용하고 있습니다. 잠시만 기다려주세요...
"%XDELTA%" -d -f -s "%SRC%" "%PATCH%" "%OUT%"

if %ERRORLEVEL% equ 0 (
    echo.
    echo [성공] 한글 패치 적용이 완료되었습니다!
    echo 생성된 파일: %OUT%
) else (
    echo.
    echo [실패] 패치 적용 중 오류가 발생했습니다. 원본 ISO의 무결성을 확인해주세요.
)

echo.
pause

