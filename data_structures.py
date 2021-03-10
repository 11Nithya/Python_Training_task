#Exploring the built-in methods of data structure and write 5 code using those methods
#The built-in data structures are
#1)String
my_message="hello world"

print(len(my_message))      # Prints the Length of the String. Index starts from Zero
print(my_message.upper())   # Prints the String in Upper Case
print(my_message.lower())   # Prints the String in Lower Case
print(my_message.count('l'))    # Prints number of occurances of the letter 'l'
print(my_message.count('Hello'))    # Prints number of occurances of the word 'Hello'
print(my_message.find('l'))     # Prints the index of first occurance of the letter '


#2)list
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

print(names)    # Prints the items of the List
print(len(names))       # Prints the Length of the List. Index starts from Zero.
print(names[0])     # Prints the item present in the 0th index of the List.


# Adding elements to the List
names.append('gmail')   # Adding element to the list
names.insert(3, 'watsapp')      # Inserts the item at 3rd index.
names.extend(['netflix', 'walmart', 'kroger'])    # Adds the new list to the existing list
names = [*names, 'signal']  # Adds the new list to the existing list
print(names)

print('gmail' in names)     # Prints True if the item is present in the list

# Removing Items from the List
names.remove('kroger')  # Removes the item 'kroger' from the List
names.pop()     # By default this will remove the last item in the List
# pop method returns the item that it has removed from the List
names.pop(3)    # Removes the item in the 3rd index of the List

#3)Set
a = {1, 2, 3, 3, 4}
print(len(a))   # Prints the Length of the Set

# Membership test
1 in a  # Prints True if the item is in a

# Set Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.union(b)  # Prints {1, 2, 3, 4, 5, 6}

c = {6, 7, 8, 9}

a.union(b, c)   # Prints {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Set Intersection
a.intersection(b)   # Returns a new set {3, 4}

# Set Difference
# Returns a new set with the elements in set a which are not in b
a.difference(b)
# a - b   # Prints {1, 2}


#4)Dictionary
dictionary:
a={"eid":12, "name":"xyz"}# prints the len of keys in dictionary
b=len(a)
print(b)

c={"eid":123, "name":"xyz"}# prints the last key value pair in dictionary
d=c.popitem()
print(d)

d={"eid":123,"name":"abc"}
d["location"]='bangalore'  # adds the another key value pair
print(d)

d1={"eid":123,"name":"abc"}
d1.pop("name")
print(d1)                 # prints only the last removed key

d2={"eid":123,"name":"abc"}
d2.get("eid")
print(d2)                # prints only the specific key mentioned


#5)Tuple
a=("hi","hello")
b=len(a)
print(b) # prints the length of tuple

b=("hi","hello",123, 45, 67)
print(b[1:3])    # prints list of tuples from the specified start index and end index

print(123 in b)# memnership operator checks whether the element is present or not

print(122 not in b)

c=("hi","hello",123, 45, 67)
for i in c:
    print(c)   # looping over the tuple

d=("hi","hello",123, 45, 67)
s=d.index(123)
print(s)     # returns index of specified element in tuple




