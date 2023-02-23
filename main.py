# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
def open_or_senior(data):
    output = []
    for i in data:
        if i[0] > 54 and i[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output


#递归

def func(n):
    if n==1 or n==2:
        return 1
    return func(n-1)+func(n-2)



#You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
# single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)
#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)
#solution1
def find_outlier(integers):
    odd=[]
    even=[]
    for num in integers:
        if num%2==0:
            odd.append(num)
        else:
            even.append(num)
    fn=lambda odd,even:odd if len(odd)<len(even) else even
    return fn(odd,even)[0]
#solution2
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
#solution3
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative
# persistence, which is the number of times you must multiply the digits in num until you reach a single
# digit.
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)





#Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language) like so:
# (index1, index2).two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
def two_sum(numbers, target):

    sum = np.empty((2,2))

    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                sum=[[i,j],[j,i]]
    return sum

#sulution2
def two_sum(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return[i,j]


#Well met with Fibonacci bigger brother, AKA Tribonacci.
#As the name may already reveal, it works basically like a Fibonacci,
# but summing the last 3 (instead of 2) numbers of the sequence to generate
# the next. And, worse part of it, regrettably I won't get to hear non-native
#test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
#test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
def tribonacci(signature, n):
    if n<=3 and n>0:
        signature=signature[0:n]
    elif n==0:
        signature=[]
    else :
        for i in range(3,n):
           signature.append(signature[i-1]+signature[i-2]+signature[i-3])
    return signature
#other solution
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
