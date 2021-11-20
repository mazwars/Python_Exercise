'''
Question :1

Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
Fill in the blanks in the code using any of the methods you’ve learned thus far,
like a for loop or a list comprehension.

'''

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for files in range(len(filenames)):
    if "hpp" in filenames[files][3:]:
        newfilenames.append(filenames[files][:-2])
    else:
        newfilenames.append(filenames[files])

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


'''
Question: 2

Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

'''


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split(" ")
    for word in words:
        # Create the pig latin word and add it to the list
        say += word[1:] + word[0] + "ay "
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

'''

Question 3:

The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
For example: 
640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
Fill in the blanks to make the code convert a permission in octal format into a string format.

'''


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for m in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if m >= value:
                result += letter
                m -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

'''

Question 5:

The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

'''

def group_list(group, users):
  members = ""
  if (len(group))!=0:
    members+=group+":"
  if (len(users))!=0:
    members+=" "+users[0]
  if (len(users)>1):
    for x in users[1:]:
      members+=", "+x
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


'''
The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 

'''

def guest_list(guests):
	for guest in guests:
		name, age, job=guest
		print("{} is {} years old and works as {}".format(name,age,job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

'''
In Python, a dictionary can only hold a single value for a given key.
To workaround this, our single value can be a list containing multiple values.
Here we have a dictionary called "wardrobe" with items of clothing and their colors.
Fill in the blanks to print a line for each item of clothing with
each color, for example: "red shirt", "blue shirt", and so on.
'''

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key,values in wardrobe.items():
	for value in values:
		print("{} {}".format(value, key))