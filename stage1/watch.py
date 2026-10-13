"""1-1 보조. swing.py와 같은 진자를 화면으로 본다. 창을 닫으면 끝난다.

실행: uv run stage1/watch.py
"""

import math
import time
from pathlib import Path

import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("pendulum.xml")))
data = mujoco.MjData(model)
data.qpos[0] = math.radians(90)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()  # 바뀐 상태를 화면에 반영한다
        time.sleep(model.opt.timestep)  # 실제 시간과 대략 맞춘다
