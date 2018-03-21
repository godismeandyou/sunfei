# -*- coding: utf-8 -*-
import csv

categoryList = ['动作', '喜剧', '爱情']
locationList = ['大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国',
                 '德国', '意大利', '西班牙', '印度', '泰国', '俄罗斯', '伊朗',
                 '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦']
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



