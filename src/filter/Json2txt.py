import re

def remove_colon_and_numbers(txt_file_path, output_path):
    with open(txt_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # 使用正则表达式去掉每一行的 ": 数字"
    modified_lines = [re.sub(r':\s*\d+', '', line) for line in lines]

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(modified_lines)

if __name__ == "__main__":
    txt_file_path = "your_text_file.txt"  # 替换为你的文本文件路径
    output_path = "output_modified.txt"    # 输出的文本文件路径

    remove_colon_and_numbers(txt_file_path, output_path)
