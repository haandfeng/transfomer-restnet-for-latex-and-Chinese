from http import HTTPStatus

import numpy as np
from albumentations.pytorch.transforms import ToTensorV2
# from fastapi import FastAPI, File, UploadFile
from PIL import Image

from image_to_latex.lit_models import LitResNetTransformer

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import asyncio
from http import HTTPStatus

import numpy as np
from albumentations.pytorch.transforms import ToTensorV2
# from fastapi import FastAPI, File, UploadFile
from PIL import Image

from image_to_latex.lit_models import LitResNetTransformer

# 定义主窗口类


# app = FastAPI(
#     title="Image to Latex Convert",
#     desription="Convert an image of math equation into LaTex code.",
# )


# @app.on_event("startup")
async def load_model():
    global lit_model
    global transform
    lit_model = LitResNetTransformer.load_from_checkpoint("../scripts/outputs/2023-12-10/18-23-13/image-to-latex/4hxczlzh/checkpoints/epoch=14-val/loss=0.09-val/cer=0.04.ckpt")
    lit_model.freeze()
    transform = ToTensorV2()



def predict(file_path: str):
    with open(file_path, "rb") as file:
        image = Image.open(file).convert("L")
        image_tensor = transform(image=np.array(image))["image"]  # type: ignore
        pred = lit_model.model.predict(image_tensor.unsqueeze(0).float())[0]  # type: ignore
        decoded = lit_model.tokenizer.decode(pred.tolist())  # type: ignore
        decoded_str = "".join(decoded)
        # response = {
        #     "message": HTTPStatus.OK.phrase,
        #     "status-code": HTTPStatus.OK,
        #     "data": {"pred": decoded_str},
        # }
        return decoded_str

import asyncio
import os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = ""
        # 设置窗口标题和大小
        self.setWindowTitle('图片识别')
        self.resize(400, 300)
        self.result = ""
        # 创建上传按钮和标签
        self.upload_btn = QPushButton('上传图片', self)
        self.upload_btn.clicked.connect(self.upload_image)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        print(self.image_label)

        # 创建下拉框和标签
        self.model_label = QLabel('选择模型:', self)
        self.model_combo = QComboBox(self)
        self.model_combo.addItem('模型1')
        self.model_combo.addItem('模型2')

        # 创建预测按钮和标签
        self.predict_btn = QPushButton('预测', self)
        self.predict_btn.clicked.connect(self.predict_image)
        self.result_label = QLabel(self)

        # 创建布局
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.upload_btn)
        hbox.addWidget(self.image_label)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.model_label)
        hbox.addWidget(self.model_combo)
        vbox.addLayout(hbox)
        vbox.addWidget(self.predict_btn)
        vbox.addWidget(self.result_label)
        self.setLayout(vbox)
    def predict11(file_path):
        print("aaa")
        print(file_path)
        with open(file_path, "rb") as file:
            print(6)
            image = Image.open(file).convert("L")
            print(7)
            image_tensor = transform(image=np.array(image))["image"]  # type: ignore
            print(8)
            pred = lit_model.model.predict(image_tensor.unsqueeze(0).float())[0]  # type: ignore
            print(9)
            decoded = lit_model.tokenizer.decode(pred.tolist())  # type: ignore
            print(10)
            decoded_str = "".join(decoded)
            print(11)

            # response = {
            #     "message": HTTPStatus.OK.phrase,
            #     "status-code": HTTPStatus.OK,
            #     "data": {"pred": decoded_str},
            # }

            return decoded_str

    # 上传图片
    def upload_image(self):
        print(1)
        file_path, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', '图片文件 (*.png *.jpg *.jpeg)')
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
            self.file_path = file_path
        # self.path = file_path
        print(file_path)
        # self.load_model()
        print(2)
        # a = self.predict11(file_path)

        print(21)
        # print(a)
    # 预测图片
    def predict_image(self):
        model_name = self.model_combo.currentText()
        # await self.load_model()

        # 在此处添加调用模型预测的代码，将预测结果存储在 prediction 变量中

        asyncio.run(main(self.file_path))

        self.result_label.setText('预测结果为：{}'.format(self.result))



if __name__ == "__main__":
    # asyncio.run(main("../dataset/test/images","../dataset/test/prediction"))
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # asyncio.run(main("../dataset/test/images","../dataset/test/prediction"))


    sys.exit(app.exec_())
