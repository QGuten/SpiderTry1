#coding:UTF-8


import snownlp as sn
import jieba
import numpy as np
import pandas as pd
import re

def clean_datacsv(data_csvfile,clean_csvfile):
  ''' 清洗csv源文件 '''
  clean_data = pd.read_csv(data_csvfile, header=None, names=['blog_content','blog_id', 'creator_nickname'])
  clean_data = clean_data.drop('blog_id', axis = 1)
  clean_data = clean_data.drop('creator_nickname', axis = 1)
  pattern = '\d+'
  clean_data['blog_content'] = clean_data['blog_content'].str.findall(pattern)
  clean_data.to_csv(clean_csvfile, index=None, mode='w' ,encoding='utf-8')

def csv_to_txt(clean_csvfile, clean_txtfile):
  '''
  csv转txt
  :param clean_csvfile:
  :param clean_txtfile:
  :return:
  '''
  data = pd.read_csv(clean_csvfile, encoding='utf-8')
  with open(clean_txtfile, mode='w', encoding='utf-8') as f:
    for line in data.values:
      print('line:'+ str(line))
      f.write(str(line) + '\n')

def read_txt(filename):
  # 读取文件
    with open(filename, 'r', encoding='utf-8')as f:
        txt = f.read()
    return txt

def write_data(filename, data):
  ''' 写入 '''
  with open(filename, 'a', encoding='utf-8')as f:
    f.write(data)

# def train_model(neg_filepath,pos_filepath, sentiment_marshal):
#   ''' 用自己的语料库训练模型 '''
#   sentiment.train(neg_filepath,pos_filepath)
#   sentiment.save(sentiment_marshal, 'w')

def get_sentiment(text):
  '''分析文本情感值'''
  res = sn.SnowNLP(text)
  return res

if __name__ == '__main__':
  data_csv = 'dataset/data.csv'
  mdd_csv = 'dataset/neg.csv'
  mdd_txt = 'E:\\Graduate\\SpiderTry1\\dataset\\neg.txt'
  pos_file = 'E:\\Graduate\\SpiderTry1\\dataset\\pos.txt'

  clean_datacsv(data_csv, mdd_csv)
  csv_to_txt(mdd_csv, mdd_txt)
  # sentiment_marshal = 'E:\\Graduate\\SpiderTry1\\dataset\\sentiment.marshal'
  from snownlp import sentiment
  # train_model(mdd_txt, pos_file, sentiment_marshal)
  text = '我感觉还好，我只是不想活啦'
  res = get_sentiment(text)
  print(res)