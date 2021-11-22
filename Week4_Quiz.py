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

##### New Quiz on Dictionary #####
'''


The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
'''

def email_list(domains):
	emails = []
	for domain,users in domains.items():
	  for user in users:
	    emails.append(user+ "@" + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

###############

'''


The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

'''

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for key,users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if(user not in user_groups.keys()):
				user_groups[user]=[]
			user_groups[user].append(key)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#####

'''

The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

'''

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for key,value in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


##################

'''
Assessment: Graded Assessment module 4
'''

'''
Ques 1
The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
'''


def format_address(address_string):
    # Declare variables

    # Separate the address string into parts
    list1 = address_string.split(" ")
    # Traverse through the address parts
    st = ""
    for x in range(len(list1)):
        if (x != 0):
            st += list1[x] + " "
        # Determine if the address part is the
        # house number or part of the street name

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(list1[0], st.strip())


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
############

