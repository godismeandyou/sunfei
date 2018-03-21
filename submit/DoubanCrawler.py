# -*- coding: utf-8 -*-
import expanddouban
from bs4 import BeautifulSoup
import csv


# 任务1:获取每个地区、每个类型页面的URL
def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
    return url


# p = getMovieUrl('剧情','美国')
# print p


# 任务3:定义电影类
class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link


# html = expanddouban.getHtml(getMovieUrl('剧情','美国'), True)
# print html


# 任务4:获得豆瓣电影的信息
def getMovies(category, location):
    aa = []
    for aa in category:
        for cc in location:
            url = expanddouban.getHtml(getMovieUrl(aa, cc), True)
            beautiful = BeautifulSoup(url, 'html.parser')
            tag = beautiful.find(class_='list-wp').find_all('a', recursive=False)
            for aTag in tag:
                a1 = aTag.find(class_='title').string
                a2 = aTag.find(class_='rate').string
                a3 = cc
                a4 = aa
                a6 = aTag.get('href')
                a7 = aTag.find('img').get('src')
                aa.append([a1, a2, a3, a4, a6, a7])
    return aa
# ab = getMovies('剧情','美国')
# print ab


# 任务5:构造电影信息数据表
categoryList = ['动作', '喜剧', '爱情']
locationList = ['大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国',
                 '德国', '意大利', '西班牙', '印度', '泰国', '俄罗斯', '伊朗',
                 '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦']

moviesList = getMovies(categoryList, locationList)
with open('movies.csv', 'w') as f:
    writers = csv.writer(f)
    for hang in moviesList:
        writers.writerow(hang)


# 任务6:统计电影数据
with open('movies.csv', 'r') as f:
    reader = csv.reader(f)
    csvNum = list(reader)


for cat in categoryList:
    aa = []
    shuzu = []
    sum = 0
    for loc in locationList:
        count = 0
        for movie in csvNum:
            if movie[3] == cat and movie[2] == loc:
                count += 1
                sum += 1
        aa.append((loc, count))
        aa = sorted(aa, key=lambda x: x[1], reverse=True)


    for i in range(3):
        shuzu.append('%.2f%%' % (float(aa[i][1]) / float(sum) * 100))

    result = (('{}电影数量排名前三的地区是{}、{}、{}，分别占此类别电影总数的百分比为{}、{}、{}。\n').format(cat, aa[0][0], aa[1][0], aa[2][0], shuzu[0], shuzu[1], shuzu[2]))
    with open('output.txt', 'a') as f:
        f.write("\n"+result)
