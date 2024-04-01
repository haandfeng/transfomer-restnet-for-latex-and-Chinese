from http import HTTPStatus

import numpy as np
from albumentations.pytorch.transforms import ToTensorV2
from fastapi import FastAPI, File, UploadFile
from PIL import Image

from image_to_latex.lit_models import LitResNetTransformer

app = FastAPI(
    title="Image to Latex Convert",
    desription="Convert an image of math equation into LaTex code.",
)


@app.on_event("startup")
async def load_model():
    global lit_model
    global transform
    lit_model = LitResNetTransformer.load_from_checkpoint(
        "../scripts/outputs/2023-12-12/00-04-04/image-to-latex/35otpit7/checkpoints/epoch=15-val/loss=0.02-val/cer=0.65.ckpt")
    lit_model.freeze()
    transform = ToTensorV2()




def predict(file_path: str):
    with open(file_path, "rb") as file:
        image = Image.open(file).convert("L")
        image_tensor = transform(image=np.array(image))["image"]  # type: ignore
        pred = lit_model.model.predict(image_tensor.unsqueeze(0).float())[0]  # type: ignore
        decoded = lit_model.tokenizer.decode(pred.tolist())  # type: ignore
        decoded_str = " ".join(decoded)
        # response = {
        #     "message": HTTPStatus.OK.phrase,
        #     "status-code": HTTPStatus.OK,
        #     "data": {"pred": decoded_str},
        # }
        return decoded_str


import asyncio
import os


# 其他导入和函数定义

async def main(folder_path: str, output_folder: str):
    # async def main():
    await load_model()
    # print(predict("../test/images/3117.png"))
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png"):
            file_path = os.path.join(folder_path, file_name)
            prediction = predict(file_path)
            # print(f"File: {file_name}, Prediction: {prediction}")
            # 构建输出文件路径
            output_file_name = file_name.replace(".png", ".txt")
            output_file_path = os.path.join(output_folder, output_file_name)

            # 将结果写入文本文件
            with open(output_file_path, "w",encoding='utf-8') as output_file:
                output_file.write(prediction)

            print(f"File: {file_name}, Prediction written to: {output_file_path}")


if __name__ == "__main__":
    asyncio.run(main("../test/images/", "../test/prediction2312121003/"))
    # asyncio.run(main())
