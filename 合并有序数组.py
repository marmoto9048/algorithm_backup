#!/usr/bin/env python
# coding: utf-8

# In[23]:


list1 = [1,3,4,6,7,78,97,190]
list2 = [2,5,6,8,10,12,14,16,18]
i = j = 0
res = []
while len(list1)>=i+1 and len(list2)>=j+1:
    if list1[i]<=list2[j]:
        res.append(list1[i])
        i +=1
        print('这里添加了list1',list1[i],i)
    else:
        res.append(list2[j])
        print('这里添加了list2',list2[j],j)
        j+=1
while len(list1)>i:
    res.append(list1[i])
    print('这里添加了list11',list1[i],i)
    i+=1
while len(list2)>j:
    res.append(list2[j])
    print('这里添加了list22',list2[j],j)
    j+=1
    
print(res)

