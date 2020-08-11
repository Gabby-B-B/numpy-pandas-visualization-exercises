#!/usr/bin/env python
# coding: utf-8

# In[365]:


import numpy as np


# In[335]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[336]:


## How many negative numbers are there?
# First I want to see which numbers are negative
negative_elements = a < 0
negative_elements
# Now I am counting each negative number
sum_negative_elements= np.count_nonzero(a < 0)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are", sum_negative_elements, "negative numbers in this numpy array.")


# In[337]:


## How many positive numbers are there?
#First I want to see which numbers are positive.
positive_elements = a > 0
positive_elements
#Now I am counting each positive number
sum_positive_elements= np.count_nonzero(a > 0)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are", sum_positive_elements, "positive numbers in this numpy array.")


# In[338]:


##How many even positive numbers are there?
#First I want to isolate my even numbers and my positive numbers
even = a % 2 == 0
positive= a > 0
#Now I want to count values that are both even and positive
sum_positive_evens= np.count_nonzero(positive & even)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are", sum_positive_evens, "positive even numbers in this numpy array.")


# In[339]:


## If you were to add 3 to each data point, how many positive numbers would there be?
#First, I want to add 3 to each data point
d= a+3
# If I was presenting the outcome to the user, I would want to show them that the list has been properly added.
print("The new array with 3 added to each value is:", d)
sum_pos_plus_three= np.count_nonzero( d > 0)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are",sum_pos_plus_three, "positive numbers in this new numpy array.")


# In[340]:


## If you squared each number, what would the new mean and standard deviation be?
# First I would want to square each number in the array.
b=np.square(a)
# If I was presenting the outcome to the user, I would want to show them that the list has been properly squared.
print("The new array with each value squared is:", b)


#Now I would want to calculate the new standard deviation.
stddev= b.std()
# If I was presenting the outcome to the user, this is what I would want to print.
print("The new standard deviation of the array is", stddev)


#Finally, I would calculate the new mean of the array.
mean= b.sum() / 12
# If I was presenting the outcome to the user, this is what I would want to print.
print("The new mean of the array is", mean)


# In[341]:


## A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
#First I want to calculate the mean of the original array.
mean = a.sum() / 12
# If I was presenting the outcome to the user, I would want to show them the mean I calculated.
print("The mean of the original array is", int(mean), ".")
## Now I want to set up my equation to center the array
d= a - int(mean)
# If I was presenting the outcome to the user, this is what I would want to print.
print("The centered array is", d)


# In[342]:


## Calculate the z-score for each data point. Recall that the z-score is given by
#First I am going to calculate the standard deviation of the array
stddev= a.std()
# If I was presenting the outcome to the user, this is what I would want to print to show that I calculated the standard deviation properly.
print("The standard deviation of the array is", stddev)
#Because I am tired, I am going to just reuse the mean from the last problem in my z score function.
z_score= a-mean/ stddev
# If I was presenting the outcome to the user, this is what I would want to print.
print("The z score for each value in the array is", z_score)


# <font face = "chalkduster" size = "48"><p style= "color: hotpink"> Numpy Exercises Part I</font> </p>

# In[343]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ab= np.array(a)


# <font face = "chalkduster" size = "32"> <p style= "color: hotpink"> Set up 1 </font> </p>
# <ul> <li><p style= "color: purple"> Use python's built in functionality/operators to determine the following: </p></li></ul>

# In[344]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a= ab.sum()
print("The sum of the array above is", sum_of_a, ".")
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a= ab.min()
print("The minimum of all the numbers is", min_of_a, ".")
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a= ab.max()
print("The maximum of all the numbers is", max_of_a, ".")
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a= sum_of_a / 10
print("The average of all the numbers is", mean_of_a, ".")
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a= np.prod(ab)
print("The product of all numbers in a list are", product_of_a, ".")
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a= np.square(ab)
print("Each value in the list squared are", squares_of_a)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a= ab[ab % 2 ==1]
print("The odds in the list are", odds_in_a)
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a= ab[ab % 2 ==0]
print("The evens in the list are", evens_in_a)


# <font face = "chalkduster" size = "32"> <p style= "color: hotpink">Setup 2: </font> </p>
# 
# <ul>
# <li><p style= "color: purple"> What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...</p> </li>
# <li><p style= "color: purple">  Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists. </p> </li> </ul> 

# In[345]:


b = [
    [3, 4, 5],
    [6, 7, 8]
]
b= np.array(b)


# <p style= "color: hotpink"> <font face = "chalkduster">Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array** </font></p>
# 
# <p style="color:purple"> sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row) </p>

# In[346]:


sum_of_b= np.sum(b)
print("The sum of b variable is",sum_of_b,".")


# <p style= "color: hotpink"> <font face = "chalkduster"> Exercise 2 - refactor the following to use numpy. </font>
# <p style="color:purple"> min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) </p>

# In[347]:


min_of_b= np.min(b)
print("The minimum value of b variable is",min_of_b,".")


# <p style= "color: hotpink"> <font face = "chalkduster"> Exercise 3 - refactor the following maximum calculation to find the answer with numpy. </font> 
# <p style="color:purple"> max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1]) </p>

# In[348]:


max_of_b= np.max(b)
print("The maximum value of b variable is",max_of_b,".")


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 4 - refactor the following using numpy to find the mean of b </font>
# 
# <p style= "color: purple"> mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1])) </p>

# In[349]:


mean_of_b= np.sum(b)/6
print("The average of b variable is",mean_of_b,".")


# <p style= "color: hotpink"><font face = "chalkduster">Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1 </font>
# <p style="color:purple"> for row in b:
#     for number in row:
#         product_of_b *= number </p>

# In[350]:


product_of_b= np.product(b)
print("The product of each number in the b variable is", product_of_b)


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 6 - refactor the following to use numpy to find the list of squares </font>
# <p style= "color:purple"> 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2) </p>
# 

# In[351]:


squares_of_b= np.square(b)
print("Each number squared in the b variable is", squares_of_b)


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 7 - refactor using numpy to determine the odds_in_b </font>
# <p style= "color: purple"> odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number) </p>

# In[352]:


odds_in_b=b[b % 2 ==1]
print("The odds in the list are", odds_in_a)


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 8 - refactor the following to use numpy to filter only the even numbers </font>
# <p style= "color: purple">
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number) </p>

# In[353]:


evens_in_b=b[b % 2 ==0]
print("The evens in the list are", evens_in_b)


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 9 - print out the shape of the array b. </font>

# In[354]:


b.shape
print("The shape of the array b is",b.shape)


# <p style= "color: hotpink"> <font face = "chalkduster"> Exercise 10 - transpose the array b. </font>

# In[355]:


np.transpose(b)
print("The array transposed is", np.transpose(b))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6) </font>

# In[356]:


np.concatenate((b))
print("The concatenated list is",np.concatenate(b))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1) </font>

# In[357]:


np_array=np.asarray(b)
reshaped_array = np_array.reshape(1, 6).T 
print("The reshaped array is",reshaped_array)


# <font face = "chalkduster" size = "32"> <p style= "color: hotpink">Setup 3: </font> </p>

# In[358]:


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c= np.array(c)


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 1 - Find the min, max, sum, and product of c. </font>        

# In[359]:


np.min(c)
print("The minimum number in the array is", np.min(c))
np.max(c)
print("The maximum number in the array is", np.max(c))
np.sum(c)
print("The sum of the array is", np.sum(c))
np.product(c)
print("The product of the array is", np.product(c))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 2 - Determine the standard deviation of c. </font>

# In[360]:


np.std(c)
print("The standard deviation of the array is", np.std(c))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 3 - Determine the variance of c. </font>

# In[361]:


np.var(b)
print("The variance of c is", np.var(b))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 4 - Print out the shape of the array c </font>

# In[362]:


np.shape(c)
print("The shape of the c array is", np.shape(c))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 5 - Transpose c and print out transposed result. </font>

# In[363]:


np.transpose(c)
print("The array transposed is", np.transpose(c))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 6 - Get the dot product of the array c with c. </font>

# In[367]:


np.dot(c, c)
# print("The dot product of the array c with c", np.dot(c))


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261 </font>

# In[ ]:


transposed= np.transpose(c) * c
summed= np.sum(transposed)
print("The sum of c transposed is", summed)


# <p style= "color: hotpink"><font face = "chalkduster"> Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400. </font>

# In[376]:


transposed=np.transpose(c)
total= (c*c.T).prod()
print("The product of c times c transposed is", total)


# <font face = "chalkduster" size = "32"> <p style= "color: hotpink">Setup 4: </font> </p>

# In[380]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d=np.array(d)


# In[381]:


# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
print("The sine of all the numbers is", np.sin(d))
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
print("The cosine of all the numbers is", np.cos(d))
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
print("The tangent of all the numbers is", np.tan(d))
# Exercise 4 - Find all the negative numbers in d
neg_in_d= d[d < 1]
print("The negative numbers in the list are", neg_in_d)
# Exercise 5 - Find all the positive numbers in d
pos_in_d= d[d > 1]
print("The positive numbers in the list are", pos_in_d)
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
print("The unique numbers in the array are", np.unique(d))
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
print("Tne amount of unique numbers in the list are", len(np.unique(d)))
# Exercise 8 - Print out the shape of d.
np.shape(d)
print("The shape of the c array is", np.shape(d))
# Exercise 9 - Transpose and then print out the shape of d.
transpose= np.transpose(d)
np.shape(transpose)
print("The shape of transposed d is", np.shape(transpose))
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)
print("The reshaped array is", d.reshape(9,2))

