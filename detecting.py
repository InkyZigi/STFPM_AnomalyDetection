import subprocess
import os
import sys
import platform

sys.path.append(r"C:\Users\ASUS\anaconda3\Lib\site-packages")


class Detecting:
    """
    automatically do prediction by command
    用cmd在同一个虚拟环境中执行预测任务(使用conda跨环境执行通常会出错)
    """
    def __init__(self, py_path=None, predict_path=None, project_path=None, output_path=None, category=None, ):
        # 程序路径
        if py_path:
            self.py_path = py_path
        else:
            self.py_path = r"./train.py"
        # 待测图像路径
        if predict_path:
            self.predict_path = predict_path
        else:
            self.predict_path = r"./image/000.png"
        # 模型路径
        if project_path:
            self.project_path = project_path
        else:
            self.project_path = r"./test/"
        # 输出路径
        if output_path:
            self.output_path = output_path
        else:
            self.output_path = r"./output/"
        # 图像类别
        if category:
            self.category = category
        else:
            self.category = "wood"

    def run(self):
        cmd = fr"""python "{self.py_path}" --predict_path="{self.predict_path}" --project_path="{self.project_path}" --output_path="{self.output_path}" --phase="predict" --category="{self.category}" """
        ret = subprocess.run(cmd, cwd=os.getcwd(), shell=True)
        print(ret)

# cmd = r'C:\Users\ASUS\anaconda3\condabin\conda.bat run -n detection python --version'
# cmd = fr'conda run -n detection python "{py_path}" --predict_path="{predict_path}" --output_path="{output_path}" '
# cmd = ['conda.bat', 'activate', 'detection', '&&', 'python', r'E:\School\Python_Programme\defect_detection\print2.py']
# cmd = ['conda.bat', 'activate', 'detection', '&&', 'conda', 'env', 'list']


detect = Detecting()
detect.run()