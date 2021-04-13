import requests
from requests.packages import urllib3
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import random
import time

# from datamanage import DataManager
#
# # 实例化数据库对象
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
    'Referer': 'https://m.weibo.cn/u/5357739241',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

max_page = 68

def get_page(page):
    params = {
        'uid': '5357739241',
        'containerid': '1076035357739241',
        'page': page
    }
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers, verify=False)
        # print(response)
        if response.status_code == 200:
            # response = response.text
            # print(type(response))
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error:数据转换失败', e.args)


def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        user_items = json.get('items').get('')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog', {})


                blog = {}

                blog['blog_id'] = item.get('id')
                blog_id = item['id']

                blog['blog_content'] = pq(item.get('text')).text()
                blog_content = item['text']

                blog['thumbnail_pic'] = item.get('thumbnail_pic')
                thumbnail_pic = item['thumbnail_pic']

                blog['collection_count'] = item.get('attitudes_count')
                collection_count = item['attitudes_count']

                blog['comment_count'] = item.get('comments_count')
                comment_count = item['comments_count']

                blog['repost_count'] = item.get('reposts_count')
                repost_count = item['reposts_count']

                blog['create_time'] = item.get('created_at')
                create_time = item['created_at']

                user_item = item.get('user', {})
                blog['user_id'] = user_item.get('id')
                user_id = user_item['id']

                blog['user_nickname'] = user_item.get('screen_name')
                user_nickname = user_item['screen_name']
                yield blog

                # # 数据存储
                # data = ('blog_id', 'creator_nickname', 'blog_content', 'thumbnail_pic','collection_count', 'comment_count', 'repost_count', 'create_time')
                # db.save_data(data)
        for


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        print(type(json))
        results = parse_page(*json)
        for result in results:
            print(result)
            time.sleep(random.uniform(1,7))
