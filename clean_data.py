# -*- coding:utf-8 -*-
import pandas as pd
import jieba
import re
from nltk.corpus import stopwords


class CleanData():

    def csv_to_txt(csv_filename):
        data = pd.read_csv('dataset/neg.csv', encoding='utf-8').get_text()
        data = re.sub(r'[^a-zA-Z0-9]','',data)
        # data = data.drop('blog_id', axis = 1)
        # data = data.drop('nick_name', axis = 1)
        with open('dataset/neg.txt', 'a+', encoding='utf-8') as f:
            for line in data.values:
                line = re.sub(r'[^a-zA-Z0-9]','',line)
                f.write(str(line) + '\n')


    # 停词函数
    def get_custom_stopword(stop_word_file):
        with open(stop_word_file) as f:
            stop_word = f.read()

        stop_word_file = stop_word.split("/n")
        custom_stopword = [i for i in stop_word_file]
        return custom_stopword


    # 读取文件
    def read_txt(filename):
        with open(filename, 'r', encoding='utf-8')as f:
            txt = f.read()
        return txt


    # 写入文件
    def write_data(filename, data):
        with open(filename, 'a', encoding='utf-8')as f:
            f.write(data)


    if __name__ == '__main__':
        csv_file = 'dataset/neg.csv'
        csv_to_txt('csv_file')

        text = read_txt('dataset/neg.txt')
        lists = text.split('\n')
