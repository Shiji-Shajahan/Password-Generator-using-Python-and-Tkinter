print('Project Password Generator')
print()

#Implementation of a password generator, that will create a random password based on the user needs

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

#The user should decide what the password contains (letters, numbers, special characters, upper or lower case)

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

def password_generation(length):
  password=''
  for n in range(length):
    password=random.choices(all_characters,k=length)
    password=''.join(password)
  return password
print()

#In random.choices the first argument accepts an iterable and the last argument specifies the number of items that will be randomly choosen from the given iterable.

#.join is used to join all characters returned from random.choices into a string
#the list returned from random.choices is add on an empty string and that acts as a seperator

#The user can write the length of the password
length=int(input('Please enter the length of password:'))
print()

#The program is able to generate more than one password, being the number defined by the user
number_of_passwords=int(input('Please enter the number of passwords required:'))
print()
n=0

#The user can store the password secretly in a file 
file=open("secret_file_password",'a')

while n!=number_of_passwords:
  new_password=password_generation(length)
  file.write(new_password)
  file.write("\n")
  n+=1
file.close()
print()