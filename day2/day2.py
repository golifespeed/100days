#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello!"[1-2])


# In[3]:


print(123-1)


# In[4]:


print(True)


# In[14]:


print(type(True))


# In[19]:


print(int("12")+int("456"))


# In[30]:


print("Characters: " + str(len(input("What is your name?"))))


# In[23]:


print(len("123"))


# In[33]:


print(10/3)
print(type(10/3))
print(10//3)
print(type(10//3))


# In[35]:


print(round(10/3, 2))


# In[39]:


score=100
height=5.7
isWinning=True
print(f"Your height is {height} and your score is {score}. It's {isWinning} that you are winning.")


# In[40]:


val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")


# In[44]:


bill=float(input("Enter the bill amount: "))
to_tip=float(input("Enter the tip percentage: "))
people=int(input("Enter the number of people: "))
split_amt=round((bill*(1+to_tip/100))/people, 2)
print(f"Each person should pay: ${split_amt}")

