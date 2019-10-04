def selection():
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
    A=[]

    for i in range(100):
        xs.append(i)
        A.append(random.randint(1,101))


    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j    
        A[i], A[min_idx] = A[min_idx], A[i] 
                
        ax.clear()
        ax.bar(xs,A)
        fig.canvas.draw()
       # time.sleep(0.01)


    # In[7]:


    plt.close()

