#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selection_sort
import bubble_sort
import insertion_sort
import shell_sort
print("Welcome to the program choose any one!")


# In[ ]:


while True:
    ch=int(input('Enter:\n[1] for Selection Sort\n[2] for Bubble Sort\n[3] for Insertion Sort\n[4] for Shell Sort\n'))
    if ch == 1:
        selection_sort.selection()
    elif ch == 2:
        bubble_sort.bubble()
    elif ch == 3:
        insertion_sort.insertion()
    elif ch == 4:
        shell_sort.shell()
    else:
        print('Wrong Input!')
        
    t = input('Do you wanna try again ?[y/n]\t')
    if t == 'n' or t== 'N':
        print('Thank you!')
        break


# In[ ]:




