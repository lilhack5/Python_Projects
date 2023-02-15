#
# Python Ver:       3.10.7
#
# Author:           Bryan
#
# Purpose:          Encapsulation assignment.
#                   
# Tested OS:        This code was written and tested to work with Windows 11.


class Apex:
    def __init__(self):
        self.__privateVar = 15

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Apex()
obj.getPrivate()
obj.setPrivate(16)
obj.getPrivate()
