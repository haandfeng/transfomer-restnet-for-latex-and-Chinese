def union_of_lines(file1_path, file2_path, output_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        lines1 = set(file1.readlines())
        lines2 = set(file2.readlines())

    # 取两个集合的并集
    union_lines = sorted(lines1.union(lines2))

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(union_lines)

if __name__ == "__main__":
    file1_path = "file1.txt"  # 第一个文本文件的路径
    file2_path = "file2.txt"  # 第二个文本文件的路径
    output_path = "output_union.txt"  # 输出并集的文本文件路径

    union_of_lines(file1_path, file2_path, output_path)
