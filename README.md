# Local Nanum Font Setup

sudo 권한 없이도 `fonts-nanum` 패키지가 제공하는 한글 글꼴을 사용할 수 있도록
프로젝트에 필요한 TTF 파일과 Matplotlib 헬퍼를 함께 넣어두었습니다.

## 동작 원리
- `fonts/nanum` 디렉터리에 `NanumGothic`, `NanumMyeongjo` 등 주요 Nanum 글꼴 TTF를 보관합니다.
- `nanum_font.py`가 해당 경로의 글꼴을 Matplotlib font manager에 직접 등록하고,
  기본 글꼴을 Nanum 계열로 설정합니다.
- 따라서 `apt-get install fonts-nanum`, `fc-cache` 같은 루트 권한 명령을 실행할 필요가 없습니다.

## 사용 방법
1. (최초 1회) Matplotlib을 설치합니다.
   ```bash
   pip install matplotlib
   ```
2. 그래프를 그리기 전에 아래 헬퍼를 호출합니다.
   ```python
   from nanum_font import use_nanum_font

   use_nanum_font()  # 기본값은 NanumGothic
   ```
3. 이후 `plt.title("안녕하세요")`처럼 한글 텍스트를 그대로 사용할 수 있습니다.

### 커스터마이징
- 다른 Nanum 계열을 기본으로 쓰고 싶다면 `use_nanum_font(font_family="NanumMyeongjo")`
  처럼 옵션을 넘겨주세요.
- 추가로 필요한 TTF가 있다면 `fonts/nanum` 폴더에 파일을 복사한 뒤 다시
  `use_nanum_font()`를 호출하면 됩니다.
- Matplotlib이 예전 캐시를 계속 참조한다면 `rm -rf ~/.cache/matplotlib`
  명령으로 사용자 캐시만 지우면 됩니다. (sudo 불필요)

### 참고
`register_nanum_fonts()` 함수만 호출하면 글꼴 등록만 수행하고 `rcParams`는 그대로 두므로,
세밀한 설정이 필요할 때 활용할 수 있습니다.