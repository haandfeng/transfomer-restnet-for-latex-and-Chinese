import re
import json

def process_line(line):
    # 使用正则表达式匹配键值对
    match = re.match(r'\\([^:]+): (\d+)', line)
    if match:
        key = match.group(1)
        value = int(match.group(2))
        data = {key: value}
        return data
    else:
        # 如果行格式不匹配，可以根据实际情况进行处理
        return {"unmatched_line": line.strip()}

def txt_to_json(txt_file_path, json_file_path):
    result_data = []

    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        for line in txt_file:
            processed_data = process_line(line)
            result_data.append(processed_data)

    # 将结果写入 JSON 文件
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(result_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    txt_file_path = "your_input.txt"  # 替换为你的输入文本文件路径
    json_file_path = "output.json"  # 输出的 JSON 文件路径

    txt_to_json(txt_file_path, json_file_path)
