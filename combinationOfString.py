#!/usr/bin/python
#
#problem:
#Implement a function that prints all possible combinations of the characters in a string. These combinations range in length fromone to the length fo the string. Two combinations
#that differ only in ordering of their characters are the same combination. In other words, "12" and "31" are different combinations from the input string "123", but "21" is the same
#as "12"
#

class Combination:
    in_str = ""
    in_len = 0
    out_str = ""

    def __init__(self, in_str):
        self.in_str = in_str
        self.in_len = len(self.in_str)

    def combine(self):
        self.combination(0)

    def combination(self, n):
        for i in range(n, self.in_len-1):
            self.out_str += self.in_str[i]
            print self.out_str
            self.combination(i+1)
            self.out_str = self.out_str[:len(self.out_str)-1]

        self.out_str += self.in_str[len(self.in_str) - 1]
        print self.out_str
        self.out_str = self.out_str[:len(self.out_str)-1]

    '''
    #another way to implement function combination
    def combination(self, n):
        for i in range(n, self.in_len):
            self.out_str += self.in_str[i]
            print self.out_str
            if i < self.in_len:
                self.combination(i + 1)
            self.out_str = self.out_str[:len(self.out_str)-1]
    '''

com = Combination("abc")
com.combine()
