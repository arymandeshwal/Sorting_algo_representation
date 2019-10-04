def shell():
    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:


    import time
    import random


    # In[2]:


    import matplotlib.pyplot as plt


    # In[3]:


    #get_ipython().run_line_magic('matplotlib', 'notebook')


    # In[4]:


    plt.rcParams['animation.html'] = 'jshtml'


    # In[5]:


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    fig.show()


    # In[6]:


    xs=[]
    arr=[]

    for i in range(100):
        xs.append(i)
        arr.append(random.randint(1,101))
     
    n = len(arr) 
    gap = n//2
    while gap > 0:   
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap  
            arr[j] = temp 
        gap //= 2
        
        ax.clear()
        ax.bar(xs,arr)
        fig.canvas.draw()
        time.sleep(0.5)
            
            
    #ax.clear()
    #ax.bar(xs,arr)
    #fig.canvas.draw()
    #time.sleep(0.01)


    # In[7]:


    plt.close()

