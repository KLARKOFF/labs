#1

from math import sqrt
a=int(input())
print("Квадрат этого числа:", sqrt(a), '\t')
import datetime
date=datetime.date.today()
print(date.strftime("%A %d.%m.%y"), '\t')
#2

import my_module as mo
print(mo.uno, mo.average(43, 7, 8, 55, 6, 45, 3, 3, 645, 7656), '\t')

#3

from mypackage import *
module1.fanta()
module1.pepsi()

print(module2.CircleArea(45))
