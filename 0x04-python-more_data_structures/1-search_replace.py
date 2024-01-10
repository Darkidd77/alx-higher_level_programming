#!/usr/bin/python3

def search_replace(my_list, search, replace):
    x_list = my_list.copy()
    x_list = list(map(lambda x: replace if x == search else x, my_list))
    return x_list
