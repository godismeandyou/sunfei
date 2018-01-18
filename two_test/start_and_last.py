# -*- coding: utf-8 -*-

def first_and_last(sequence):
    """返回序列的第一个和最后一个元素。"""
    return sequence[0], sequence[-1]

a = ["Spam", "egg", "sausage", "Spam-1"]
start,end = first_and_last(a)
print (start,end)