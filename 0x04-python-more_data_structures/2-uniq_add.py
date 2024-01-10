#!/usr/bin/python3

def uniq_add(my_list=[]):
    x_list = my_list.copy()
    x_list = sum(set(my_list))
    return x_list
