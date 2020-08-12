#!/usr/bin/env python
# coding: utf-8

# ... 
# <font face = "Marker felt" size = "46">
# <p>
# <span style='color: turquoise'>PAN</span>
# <span style='color: BlueViolet'>DAS</span>   
# <span style='color: CornflowerBlue'>Exer</span>
# <span style='color: Coral'>cises</span>
# </p>

# <center><font face = "Marker felt" size = "32"> <p style= "color: turquoise">Part I </font> </p></center>

# In[273]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# <p style= "color: turquoise"> <font face = "marker felt">A. Name the variable that holds the series fruits.
# </font></p>

# In[274]:


fruity= ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits = pd.Series(fruity)


# <p style= "color: turquoise"> <font face = "marker felt">B. Run .describe() on the series to see what describe returns for a series of strings. </p>

# In[275]:


described= fruits.describe()
described


# <p style= "color: turquoise"> <font face = "marker felt">C. Run the code necessary to produce only the unique fruit names. </p>

# In[276]:


uniques=fruits[fruits.unique()]
uniques


# <p style= "color: turquoise"> <font face = "marker felt"> D. Determine how many times each value occurs in the series. </p>

# In[277]:


total_fruit_counts= fruits.value_counts(sort= True)
total_fruit_counts


# <p style= "color: turquoise"> <font face = "marker felt">E. Determine the most frequently occurring fruit name from the series. </p>

# In[278]:


most_common_fruit= fruits.mode()
most_common_fruit


# <p style= "color: turquoise"> <font face = "marker felt"> F. Determine the least frequently occurring fruit name from the series.</p>

# In[279]:


least_common_fruits= fruits.value_counts().nsmallest(keep='all')
least_common_fruits


# <p style= "color: turquoise"> <font face = "marker felt">G. Write the code to get the longest string from the fruits series. </p>

# In[280]:


location_index = fruits.apply(len).idxmax()
fruits[location_index]
#Another way to check is to use this code…checking the length of the strings
#fruits.apply(len).sort_values().tail()


# <p style= "color: turquoise"> <font face = "marker felt">H. Find the fruit(s) with 5 or more letters in the name. </p>

# In[281]:


fruits[fruits.str.len() >= 5]


# <p style= "color: turquoise"> <font face = "marker felt">I. Capitalize all the fruit strings in the series. </p>

# In[282]:


fruits.str.capitalize()


# <p style= "color: turquoise"> <font face = "marker felt">J. Count the letter "a" in all the fruits (use string vectorization) </p>

# In[283]:


fruits_with_a= fruits[fruits.str.count("a")]
fruits_with_a


# <p style= "color: turquoise"> <font face = "marker felt">K. Output the number of vowels in each and every fruit. </p>

# In[284]:


vowel_counts= fruits.str.count('[aeiou]')
vowel_counts


# <p style= "color: turquoise"> <font face = "marker felt">L.Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
# </p>

# In[285]:


fruits[fruits.apply(lambda fruit: fruit.count('o') >=2)]


# <p style= "color: turquoise"> <font face = "marker felt">M.Write the code to get only the fruits containing "berry" in the name
# </p>

# In[286]:


fruits[fruits.str.contains('berry')]


# <p style= "color: turquoise"> <font face = "marker felt">N.Write the code to get only the fruits containing "apple" in the name </p>

# In[287]:


fruits[fruits.str.contains('apple')]


# <p style= "color: turquoise"> <font face = "marker felt">O.Which fruit has the highest amount of vowels? </p>

# In[288]:


max_vowels = fruits[max(fruits.str.count('[aeiou]'))]
max_vowels


# <center><font face = "Marker felt" size = "32"> <p style= "color: BlueViolet">Part II </font> </p></center>

# In[289]:


money = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# <p style= "color: BlueViolet"> <font face = "marker felt"> What is the data type of the series? </p>

# In[290]:


money.describe()


# <p style= "color: BlueViolet"> <font face = "marker felt"> Use series operations to convert the series to a numeric data type. </p>

# In[ ]:


#First I will remove the $
money= money.str.replace("$", "")
#Now I will remove the ,
money= money.str.replace(",","")


# In[309]:


#Finally I will convert object to a string
money = money.astype(float)
money


# <p style= "color: BlueViolet"> <font face = "marker felt">  What is the maximum value? The minimum? </p>

# In[310]:


money.max()


# In[311]:


money.min()


# <p style= "color: BlueViolet"> <font face = "marker felt"> Bin the data into 4 equally sized intervals and show how many values fall into each bin.</p>

# In[320]:


money_bins = pd.cut(money, 4)
money_bins.value_counts()


# <p style= "color: BlueViolet"> <font face = "marker felt"> Plot a histogram of the data. Be sure to include a title and axis labels. </p>

# In[369]:


plt.title("Money Histogram")
plt.xlabel("Money")
plt.ylabel("Count Values")
plt.hist(money, color="cornflowerblue")
plt.show()


# <center><font face = "Marker felt" size = "32"> <p style= "color: CornflowerBlue">Part III </font> </p></center>

# In[291]:


exam_scores= pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])


# <p style= "color: CornflowerBlue"> <font face = "marker felt">What is the minimum exam score? The max, mean, median? </p>

# In[368]:


min_exam=exam_scores.min()
min_exam


# In[340]:


mean= exam_scores.sum()/20
mean


# In[343]:


medians=exam_scores.median()
medians


# <p style= "color: CornflowerBlue"> <font face = "marker felt">Plot a histogram of the scores. </p>

# In[363]:


plt.hist(exam_scores, color="cadetblue")
plt.title("Scores")
plt.xlabel("Scores")
plt.ylabel("Value Counts")
plt.show()


# <p style= "color: CornflowerBlue"> <font face = "marker felt">Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'. </p>

# In[459]:


def get_letter_grade (num):
    if num >= 90:
        return "A"
    elif num >= 80 and num <= 89:
        return "B"
    elif num >= 76 and num <= 79:
        return "C"
    elif num >= 70 and num <=75:
        return "D"
    elif num <= 60:
        return "D"
exam_scores.apply(get_letter_grade).sample(20)


# <p style= "color: CornflowerBlue"> <font face = "marker felt">Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well. </p>

# In[382]:


exam_scores +=4
exam_scores


# <center><font face = "Marker felt" size = "32"> <p style= "color: Coral">Part IV </font> </p></center>

# In[477]:


letters= list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
alphabet = pd.Series(letters)
alphabet.describe()


# <p style= "color: Coral"> <font face = "marker felt"> What is the most frequently occuring letter? Least frequently occuring? </P>

# In[444]:


most_common_letter= alphabet[max(alphabet.value_counts())]
most_common_letter


# In[441]:


least_common_letter= alphabet[min(alphabet.value_counts())]
least_common_letter


# <p style= "color: Coral"> <font face = "marker felt"> How many vowels are in the list? </p>

# In[494]:


def count_vowels(string): 
    vowels = "aeiou"
    final = [each for each in string if each in vowels] 
    return(len(final))
sum(alphabet.apply(count_vowels))


# <p style= "color: Coral"> <font face = "marker felt"> How many consonants are in the list? </p>

# In[493]:


def count_cons(string): 
    cons = "bcdfghjklmnpqrstvwxyz"
    final = [each for each in string if each in cons] 
    return(len(final))
sum(alphabet.apply(count_cons))


# <p style= "color: Coral"> <font face = "marker felt"> Create a series that has all of the same letters, but uppercased </P>

# In[500]:


alph= alphabet.astype('str')
alph= alph.str.upper()
alph


# <p style= "color: Coral"> <font face = "marker felt">
# Create a bar plot of the frequencies of the 6 most frequently occuring letters.
# </p>

# In[506]:


alphabet_count= alphabet.value_counts()
alphabet_count.plot.bar()


# <center><font face = "Marker felt" size = "32"> <p style= "color: OliveDrab">17 list comprehension problems in python </font> </p></center>

# In[510]:


fruits1 = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

fruits_series= pd.Series(fruits1)
numbers_series= pd.Series(numbers1)


# In[294]:


# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...] </p>

# In[513]:


uppercased_fruits= fruits_series.str.upper()
uppercased_fruits


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]</p>

# In[515]:


capitalized_fruits= fruits_series.str.title()
capitalized_fruits


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel. </p>

# In[561]:


fruits_with_more_than_two_vowels= fruits_series[fruits_series.apply(count_vowels) > 2]
fruits_with_more_than_two_vowels


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry'] </p>

# In[560]:


fruits_with_only_two_vowels= fruits_series[fruits_series.apply(count_vowels) == 2]
fruits_with_only_two_vowels


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 5 - make a list that contains each fruit with more than 5 characters </p>

# In[533]:


fruits_more_than= fruits_series[fruits_series.str.len() > 5]
fruits_more_than


# <p style= "color: OliveDrab"> <font face = "marker felt">Exercise 6 - make a list that contains each fruit with exactly 5 characters</p>

# In[531]:


fruits_equal_to = fruits_series[fruits_series.str.len() == 5]
fruits_equal_to


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 7 - Make a list that contains fruits that have less than 5 characters</p>

# In[527]:


fruits_less_than= fruits_series[fruits_series.str.len() < 5]
fruits_less_than


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ] </p>

# In[537]:


fruit_length=fruits_series.str.len()
fruit_length


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a" </p>

# In[538]:


fruits_with_letter_a = fruits_series[fruits_series.apply(lambda fruit: fruit.count('a') >=1)]
fruits_with_letter_a


# <p style= "color: OliveDrab"> <font face = "marker felt"> Exercise 10 - Make a variable named even_numbers that holds only the even numbers  </p>

# In[562]:


even_numbers= numbers_series[numbers_series.apply(lambda num: num % 2 == 0)]
even_numbers


# <p style= "color: OliveDrab"> <font face = "marker felt">
#     Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers </p>

# In[563]:


odd_numbers= numbers_series[numbers_series.apply(lambda num: num % 2 == 1)]
odd_numbers


# <p style= "color: OliveDrab"> <font face = "marker felt">
#     Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers </p>

# In[564]:


positive_numbers= numbers_series[numbers_series.apply(lambda num: num > 0)]
positive_numbers


# <p style= "color: OliveDrab"> <font face = "marker felt">
#     Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers </p>

# In[565]:


negative_numbers= numbers_series[numbers_series.apply(lambda num: num < 0)]
negative_numbers


# <p style= "color: OliveDrab"> <font face = "marker felt">
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
#     </p>

# In[589]:


more_than_two=numbers_series[numbers_series.apply((lambda num: num >9))]
more_than_two


# <p style= "color: OliveDrab"> <font face = "marker felt">
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
# </p>

# In[570]:


numbers_squared= numbers_series**2
numbers_squared


# <p style= "color: OliveDrab"> <font face = "marker felt"> 
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
# </p>

# In[580]:


odd_negative_numbers= numbers_series[numbers_series.apply((lambda num: num < 0) and (lambda num: num % 2 == 1))]
odd_negative_numbers


# <p style= "color: OliveDrab"> <font face = "marker felt">
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
# </p>

# In[582]:


numbers_plus_five= numbers_series+5
numbers_plus_five


# <p style= "color: OliveDrab"> <font face = "marker felt">BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not. </p>

# In[ ]:




