#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

num1, num2 = swap_numbers(num1, num2)

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

