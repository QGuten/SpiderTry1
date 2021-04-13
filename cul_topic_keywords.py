import jieba

class CulTopicKeyword():
    def __init__(self):
        cul_topic_

    def cul_topic_keyword(txtfile, stopwords_txt):
        txt = open(txtfile,"r", encoding="utf-8").read()
        words = jieba.lcut(txt)
        stop=[]
        with open(stopwords_txt,"r", encoding="utf-8") as f:
            lines = f.readline()
            for line in lines:
                lline = line.strip()
                stop.append(lline)

        counts = {}
        for word in words:
            if word not in stop:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] = counts[word] + 1

    if __name__ == '__main__':
