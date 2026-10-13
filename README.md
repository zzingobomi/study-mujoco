# study-mujoco

MuJoCo 물리 엔진을 기초부터 공부하는 저장소.

- 계획과 진도: [ROADMAP.md](ROADMAP.md)
- Claude Code가 읽는 작업 지침: [CLAUDE.md](CLAUDE.md)

## 새 PC에서 이어서 하기

1. 저장소를 clone한다.
2. 폴더에서 `uv sync`를 실행한다. Python 3.11과 mujoco 3.15.0이 다른 PC와 똑같이 설치된다. (uv가 없다면 먼저 설치한다.)
3. 그 PC의 전역 git 작성자가 개인 계정이 아니라면, 이 저장소에만 `git config --local user.name`과 `git config --local user.email`로 개인 계정을 설정한다. 이 설정은 저장소와 함께 옮겨지지 않는다.
4. 이 폴더에서 Claude Code를 열고 "이어서 하자"라고 하면, ROADMAP.md의 현재 위치부터 이어 간다.

## 실험 실행

```bash
uv run stage1/swing.py   # 숫자로 보기
uv run stage1/watch.py   # 화면으로 보기 (macOS에서는 uv run mjpython stage1/watch.py)
```
