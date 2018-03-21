# -*- coding: utf-8 -*-
# from expanddouban import getHtml
#
# aa = getHtml('https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影','true')
# print aa

def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
    return url

a = getMovieUrl('孙飞','孙飞1')
print a