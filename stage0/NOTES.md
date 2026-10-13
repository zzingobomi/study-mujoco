# 0단계 노트 — 들어가기

## 0-1. 역사 (2026-10-13)

### 핵심

- MuJoCo = Multi-Joint dynamics with Contact. 워싱턴 대학교의 에마누엘 토도로프가 만들었고, 2012년 논문 "MuJoCo: A physics engine for model-based control"로 처음 소개했다.
- 출발점은 게임이 아니라 모델 기반 제어다. 시뮬레이터로 수없이 미리 돌려 보고 가장 좋은 동작을 고르는 방식이라 엔진에 세 가지가 필요했다.
  - 빠를 것: 논문 기준 사람 모양 모델을 12코어 컴퓨터에서 1초에 약 40만 번 계산
  - 정확하고 안정적일 것
  - 거꾸로(역동역학)도 계산할 것: 물체끼리 닿아 있을 때도
- 연표: 2012 논문 → 2015~ Roboti 유료 판매 → 2016 OpenAI Gym으로 강화학습 표준 시험 환경이 됨 → 2018 DeepMind Control Suite → 2021.10 Google DeepMind 인수·무료화(2.1.0) → 2022.3 공식 Python 바인딩(2.1.2) → 2022.5 오픈 소스(2.2.0, Apache 2.0) → 2023.10 3.0·MJX → 2025.3 Newton 발표(MuJoCo Warp 포함) → 2026.2 MuJoCo Warp 정식 출시(3.5.0) → 2026.10 3.15.0
- 버전이 빠르게 바뀐다(2026년에만 12번). 예제나 문서를 볼 때는 버전부터 확인한다.

### 메모

- 질문 없이 넘어갔다.
- 0-4로 이어지는 질문: "제어 연구용으로 만들어졌다"는 점이 설계에 어떤 흔적을 남겼을까?

### 출처

- [MuJoCo 공식 문서 개요](https://mujoco.readthedocs.io/en/stable/overview.html)
- [MuJoCo 변경 기록](https://mujoco.readthedocs.io/en/stable/changelog.html)
- [2012년 논문 (IEEE Xplore)](https://ieeexplore.ieee.org/document/6386109)
- [Gigazine: DeepMind의 MuJoCo 인수 보도](https://gigazine.net/gsc_news/en/20211019-physics-simulator-for-robotics)
- [OpenAI Gym 논문 (2016)](https://arxiv.org/abs/1606.01540)
- [DeepMind Control Suite 논문 (2018)](https://arxiv.org/abs/1801.00690)
- [NVIDIA의 Newton 발표](https://forums.developer.nvidia.com/t/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/327513)
- [MuJoCo Warp 저장소](https://github.com/google-deepmind/mujoco_warp)
- [Wikipedia: MuJoCo](https://en.wikipedia.org/wiki/MuJoCo)

<details>
<summary>GPT 복붙용</summary>

```text
저는 MuJoCo(로봇·물리 시뮬레이션 엔진)를 처음부터 공부하고 있는 개발자입니다. 아래 [공부 내용]을 저에게 쉽게 설명해 주세요.

[저에 대해]
- 프론트엔드와 Python 백엔드 개발은 어느 정도 합니다.
- 수학은 아주 기초 수준입니다. 미분과 행렬은 대략적으로만 알고, 동역학(힘과 운동)은 처음입니다.
- 로봇 프로젝트에서 MuJoCo를 로봇 자세 계산과 충돌 검사용으로만 써 봤고, 시간을 진행시키는 시뮬레이션 기능은 써 본 적이 없습니다.

[설명 방식]
- 한국어로, 수식 없이, 일상적인 비유와 예시를 들어 설명해 주세요.
- 전문 용어는 처음 나올 때 쉬운 말로 풀어 주세요.
- 큰 그림부터 순서대로 설명해 주세요.
- 아래 내용에 없는 연도, 숫자, 사실을 새로 덧붙이지 마세요. 확실하지 않은 것은 모른다고 말해 주세요.

[공부 내용: MuJoCo의 역사 — 누가, 왜 만들었고, 어떻게 지금에 이르렀나]

1. 이름
- MuJoCo는 Multi-Joint dynamics with Contact의 줄임말이다. 여러 관절로 이어진 물체들이 서로 닿으면서 움직이는 것을 계산하는 엔진이라는 뜻이다.

2. 왜 만들었나
- 워싱턴 대학교의 에마누엘 토도로프가 만들었고, 2012년 논문 "MuJoCo: A physics engine for model-based control"(모델 기반 제어를 위한 물리 엔진)으로 처음 소개했다.
- 모델 기반 제어: 로봇이 "이렇게 움직이면 어떻게 될까"를 시뮬레이터로 수없이 미리 돌려 보고 가장 좋은 동작을 고르는 방식이다. 체스 고수가 머릿속으로 수를 미리 둬 보는 것과 비슷하다.
- 그래서 엔진에 세 가지가 필요했다.
  (1) 빨라야 한다: 논문 기준으로 사람 모양 모델을 12코어 컴퓨터에서 1초에 약 40만 번 계산했다.
  (2) 정확하고 안정적이어야 한다: 예측이 틀리면 고른 동작도 틀린다.
  (3) 거꾸로도 계산할 수 있어야 한다: "이렇게 움직이려면 힘이 얼마나 필요한가"(역동역학)를 계산할 수 있고, 물체끼리 닿아 있을 때도 계산된다.
- 화면에서 자연스럽게 보이는 것이 더 중요한 게임용 물리 엔진과는 출발점이 다르다.

3. 연표
- 2012: 논문으로 처음 소개
- 2015년부터: Roboti라는 회사가 유료로 판매
- 2016: OpenAI Gym(강화학습 연구 도구)에 MuJoCo 기반 환경(HalfCheetah, Hopper, Humanoid 등)이 들어가면서 강화학습 연구의 사실상 표준 시험 환경이 됨
- 2018: DeepMind Control Suite도 MuJoCo로 만들어짐
- 2021년 10월: Google DeepMind가 인수하고 무료로 공개 (버전 2.1.0)
- 2022년 3월: 공식 Python 바인딩 (2.1.2, pip install mujoco)
- 2022년 5월: 소스 코드 전체 공개, 오픈 소스가 됨 (2.2.0, Apache 2.0 라이선스)
- 2023년 10월: MuJoCo 3.0. GPU·TPU에서 대량 병렬로 돌리는 MJX 추가
- 2025년 3월: NVIDIA·Google DeepMind·Disney Research가 GPU 물리 엔진 Newton 공동 개발을 발표. MuJoCo Warp(NVIDIA GPU용 MuJoCo)가 그 일부
- 2026년 2월: MuJoCo Warp 정식 출시 (3.5.0)
- 2026년 10월: 3.15.0. 2026년에만 새 버전이 12번 나올 만큼 빠르게 바뀌는 중

4. 핵심
- MuJoCo는 게임이 아니라 제어 연구를 위해 만들어졌다. 그래서 빠르고, 정확하고, 거꾸로도 계산할 수 있어야 했다.
- 강화학습의 표준 시험 환경이 되면서 널리 퍼졌고, 2021년에 무료가 됐고, 2022년에 오픈 소스가 됐다.
- 지금은 GPU 버전(MJX, MuJoCo Warp)까지 나왔다. 버전이 빠르게 바뀌므로 예제나 문서를 볼 때는 버전을 확인해야 한다.
```

</details>
