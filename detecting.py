import subprocess
import os
import sys

sys.path.append(r"C:\Users\ASUS\anaconda3\Lib\site-packages")


class Detecting:
    """
    automatically do prediction by command
    用cmd在同一个虚拟环境中执行预测任务(使用conda跨环境执行通常会出错)
    """
    def __init__(self, predict_path=None):
        # 程序路径
        self.py_path = r"./train.py"
        # 待测图像路径
        if not predict_path:
            self.predict_path = r"./image/000.png"
        else:
            self.predict_path = predict_path
        # 输出路径
        self.output_path = r"./output"

    def run(self):
        cmd = fr'python "{self.py_path}" --predict_path="{self.predict_path}" --output_path="{self.output_path}" '
        ret = subprocess.run(cmd, cwd=os.getcwd(), shell=True)
        print(ret)

# cmd = r'C:\Users\ASUS\anaconda3\condabin\conda.bat run -n detection python --version'
# cmd = fr'conda run -n detection python "{py_path}" --predict_path="{predict_path}" --output_path="{output_path}" '
# cmd = ['conda.bat', 'activate', 'detection', '&&', 'python', r'E:\School\Python_Programme\defect_detection\print2.py']
# cmd = ['conda.bat', 'activate', 'detection', '&&', 'conda', 'env', 'list']


detect = Detecting()
detect.run()