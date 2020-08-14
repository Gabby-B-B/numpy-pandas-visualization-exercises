#!/usr/bin/env python
# coding: utf-8

# In[218]:


from pydataset import data
import pandas as pd
import numpy as np


# <font face = "signpainter" size = "32"> <p style= "color: cadetblue"> 1. Copy the code from the lesson to create a dataframe full of student grades: </font> </p>

# In[219]:


np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)


# <ul>
# <size= 14><li><p style= "color: cadetblue">Create a column named passing_english that indicates whether each student has  a passing grade in english. </p></li> </ul>

# In[220]:


df['passing_english'] = df.english > 70
df


# <ul><font face = "sign painter"><li><p style= "color: cadetblue">Sort the english grades by the passing_english column. How are duplicates handled?</p></li></ul>

# In[221]:


df.sort_values(by='passing_english') 
#The automatic sorting style has the nonpassing students at the top and the order is by the number they are assigned (6,7,8 etc)


# <ul>
# <li><p style= "color: cadetblue">Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method) </p></li>
# </ul>

# In[222]:


df.sort_values(by=['passing_english', 'name'])


# <ul>
#     <font face = "sign painter"><li><p style= "color: cadetblue">Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.</p></li>
#         </ul>

# In[223]:


df.sort_values(by=['passing_english', 'english'])


# <ul>
# <font face = "sign painter"><li><p style= "color: cadetblue">Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades. </p></li>
#     </ul>

# In[224]:


df['overall_grade'] =(df.math+df.english+df.reading)/3
df


# <p style= "color: plum"> <font face = "signpainter" size = "32"> 
# 2. Load the mpg dataset. <br><br>
#  Read the documentation for the dataset and use it for the following questions: </p></font>

# <ul>
#     <b>
# <li> <p style= "color: plum">  How many rows and columns are there? </li> </p>
# </ul>
# </p></b>

# In[225]:


#First I need to import my MPG dataframe.
mpg = data('mpg')
mpg
#There are 234 rows and 11 columns in the MPG dataframe


# <ul><li><b><p style= "color: plum"> What are the data types of each column? </li></p></b></ul>

# In[226]:


mpg.info()
#The datatypes for each column are object, float, and int


# <ul>
#     <b><li><p style= "color: plum"> Summarize the dataframe with .info and .describe </li></p>
#     </ul>

# In[227]:


print("The information about MPG is:")
mpg.info()


# In[228]:


print("The description of MPG is:")
mpg.describe()


# <ul>
# <b><li><p style= "color: plum">Rename the cty column to city. </li></p>
# </ul></b>

# In[229]:


mpg.rename(columns={'cty': 'city'})


# <ul><b> <li><p style= "color: plum"> Rename the hwy column to highway. </li></p> <b> </u;>

# In[230]:


mpg.rename(columns={'hwy': 'highway'})


# <ul><b><li><p style= "color: plum"> Do any cars have better city mileage than highway mileage? </li> </p></b></ul>

# In[231]:


mpg[mpg.cty > mpg.hwy].sort_values(by='cty')
mpg
#There are no cars with better city mileage than highway mileage


# <ul><b>
#     <li><p style= "color: plum"> Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.</li></p>
#     </ul></b>

# In[232]:


mpg['mileage_difference']= (mpg.hwy-mpg.cty)
mpg


# <ul><b>
# <li><p style= "color: plum">Which car (or cars) has the highest mileage difference?</li></p>
#     </ul></b>

# In[233]:


mpg.sort_values(by='mileage_difference', ascending=False)


# <ul><b>
# <li><p style= "color: plum">Which compact class car has the lowest highway mileage? The best?</li></p>
#     </ul></b>

# In[234]:


mpg.loc[mpg['class'] == 'compact']
mpg.sort_values(by=['hwy']).head(5)


# In[235]:


mpg.loc[mpg['class'] == 'compact']
mpg.sort_values(by=['hwy']).tail(2)


# <ul><b>
# <li><p style= "color: plum">Create a column named average_mileage that is the mean of the city and highway mileage.</li></p></ul></b>

# In[236]:


mpg['average_mileage']= (mpg.hwy+mpg.cty)/2
mpg


# <ul><li><b><p style= "color: plum"> Which dodge car has the best average mileage? The worst?</li></p></ul>

# In[237]:


mpg.loc[mpg['manufacturer'] == 'dodge'].sort_values(by=['average_mileage']).head(4)


# In[238]:


mpg.loc[mpg['manufacturer'] == 'dodge'].sort_values(by=['average_mileage']).tail(1)


# <p style= "color: palevioletred"> <font face = "signpainter" size = "32"> 
# 3. Load the Mammals dataset. <br><br>Read the documentation for it, and use the data to answer these questions: 
# </p></font>

# <ul><li><b><p style= "color: palevioletred">How many rows and columns are there?</ul></li></b>
# <ul><li><b><p style= "color: palevioletred">What are the data types?</ul></li></b>

# In[239]:


mammals=data('Mammals')
mammals


# <ul><li><b><p style= "color: palevioletred">Summarize the dataframe with .info and .describe</b></ul></li>

# In[240]:


mammals.info()
#There are 4 columns and 107 rows
#The data types are bools and floats


# In[241]:


mammals.describe()


# <ul><li><b><p style= "color: palevioletred">What is the the weight of the fastest animal?</ul></li></b>

# In[242]:


mammals.sort_values('speed', ascending=False).head(1)


# <ul><li><b><p style= "color: palevioletred">What is the overall percentage of specials?</ul></li></b>

# In[243]:


mammals['specials'].value_counts()
percent= (10/97)
percent= percent * 100
percent= round(percent, 2)
print(percent,"% are specials")


# In[244]:


mean_speed= 46.208411
means= mammals['greater_than_av']= mammals.speed > mean_speed
mammals


# <ul><li><b><p style= "color: palevioletred">How many animals are hoppers that are above the median speed? What percentage is this?</ul></li></b>

# In[245]:


hoopers= mammals.loc[mammals['hoppers'] == True].sort_values(by=['speed'])
hoopers


# In[246]:


mammals.loc[mammals['hoppers'] == True].sort_values(by=['greater_than_av'])
#There are 4 animals slower than the median speed and there are 7 faster than the median speed


# In[247]:


median_speed_overall= (7/11) *100
median_speed_overall= round(median_speed_overall, 2)
print("The overall percentage faster than the median speed are", median_speed_overall, "%")

