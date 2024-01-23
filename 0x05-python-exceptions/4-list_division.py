#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x_list = []
    for n in range(0, list_length):
        try:
            ans = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            x_list.append(ans)
    return x_list
