"""
run tensorboard by command
用命令运行 tensorboard 可视化算法训练结果：包括Training Loss、ROC-AUC等
不要将本文件改名为 tensorboard.py，否则报错
"""

import subprocess
import tensorboard

# give a path like '......\test\wood(type)\lightning_logs\version_1(version_X)'
dir = r'E:\CODE\Python\defect_detection_experiment\STFPM_AD\test\wood\lightning_logs\version_1'
cmd = f"tensorboard --logdir={dir} --port 6007"
print(cmd)
subprocess.run(cmd)