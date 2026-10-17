"""Build release zip package for Ratchet & Clank: Size Matters in accordance with git release standards."""
import os
import shutil
import zipfile
from pathlib import Path

ROOT = Path("g:/Downloads/Korean Traslate Project/Games/Ratchet  Clank - Size Matters")
DIST = ROOT / "dist"
PKG_DIR = DIST / "Ratchet_Clank_Size_Matters_KR_v1.0_20261017"

# Clean/Create package directory
if PKG_DIR.exists():
    shutil.rmtree(PKG_DIR)
PKG_DIR.mkdir(parents=True, exist_ok=True)
(PKG_DIR / "patches").mkdir(parents=True, exist_ok=True)

# 1. Copy xdelta patch and xdelta3 tool
shutil.copy(DIST / "Ratchet_Clank_Size_Matters_KR_v1.0.xdelta", PKG_DIR / "patches/Ratchet_Clank_Size_Matters_KR_v1.0.xdelta")
shutil.copy(ROOT.parent.parent / "Tools/xdelta3-3.2.0-windows-x86_64/xdelta3.exe", PKG_DIR / "xdelta3.exe")

# 2. Create 적용방법.txt
readme_text = """================================================================================
PSP 라쳇 & 클랭크: 사이즈 매터스 (공구들고 바캉스) 한글 패치 v1.0
================================================================================

본 패치는 PlayStation Portable(PSP)용 액션 어드벤처 게임
《라쳇 & 클랭크: 사이즈 매터스 (공구들고 바캉스)》 한국 정식 발매판(UCKS45048 v1.00)의
공식 한글판 번역 오류, 시스템 결함, 캐릭터 보이스 붕괴를 전면 교정한 패치입니다.

일본판 원본(UCJS10052) 및 북미 오리지널 스크립트와의 전수 대조 감사를 통해 총 103건의
치명적 서식 결함, 미번역 영문, 분리된 강조 태그, 캐릭터 말투(클랭크 경어체 복원),
스토리 오역, 무기 및 인게임 퀘스트 번역기 직역투를 완벽하게 정비하였습니다.

--------------------------------------------------------------------------------
1. 파일 목록
--------------------------------------------------------------------------------
- 적용방법.txt                              : 본 안내 문서
- apply.cmd                                 : Windows용 1클릭 자동 패치 실행기 (드래그 앤 드롭 지원)
- apply.py                                  : Python 3 환경용 크로스 플랫폼 패치 스크립트
- xdelta3.exe                               : xdelta3 패치 실행 프로그램
- patches/Ratchet_Clank_Size_Matters_KR_v1.0.xdelta : 한글 패치 델타 파일

--------------------------------------------------------------------------------
2. 패치 대상 및 결과 파일 정보
--------------------------------------------------------------------------------
[지원 원본 ISO]
- 정식 명칭    : 라쳇 & 클랭크: 사이즈 매터스 (공구들고 바캉스) 한국 정발판
- 파일명       : Ratchet & Clank - Size Matters (Korea).iso
- Disc ID      : UCKS45048 (v1.00)
- 파일 크기    : 701,300,736 바이트
- SHA-256 해시 : 16703571011e7e6aff5c37049964e246f28276f2673e2d45ff6ad22856adb817

[패치 파일]
- 파일명       : patches/Ratchet_Clank_Size_Matters_KR_v1.0.xdelta
- 파일 크기    : 10,419 바이트
- SHA-256 해시 : 14e23a7df8aeb936444eccf67eac9b90d6c78e88d338b95f8fac7e02032ee85d

[패치 완료 결과 ISO]
- 파일명       : Ratchet & Clank - Size Matters (Korea) (Updated).iso
- 파일 크기    : 701,300,736 바이트
- SHA-256 해시 : d2597deb3f3b26a9800dc045d9e655162a85991faee83d5482d5b06ef0767185

* 주의: 일본판(UCJS10052), 북미판(UCUS98633), 유럽판(UCES00494)에는 적용되지 않습니다.
  반드시 상기 SHA-256 해시와 일치하는 한국 정발판 원본 ISO를 준비해 주십시오.

--------------------------------------------------------------------------------
3. 패치 적용 방법
--------------------------------------------------------------------------------
[방법 1: Windows 드래그 앤 드롭 (가장 간편)]
1) 다운로드한 압축 파일의 압축을 모두 풉니다.
2) 준비한 한국 정발판 원본 ISO 파일을 마우스로 끌어서 `apply.cmd` 파일 위에 놓습니다.
3) 자동으로 무결성 검사 후 패치가 적용되어 원본 파일 옆에
   `Ratchet & Clank - Size Matters (Korea) (Updated).iso` 파일이 생성됩니다.

[방법 2: apply.cmd 직접 실행]
1) 원본 ISO 파일을 본 폴더 안에 넣고 파일명을
   `Ratchet & Clank - Size Matters (Korea).iso`로 맞춥니다.
2) `apply.cmd`를 더블클릭하여 실행합니다.

[방법 3: Python 3 환경 (Linux, macOS, Windows)]
터미널에서 아래 명령어를 실행합니다.
  python apply.py "Ratchet & Clank - Size Matters (Korea).iso"

--------------------------------------------------------------------------------
4. 주요 수정 내역 요약 (총 103건)
--------------------------------------------------------------------------------
1) 치명적 포맷 스트링 및 매크로 결함 교정
   - `#s` 오류로 인한 보상 아이템 이름 깨짐 복구 (`#s` -> `%s`)
   - 미치환 영문 매크로 태그 `[analog stick]` -> `아날로그 패드` 복구
   - 버튼 아이콘 누락 매크로 `[trianglesymbol]`, `[squaresymbol]` 복구
2) 미번역 영문 및 더미 텍스트 한국어화
   - 메인 메뉴 영문 방치 해소: `LOAD GAME` -> `게임 불러오기`, `NEW GAME` -> `새 게임`
   - `Start 버튼` -> `START 버튼`, `Ok` -> `확인` 표기 정규화
   - 더미 문자열 `?NDEF` -> `문고 등장` 복구
3) 강조 태그(`<COL:02>`) 단어 분리 및 오염 전수 교정 (31건)
   - `<COL:02>폭발<COL:01>시키기` -> `<COL:02>폭발시키기<COL:01>`
   - `메가<COL:02>포탑 글러브<COL:01>` -> `<COL:02>메가 포탑 글러브<COL:01>`
   - `ID 710, 711`: `<COL:02>듀얼 래서레이터 <COL:01>탄약` 공백 위치 정상화
4) 스토리 컷씬 대사 및 캐릭터 보이스 전면 정비
   - 클랭크 존댓말/신사적 어조 복원 (라쳇에게 시비조 반말 쓰던 캐릭터 붕괴 전면 교정)
   - 스토리 오역/유머 복원:
     * 15분 뒤 출동 오역 -> "다음 은하 구출 스케줄까지 15분 남았는데... 뭐, 어때. 몸이나 풀지 뭐."
     * "Be my guest" 오역 "좋도록 해" -> "마음대로 해. 늙어 죽기 전엔 끝내라구!"
     * 라쳇의 핀잔 대사 -> "쉽다고?! 그럼 넌 싸우고 난 낮잠이나 잘란다."
     * 오토 황제의 야욕 -> "태양계"가 아닌 원작 세계관 "온 은하계"로 교정
   - 맞춤법 및 오타 전수 교정: "얻으려도" -> "얻으려고", "눈을 감어" -> "눈을 감아",
     "파해치려면" -> "파헤치려면", "작동불능" -> "작동 불능", "이럴수가" -> "이럴 수가"
5) 인게임 퀘스트/무기/개발 비화 번역기투 전면 윤문
   - 버다닥틸 개발 비화의 유명한 오역 'expensive to run'을 '돈이 들었다'로 오역한 것을
     '연산 부하가 심해 프레임이 떨어졌다'로 올바르게 교정
   - 셰익스피어 암호 명대사('<JA93:0C>여기<JA93:0D>...<JA93:0C>에서<JA93:0D>...<JA93:0C>빠져<JA93:0D>...<JA93:0C>나가<JA93:0D>!')
     조잡한 번역기투 문장을 문학적 번역으로 완성
   - 흡입 대포 설명 '빨아인 후' -> '빨아들인 후' 오타 교정
   - 화폐 표기 '현금', '돈' -> 시리즈 공식 화폐 단위 '볼트'로 전면 통일, '혹성' -> '행성' 통일

--------------------------------------------------------------------------------
5. 권리 표기 및 크레딧
--------------------------------------------------------------------------------
- 원작 개발: High Impact Games / Sony Computer Entertainment
- 한글 패치 제작: AKUMA815 (https://github.com/akuma815)
- 본 패치는 비상업적 팬 패치이며, 원본 게임 소프트웨어는 별도로 소장하셔야 합니다.
"""

(PKG_DIR / "적용방법.txt").write_text(readme_text, encoding="utf-8")

# 3. Create apply.cmd
apply_cmd_text = """@echo off
chcp 65001 > nul
setlocal

echo =======================================================================
echo   라쳇 & 클랭크: 사이즈 매터스 (공구들고 바캉스) 한글 패치 v1.0
echo =======================================================================
echo.

set "SCRIPT_DIR=%~dp0"
set "XDELTA=%SCRIPT_DIR%xdelta3.exe"
set "PATCH=%SCRIPT_DIR%patches\\Ratchet_Clank_Size_Matters_KR_v1.0.xdelta"
set "EXPECTED_OUT=Ratchet & Clank - Size Matters (Korea) (Updated).iso"

if not exist "%XDELTA%" (
    echo [오류] xdelta3.exe 프로그램을 찾을 수 없습니다.
    pause
    exit /b 1
)

if not exist "%PATCH%" (
    echo [오류] 패치 파일을 찾을 수 없습니다: %PATCH%
    pause
    exit /b 1
)

rem 드래그 앤 드롭된 파일이 있는지 확인
if "%~1" neq "" (
    set "SRC=%~1"
    set "OUT_DIR=%~dp1"
    set "OUT=%~dp1Ratchet & Clank - Size Matters (Korea) (Updated).iso"
) else (
    set "SRC=%SCRIPT_DIR%Ratchet & Clank - Size Matters (Korea).iso"
    set "OUT=%SCRIPT_DIR%Ratchet & Clank - Size Matters (Korea) (Updated).iso"
)

if not exist "%SRC%" (
    echo [안내] 원본 ISO 파일을 찾을 수 없습니다.
    echo 한국 정발판 원본 ISO 파일을 이 창에 드래그 앤 드롭하거나,
    echo 본 폴더에 복사 후 'Ratchet & Clank - Size Matters (Korea).iso'로 이름을 변경해주세요.
    echo.
    set /p "SRC=또는 원본 ISO 파일의 전체 경로를 입력하세요: "
    set "OUT=%SCRIPT_DIR%Ratchet & Clank - Size Matters (Korea) (Updated).iso"
)

if not exist "%SRC%" (
    echo [오류] 지정된 원본 파일을 찾을 수 없습니다: %SRC%
    pause
    exit /b 1
)

echo [*] 원본 파일: %SRC%
echo [*] 패치 적용 중입니다... 잠시만 기다려주세요.
echo.

"%XDELTA%" -d -f -s "%SRC%" "%PATCH%" "%OUT%"

if %ERRORLEVEL% equ 0 (
    echo [성공] 한글 패치가 정상적으로 적용되었습니다!
    echo 생성된 파일: %OUT%
) else (
    echo [오류] 패치 적용에 실패했습니다.
    echo 원본 ISO의 해시값(SHA-256)이 '적용방법.txt'에 기재된 값과 일치하는지 확인해주세요.
)

echo.
pause
"""
(PKG_DIR / "apply.cmd").write_text(apply_cmd_text, encoding="cp949")

# 4. Create apply.py
apply_py_text = """#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
XDELTA = ROOT / "xdelta3.exe"
PATCH = ROOT / "patches/Ratchet_Clank_Size_Matters_KR_v1.0.xdelta"

def main():
    if len(sys.argv) > 1:
        src = Path(sys.argv[1])
    else:
        src = ROOT / "Ratchet & Clank - Size Matters (Korea).iso"

    if len(sys.argv) > 2:
        out = Path(sys.argv[2])
    else:
        out = src.parent / "Ratchet & Clank - Size Matters (Korea) (Updated).iso"

    if not src.exists():
        print(f"[Error] Source ISO not found: {src}")
        print("Usage: python apply.py <source_iso> [output_iso]")
        return 1

    if not PATCH.exists():
        print(f"[Error] Patch file not found: {PATCH}")
        return 1

    print(f"[*] Applying patch: {PATCH.name}")
    print(f"[*] Source: {src}")
    print(f"[*] Target: {out}")

    cmd = ["xdelta3", "-d", "-f", "-s", str(src), str(PATCH), str(out)]
    if XDELTA.exists() and sys.platform == "win32":
        cmd[0] = str(XDELTA)

    ret = subprocess.run(cmd)
    if ret.returncode == 0:
        print(f"[+] Success! Patched ISO created at: {out}")
        return 0
    else:
        print("[-] Patch application failed.")
        return ret.returncode

if __name__ == "__main__":
    sys.exit(main())
"""
(PKG_DIR / "apply.py").write_text(apply_py_text, encoding="utf-8")
shutil.copy(PKG_DIR / "적용방법.txt", PKG_DIR / "README.txt")

# 5. Build ZIP
zip_name = DIST / "Ratchet_Clank_Size_Matters_KR_v1.0_20261017.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(PKG_DIR):
        for f in files:
            p = Path(root) / f
            arcname = str(p.relative_to(PKG_DIR)).replace("\\", "/")
            zinfo = zipfile.ZipInfo(arcname)
            zinfo.flag_bits |= 0x800  # UTF-8 flag
            zinfo.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zinfo, p.read_bytes())

print(f"[+] Created {zip_name} (Size: {zip_name.stat().st_size:,} bytes)")
