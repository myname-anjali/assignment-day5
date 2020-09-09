#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def prime(num):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print (num,"is not prime")
                break
            else:
                print(num,"is prime")
            else:
            print(not valid option)


# In[ ]:


lst=list(range(1,2500))
lst_prime_no=filter(prime,lst)
print(list(lst_prime_no))


# In[ ]:



  

