#John Kushkorov
#part1
def greet(first_name, last_name):
    greeting = 'My name is ' + last_name + ', ' + first_name + ' ' + last_name + '!'
    return greeting
print(greet('John', 'kush')

#part2
# Importing the pandas module
      
import pandas as pd

# Reading in the global temperature data from url
url="https://pkgstore.datahub.io/core/global-temp/annual_csv/data/a26b154688b061cdd04f1df36e4408be/annual_csv.csv"
global_temp = pd.read_csv(url)#reading the data

# displaying the the data set
display(global_temp)

#part3 
%matplotlib inline#using the matplotlib libary 

import matplotlib.pyplot as plt


plt.plot(global_temp['Year'], global_temp['Mean'])


# Adding some labels 
plt.xlabel('Year') 
plt.ylabel('Mean')

#testing

%matplotlib inline

import matplotlib.pyplot as plt

plt.plot(global_temp['Year'], global_temp['Mean'])
plt.scatter(global_temp['Year'], global_temp['Mean'])
plt.bar(global_temp['Year'], global_temp['Mean'])
      

# Adding some labels 
plt.xlabel('Year') 
plt.ylabel('Mean') 
