

import os
import numpy as np


def process_and_filter_text_files(folder_path, start_number=60):
    char_dict = {}
    char_counts = {}

    # 遍历文件夹中的所有 txt 文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                # 将文件中的每个汉字添加到字典中，并计数
                for char in text:
                    if '\u4e00' <= char <= '\u9fff':  # 检查是否为汉字
                        char_counts[char] = char_counts.get(char, 0) + 1
                        if char not in char_dict:
                            char_dict[char] = start_number
                            start_number += 1

    # 筛选出现次数不少于中位数的汉字
    median_count = np.median(list(char_counts.values()))
    filtered_chars = {char: number for char, number in char_dict.items() if char_counts[char] > 0}

    # 将筛选后的字典保存为 txt 文件
    output_path = os.path.join(folder_path, 'result.txt')
    with open(output_path, 'w', encoding='utf-8') as file:
        for char, number in filtered_chars.items():
            file.write(f"'{char}': {number}\n")

    print(f"Result saved to {output_path}")

folder_path = '1'
process_and_filter_text_files(folder_path)

