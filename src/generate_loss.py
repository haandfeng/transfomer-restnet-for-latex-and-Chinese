import os
from Levenshtein import distance as lev
from nltk.translate.bleu_score import sentence_bleu


def compare_files(folder1, folder2, output_file):
    # 遍历 folder1 中的所有 txt 文件
    count = 0
    all = 0
    d_leven, len_tot = 0, 0
    blue_score = 0.0
    # blue = 0
    seq1 = []
    seq2 = []
    for file_name in os.listdir(folder1):
        all += 1

        if file_name.endswith('.txt'):
            file1_path = os.path.join(folder1, file_name)
            file2_path = os.path.join(folder2, file_name)
            # print(file1_pathpath,file2_path)

        # 检查 folder2 中是否存在相同名称的文件
        if os.path.exists(file2_path):
            # print(file2_path)
            with open(file1_path, 'r', encoding='UTF-8') as file1, open(file2_path, 'r', encoding='UTF-8') as file2:
                # print(content1)
                content1 = file1.read().replace(' ', '')

                content2 = file2.read().replace(' ', '')
                # 计算 edit distance
                seq1.append(content1)
                seq2.append(content2)
                for ref, hypo in zip(content1, content2):
                    d_leven += int(lev(ref, hypo))
                    len_tot += float(max(len(ref), len(hypo)))
               


    for ref, hypo in zip(seq1, seq2):
        blue_score += max(0.01, sentence_bleu([ref], hypo))
    blue_score = blue_score / len(seq1) * 100
    a = (all - count) / all * 100
    b = ((1. - d_leven / len_tot) * 100)
    c = blue_score
    print((all - count) / all)
    print((1. - d_leven / len_tot) * 100)
    print(blue_score)

    print((a + b + c) / 3)


# 调用函数
# 请替换 'folder1_path' 和 'folder2_path' 为您的实际文件夹路径
# 以及 'output.txt' 为您想要保存结果的文件路径
folder1_path = 'test/prediction'
folder2_path = 'datasets2/'
output_txt = 'path_to_output.txt'
compare_files(folder1_path, folder2_path, output_txt)

