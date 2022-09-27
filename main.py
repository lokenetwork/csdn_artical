#!/usr/bin/env python
# coding:utf-8
"""
Name : CSDN_actical.py
Author  : SongJian
Contect : songjianhitsz@qq.com
Time    : 2022/3/19 11:56
Desc    : 针对特定的文章刷阅读量
"""
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


class CsdnVisitor(object):
    def __init__(self, home_url, page_num):
        self.headers = {'User-Agent': ''}
        self.url = home_url
        self.page_url = []
        self.page_num = page_num  # 用于记录博客最大页数
        self.article_list = []  # 用于保存所有的文章链接
        self.ua = UserAgent()   # 代理实例
        self.visitor_count = 1  # 记录已访问次数


    def visitor(self):
        self.headers = {'User-Agent': self.ua.chrome}

        # 文章链接
        self.article_list.append('https://blog.csdn.net/u012117034/article/details/127080544')

        for article_url in self.article_list:
            response = requests.get(url=article_url, headers=self.headers)

    def run(self):
        while self.visitor_count < 3000:
            print("\r已访问次数：%s" % self.visitor_count, end='')
            self.visitor()
            self.visitor_count += 1
            time.sleep(60)


def main():
    url = "https://blog.csdn.net/u012117034"  # 用于保存你的博客主页地址（根据实际情况更改）
    page_num = 1  # 用于保存你的博客页数 （根据实际情况更改）
    visitor = CsdnVisitor(url, page_num)
    visitor.run()


if __name__ == '__main__':
    main()
