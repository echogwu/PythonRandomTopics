#!/usr/bin/python
#Problem:
#Implement a routing that prints all possible orderings of the characters in a string. In other words, print all permutations that use all the characters from the original string.
#For example, given the string "hat", your function should print the strings "tha", "aht", "tah", ath", "hta", and "hat". Treat each chatacter in the input string as a distinct character,
#even if it is repeated.  Given the string "aaa", you routine should print "aaa" six times. You may print the permutations in any order you choose.

class Permutation:
    word = ""
    word_len = 0
    used = []
    word_out = ""

    def __init__(self, word_in):
        self.word = word_in
        self.word_len = len(self.word)
        self.used = [False] * self.word_len
        self.word_out = ""

    def permute(self):
        if len(self.word_out) == self.word_len:
            print self.word_out
            return
        for i in range(0, self.word_len):
            if self.used[i]:
                continue
            self.word_out += self.word[i]
            self.used[i] = True
            self.permute()
            self.used[i] = False
            self.word_out = self.word_out[:len(self.word_out)-1]

permutation = Permutation("abc")
permutation.permute()

