#!/usr/bin/python3
''' module for sort and print'''


class MyList(list):
    ''' class list that inherts list '''
    def print_sorted(self):
        ''' methode for printing sorted list '''
        print(sorted(self))
