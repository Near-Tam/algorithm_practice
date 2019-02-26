#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
# File Name: sort.py
# Author: Neablister
# Mail: 943272448@qq.com
# Created Time: 2019-02-10 14:37:19
############################

def bubble_sort(array):
    """
    冒泡排序-bubble_sort
    """
    num = len(array)
    for i in range(num - 1):
        for j in range(num - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def insert_sort(array):
    """
    插入排序-insert_sort
    """
    print("############### DEBUG ###############")
    num = len(array)
    for i in range(1, num):
        j = i - 1
        if array[i] < array[j]:
            tmp = array[i]
            array[i] = array[j]
            while j > 0 and array[j - 1] > tmp:
                array[j] = array[j - 1]
                j -= 1
            array[j] = tmp
        print(array)
    print("############### DEBUG ###############") 
    return array

if __name__ == "__main__":
    array = [64, 231, 56, 32, 76, 23]
    # print(bubble_sort(array))
    print(insert_sort(array))
