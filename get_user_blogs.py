import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import random
import time
import csv
import pandas as pd

# from datamanage import DataManager

# 实例化数据库对象
# db = DataManager()

# 判空
def getDataFormList(temp_list):
    if len(temp_list) > 0:
        return temp_list[0].strip()
    else:
        return ''

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2112738497?uid=2112738497',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Xsrf-Token': 'a56994',
}

max_page = 10

def get_page(page):
    params = {
        # 'type': 'uid',
        # 'value': '2771423767',
        'containerid': '1076032112738497',
        # 'page_type': 'searchall',
        'uid': '2112738497',
        'page': page
    }
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            # response = response.text
            # print(type(response))  # tuple
            return response.json(), page
        else:
            print("请求失败了。")
    except requests.ConnectionError as e:
        print('Error:数据转换失败', e.args)

def save_to_csv(resource_data):
    file_name = 'dataset/blogs.csv'
    # print(type(resource_data))    # tuple
    resource_data = list(resource_data)
    # print(type(resource_data))    # list
    save = pd.DataFrame([resource_data], columns=['blog_id','creator_id','creator_nickname', 'blog_content', 'thumbnail_pic','collection_count', 'comment_count', 'repost_count', 'create_time'])
    try:
        save.to_csv(file_name, mode='a')
        print("写入成功")
    except UnicodeEncodeError:
        print("编码错误，数据转换失败，无法写入。")

def parse_page(json, page: int):
    # print(json)
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                if item.get('mblog'):
                    item = item.get('mblog',{})
                else:
                    continue

                user_item = item.get('user', {})
                blog = {}

                blog['blog_id'] = item.get('id')
                blog_id = blog['blog_id']

                blog['creator_id'] = user_item.get('id')
                creator_id = str(blog['creator_id'])

                blog['creator_nickname'] = user_item.get('screen_name')
                creator_nickname = user_item['screen_name']

                blog['blog_content'] = pq(item.get('text')).text()
                if blog['blog_content'] != '':
                    blog_content = item['text']
                else:
                    blog_content = "纯图片"

                blog['thumbnail_pic'] = str(item.get('thumbnail_pic'))
                if blog['thumbnail_pic'] != '':
                    thumbnail_pic = blog['thumbnail_pic']
                else:
                    thumbnail_pic = "纯文本"

                blog['collection_count'] = item.get('attitudes_count')
                collection_count = item['attitudes_count']

                blog['comment_count'] = item.get('comments_count')
                comment_count = item['comments_count']

                blog['repost_count'] = item.get('reposts_count')
                repost_count = item['reposts_count']

                blog['create_time'] = item.get('created_at')
                create_time = item['created_at']
                yield blog

            # # 数据存储到mysql
            data = (blog['blog_id'],str(blog['creator_id']),blog['creator_nickname'], blog['blog_content'], blog['thumbnail_pic'],str(blog['collection_count']), str(blog['comment_count']), str(blog['repost_count']), blog['create_time'])   # 是个元组
            # # print(data)
            # try:
            #     # 插入数据，如果已存在就不再重复插入
            #     res = db.save_data(data)
            # except Exception as e:
            #     print('插入数据失败', str(e)) # 打印插入失败的报错语句

            # 存储到csv
            save_to_csv(data)


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        print(type(json)) # tuple
        print(*json)
        results = parse_page(*json)
        for result in results:
            print(result)
            time.sleep(random.uniform(1,7))
