#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    int indx = 0
    try:
        while (indx < x):
            print(my_list[indx], end='')
            ind x += 1
    except Exception:
        break
    print()
    return indx
