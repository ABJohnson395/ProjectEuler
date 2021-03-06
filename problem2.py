# @author: Andrew Johnson
# 
# Problem: Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

num1 = 0
num2 = 1
sum = 0
total = 0

while ( total < 4000000 ):
  sum = num1 + num2
  num1 = num2
  num2 = sum

  if ( sum % 2 == 0 ):
    total += sum

print( "%d" %total )
