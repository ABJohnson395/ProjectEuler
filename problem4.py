# @author: Andrew Johnson
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []
for i in range(100, 999):
    for j in range(100, 999):
        num = str(j * i).split()[0]
        if (len(num) == 6):
            if (num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]):
                palindromes.append(j * i)

print(max(palindromes))
