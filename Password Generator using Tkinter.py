print('Project Password Generator using Tkinter')
print()

#Implementation of a password generator, that will create a random password based on the user needs using Tkinter

from tkinter import *
# imports every exposed object in Tkinter 
#Tkinter is the standard GUI library for Python. 

import string
#builtin string library which contains a collection of string constants

import random
#import random imports the random module, which contains a variety of things to do with random number generation

lower_case_letters= string.ascii_lowercase
#string.ascii_lowercase display the lowercase letters'abcdefghijklmnopqrstuvwxyz'

upper_case_letters= string.ascii_uppercase
#string.ascii_uppercase display the uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers=string.digits
#string.digits display the numbers string '0123456789'

special_characters= string.punctuation
#String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#string.punctuation display the special characters

#The user can decide what the password contains (letters, numbers, special characters, upper or lower case)

def generate_characters():
  all_characters=''

  user_wish_lower=str(input("Enter your wish for lowercase letters, type y or n:"))
  if user_wish_lower =='y':
    all_characters+=lower_case_letters
  print()

  user_wish_upper=str(input("Enter your wish for uppercase letters, type y or n:"))
  if user_wish_upper =='y':
    all_characters+=upper_case_letters
  print()

  user_wish_number=str(input("Enter your wish for digits, type y or n:"))
  if user_wish_number =='y':
    all_characters+=numbers
  print()

  user_wish_punctuation=str(input("Enter your wish for special characters, type y or n:"))
  if user_wish_punctuation =='y':
    all_characters+=special_characters
  all_characters=list(all_characters)
  return all_characters
  print()

  #lowercase letters or uppercase letters or digits or special characters are concatenated into all_characters

all_characters=generate_characters()
random.shuffle(all_characters)
#random.shuffle() takes a list as it's argument and changes the list item position randomly

def password_generation():
  #get the length of the password
  length=val.get()
  password=''
  for n in range(length):
    password=random.choices(all_characters,k=length)
    password=''.join(password)
  password_label.config(text=password)

#user can define the length of the password
#In random.choices the first argument accepts an iterable and the last argument specifies the number of items that will be randomly choosen from the given iterable.

#.join is used to join all characters returned from random.choices into a string
#the list returned from random.choices is add on an empty string and that acts as a seperator

#creating basic Tkinter window
window= Tk()
window.geometry("450x400")
#setting the default window size using geometry function. size of the window width=450 and height =400

window.resizable(0,0)
#this prevents from resizing the window

window.title("Password Generator")
#giving title for the window

lenlabel=StringVar()
#value holder for string variables

lenlabel.set("Password length:")
#set the variable to the VALUE

lentitle=Label(window, textvariable=lenlabel,bg="yellow",fg="green",font=("Calibri",20))

lentitle.grid(row=0, column=4)
#grid uses the matrix row column concepts to organize the widgets

val= IntVar() 
#value holder for integer variables

spinlength= Spinbox(window, from_=8, to_=24, textvariable=val, width=13,font=("Calibri",20))

spinlength.grid(row=1,column=4)

btn=Button(window,text="Password Generate",bg="orange",fg="red",command=password_generation,font=("Calibri",20))
#bg and fg changing the background and foreground colour

btn.grid(row=3,column=4)

password_label=Label(window,font=("Calibri",30))
#setting the label font
password_label.grid(row=5,column=4) 

window.mainloop()