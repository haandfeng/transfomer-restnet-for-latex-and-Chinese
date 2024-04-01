import os


def filter_txt_files_by_content(folder_path, filter_text):
    # 获取文件夹内所有文件
    files = os.listdir(folder_path)

    # 过滤掉内容包含指定文本的文件
    filtered_files = []

    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if filter_text not in content:
                    filtered_files.append(file)

    return filtered_files


folder_path = './data'
filter_text = '\text'

filtered_files = filter_txt_files_by_content(folder_path, filter_text)

print("过滤后的txt文件:")
for file in filtered_files:
    print(file)
