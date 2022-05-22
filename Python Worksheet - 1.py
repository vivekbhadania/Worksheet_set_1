#!/usr/bin/env python
# coding: utf-8

# In[9]:


#11. Write a python program to find the factorial of a number.

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)
    
num = 10
print ("factorial of",num, "is",factorial(num))
    


# In[2]:


#12. Write a python program to find whether a number is prime or composite.

n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is not prime but composite number")
            break
    else:
        print(n,"number is prime but not composite number")
else :
    print("Please enter positive number only ")


# In[5]:


# 13. Write a python program to check whether a given string is palindrome or not.

my_str = '131'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[9]:


#15. Write a python program to print the frequency of each of the characters present in a given string.

test_str = "vivek"
  
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print ("Count of all characteris :\n "+  str(all_freq))

