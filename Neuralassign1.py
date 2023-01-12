#!/usr/bin/env python
# coding: utf-8

# In[1]:


(/Question, 1)
input_str=input()//Taking input from the user.
if(len(input_str))>=2:
    input_str=input_str[2:]//Deleting two elements using slicing.
input_str=input_str[::-1]//Reversing the string.
print(input_str)//Printing the new output.


# In[4]:


(/Question, 1)
num1=int(input())//taking input from user as integer
num2=int(input())
print("Addition of two numbers",(num1+num2));
print("substract of two numbers",(num1-num2));
print("Multiplicationof two numbers",(num1*num2));
print("Division of two numbers",(num1//num2));
print("Percentileof two numbers",(num1%num2));


# In[7]:



input_str=input()
input_str=input_str.replace("python","pythons")//using replace() to replace the particular string.
print(input_str)
        


# In[8]:


score=int(input("Enter your score to get grade out of 100"))
if score>=90 and score<=100:
    print("Your Grade is A")
elif score>=80 and score<=89:
     print("Your Grade is B")
elif score>=70 and score<=79:
     print("Your Grade is C")
elif score>=60 and score<=69:
     print("Your Grade is D")
else:
     print("Your Grade is F")


# In[ ]:




