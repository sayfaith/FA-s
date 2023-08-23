#!/usr/bin/env python
# coding: utf-8

# In[73]:


nationality = int(input("Enter your nationality: Filipino[1], Foreigner[2]: "))
gender = int(input("Enter your gender: Male[1], Female[2]: "))
year = int(input("Enter your year level: [1], [2], [3], [4]: ")) 
fee = 800
if (gender == 1) and (year == 4): fee += 500
if (gender == 2) and (year == 1 or year == 2): fee += 250
if (nationality == 2): fee += 400 #For foreign students
print(f"\nTotal Miscellaneous Fee: ₱{fee}")


# In[10]:


place = int(input("Enter the destination of the call: Phil [1], Asia [2], Africa [3], America [4], Antartica [5], Europe [6] or Australia [7]: "))
duration = int(input("Enter the duration of the call: Sec[1], Min[2] or Hour[3]: ")) 
time = int(input("Enter the time of call: Morning [1], Afternoon [2] or Night [3]: "))
            
bill = 0 

if place == 1: #place
    bill += 20
elif place == 2:
    bill += 30
elif place == 3: 
    bill += 40
elif place == 4:
    bill += 50
elif place == 5 : 
    bill += 60
elif place == 6:
    bill += 70
elif place == 7:
    bill += 80
else:
    print("Wrong number of place input. Please try again. ")
    
    
if time == 1:
    bill += 10
elif time == 2:
    bill += 20
elif time == 3:
    bill +=30
else:
    print("Wrong number of time input. Please try again. ")
        
if duration == 1:
    bill += 20
elif duration == 2:
    bill += 45
elif duration == 3:
    bill += 60
else:
    print("Wrong duration of call input. Please try again. ")

    
print(f"\nThe call's total bill is ₱{bill}")


# In[8]:


from IPython.display import Image

face = input("Would you like to display your face? [y/n]: ").lower()
if face == "y":
    img = r"C:\Users\linds\Downloads\face.jpg"
    display.display(Image(filename=img))
else:
    print("No face display")

import calendar

def date(year, month, day):
    birthday = calendar.month(year, month, 15, 5)
    birthday = birthday.replace(f"{day}", f"\033[1;33m{day}\033[m", 1)
    return birthday

month = int(input("\nEnter the month of your birthday (1-12): "))
day = int(input("Enter the day of your birthday (1-31): "))
year = int(input("Enter the year of your birthday: "))

print("\n")
print(date(year, month, day))

