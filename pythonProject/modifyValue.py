def process_lines(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    processed_lines = []
    for i, line in enumerate(lines):
        # 如果行以斜杠 \ 开头，则将开头的单个斜杠 \ 替换为两个斜杠 \\
        if line.startswith('\\'):
            line = line.replace('\\', '\\\\', 1)

        # 使用双引号括住每一行
        formatted_line = f'"{line.strip()}"'

        # 在每一行末尾加上行号
        formatted_line += f': {i},'

        processed_lines.append(formatted_line + '\n')

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(processed_lines)


if __name__ == "__main__":
    input_path = "output_union2.txt"  # 替换为你的输入文本文件路径
    output_path = "vocab2.json"  # 输出的文本文件路径

    process_lines(input_path, output_path)
