# -*- coding: utf-8 -*-

import random
import time

s = int(random.uniform(1, 10))
try:
    m = int(input('请输入整数：'))
    if m is not None:
        while s != m:
            if m > s:
                print '大了，二货'
                m = int(input('请再次输入：'))
            if m < s:
                print '小了，二货'
                m = int(input('请再次输入：'))
            if m == s:
                print 'ok，你蒙对了！'
                break
    else:
        print '你输入错误！'

except SyntaxError:
    print '系统错误；'

else:
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
