#
# Python Ver:       3.10.7
#
# Author:           Bryan
#
# Purpose:          Abstraction assignment.
#                   
# Tested OS:        This code was written and tested to work with Windows 11.

from abc import ABC, abstractmehod
class apex(ABC):
    def buyCoins(self, amount):
        print("The apex coins cost: ",amount)
# This function is telling us to pass in an argument, but we won't tellyou how or what kind
# of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(apex):
# here we have defined how to implement the payment function from its parent buyCoins class.
    def payment(self, amount):
        print('The amount owed of {} exceeds your limit.'.format(amount))

obj = DebitCardPayment()
obj.buyCoins("$99")
obj.payment("$99")
