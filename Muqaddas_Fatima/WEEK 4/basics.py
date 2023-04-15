print("Muqaddas Fatima")

#variables
x = '8th'
y=7                   #int
name= 'Muqaddas'       #string/char
isFemale = True        #bool
print(y)
print("My name is " + name)

name = 'Fatima'
print("My name is " + name +" and am in my " + x + " semester")

#strings
phrase = "Giraffe"
print(phrase.upper())
print(phrase.isupper()) # Check the string is in upercase letters
print(phrase.upper().isupper()) # convert the string to upercase letters then Check taht the string is in upercase letters or not
print(len(phrase)) # return length of string
print(phrase[0])  # return elemnt at 0 index
print(phrase.index("G")) # return index of string G
print(phrase.replace("Giraffe","Elephant")) # replace the  "giraffe" with the "elephant"


#numbers

from math import *
my_num= -5
print(abs(my_num))
print(pow(3,2))
print(min(3,2))
print(max(3,2))
print(round(3.782))
print(sqrt(3.782))
print(ceil(3.782))
print(floor(3.782)) #chop off the decimal part

# Take input from user
name= input ("Enter your name")
age= input ("Enter your age")
print("Hello" +name +", you are " + age)

#Type casting from string to float
num1=float(input ("Enter your 1st number"))
num2=float(input ("Enter your 2nd number"))
result= int(num1)+ int (num2)
print(result)
# for float
result= float(num1)+ float (num2)
print(result)

# Building Mad Lib Game in Python
color = input ("Enter color")
Plural_noun = input ("Enter Plural_noun")
celebrity =input ("Enter celebrity")
print("Roses are " +color)
print(Plural_noun+" are blue")
print("I love "+celebrity)