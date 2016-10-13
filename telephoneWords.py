#!/usr/bin/python
#problem:
#People in the United States often give others their telephone number as a word representing the seven-digit number after the area code. For example, if my telephone number were 866-2665,
#I could tell people my number is "TOOCOOL", instead of the hard-to-remember seven-digit number. Note that many other possibilities(most of which are nonsensical) can represent 866-2665.
#You can see how letters correspond to numbers on a telephone keypad in Figure 7-2.
#                 ABC       DEF
#         1        2         3
#
#        GHI      JKL       MNO
#         4        5         6
#
#        PRS      TUV       WXY
#         7        8         9
#
#         *        0         #
#
#Write a function that takes a seven-digit telephone number and prints out all of the possible "words" or combinations of letters that can represent the given number. Because the 0 and 1
#keys have no letters on them, you should change only the digits 2-9 to letters. You'll be passed an array of seven integers, with each element being one digit in the number. You may
#assume that only valid phone numbers will be passed to your function. You can use the helper function:
#       char getCharKey(int telephoneKey, int place)
#which takes a telephone key(0-9) and a place of either 1, 2, 3 and returns the character corresponding to the letter in that position on the specified key. For example, GetCharKey(3, 2)
#will return "E" because the telephone key 3 has the letters "DEF" on it and "E" is the second letter.

class telephoneRep:
    telenumber = ""
    rep = ""
    TELEPHONE_NUMBER_LENGTH = 7
    count = 0

    def __init__(self, number):
        self.telenumber = number

    def getCharKey(self, telephoneKey, place):
        '''
        telephoneKey: any character within 1234567890
        place: either one of 1, 2, 3
        '''
        keypad = {"1":"111", "2":"ABC", "3":"DEF", "4":"GHI", "5":"JKL", "6":"MNO", "7":"PRS", "8":"TUV", "9":"WXY", "0":"000"}
        return keypad[telephoneKey][place]

    def teleTranslate(self):
        '''
        number is a string of the 7-digit phone number
        '''
        if len(self.telenumber) != self.TELEPHONE_NUMBER_LENGTH:
            print("phone number should be 7-digit")
            sys.exit(1)
        self.wordTran(0)

    def wordTran(self, start):
        for i in range(3):
            self.rep += self.getCharKey(self.telenumber[start], i)
            if len(self.rep) == self.TELEPHONE_NUMBER_LENGTH:
                print self.rep
                self.count += 1
            if start < len(self.telenumber) - 1:
                self.wordTran(start+1)
            self.rep = self.rep[:len(self.rep)-1]
            if self.telenumber[start] == "0" or self.telenumber[start] == "1":
                break


teleRep = telephoneRep("6760391")
teleRep.teleTranslate()
print("count = %s" % teleRep.count)
