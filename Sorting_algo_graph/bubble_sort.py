def bubble():
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
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        ax.clear()
        ax.bar(xs,arr)
        fig.canvas.draw()
       # time.sleep(0.01)


    # In[7]:


    plt.close()

