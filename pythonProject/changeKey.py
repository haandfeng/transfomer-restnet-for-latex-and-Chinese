import json

def add_55_to_values(json_data):
    # 遍历JSON数据中的每一个键值对
    for key, value in json_data.items():
        # 对值进行加法操作
        json_data[key] = value + 55

    return json_data

# 读取JSON文件
file_path = 'Chinese.json'  # 请替换成你的JSON文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    # 加载JSON数据
    json_data = json.load(file)

# 对JSON数据进行处理
new_json_data = add_55_to_values(json_data)

# 将处理后的JSON数据写回文件
with open(file_path, 'w', encoding='utf-8') as file:
    # 使用json.dump写回文件
    json.dump(new_json_data, file, ensure_ascii=False, indent=2)
