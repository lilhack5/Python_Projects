#
# Python:   3.10.7
#
# Author:   Bryan
#
# Purpose:  The Tech Academy - Python Course, showing inheritance and attributes

# Made class gamer with name, email
class Gamer:
    name = 'Billy Bob'
    email = 'joe@gmail.com'

# Pick the console system you play with and controller brand style you use.
class Console(Gamer):
    system = 'ps5'
    controller = 'Scuf'

# What mouse do you use and what is you dpi set at for gaming.
class Pc(Gamer):
    mouse = 'Logitech'
    dpi = '3750'
