"""1-1. 진자를 만들고 돌려 본다.

MuJoCo의 기본 흐름:
    XML(설계도) → MjModel(모델) → MjData(상태) → mj_step(시간 진행)

실행: uv run stage1/swing.py
"""

import math
from pathlib import Path

import mujoco

# 1) 설계도(XML)를 읽어 모델을 만든다.
#    모델은 시뮬레이션 내내 바뀌지 않는 정보다. 몸체 구조, 질량, 시간 간격 같은 것들.
model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("pendulum.xml")))

# 2) 모델로 상태를 만든다.
#    시간, 관절 각도, 각속도처럼 매 순간 바뀌는 값은 전부 여기에 있다.
data = mujoco.MjData(model)

# 3) 출발 자세: 막대를 90도(수평)로 들어 올린다.
#    바꾸는 것은 상태(data)이지 모델(model)이 아니다.
data.qpos[0] = math.radians(90)

# 4) 시간을 진행시킨다. mj_step 한 번에 model.opt.timestep 초가 흐른다.
print(f"시간 간격: {model.opt.timestep}초")
print(f"출발 각도: {math.degrees(data.qpos[0]):.2f}도\n")

seconds = 2.0
steps = round(seconds / model.opt.timestep)
lowest = 0.0  # 반대편(음수 쪽)으로 가장 많이 올라간 각도

for i in range(1, steps + 1):
    mujoco.mj_step(model, data)
    angle = math.degrees(data.qpos[0])
    lowest = min(lowest, angle)
    if i % 50 == 0:  # 50번 = 0.1초마다 한 줄씩 출력
        print(f"{data.time:4.1f}초   각도 {angle:7.2f}도")

print(f"\nmj_step 호출 횟수: {steps}번")
print(f"반대편으로 가장 높이 올라간 각도: {abs(lowest):.3f}도 (출발은 90도)")
