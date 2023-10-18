#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# Sample data
genders = ['Male', 'Female', 'Non-Binary', 'Other']
count = [150, 120, 20, 10]  # Replace with your actual data

# Create a bar chart
plt.bar(genders, count, color=['blue', 'pink', 'purple', 'gray'])

# Add labels and title
plt.xlabel('Genders')
plt.ylabel('Count')
plt.title('Distribution of Genders in a Population')

# Show the plot
plt.show()


# In[2]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.random.normal(loc=30, scale=10, size=1000)  # Replace with your actual data

# Create a histogram
plt.hist(ages, bins=30, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in a Population')

# Show the plot
plt.show()


# In[ ]:




