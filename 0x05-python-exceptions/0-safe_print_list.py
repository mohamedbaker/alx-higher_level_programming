#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    indx = 0
    try:
        while (indx < x):
            print(my_list[indx], end='')
            indx += 1
    except Exception:
        None
    print()
    return indx
