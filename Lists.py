
""""
https://www.geeksforgeeks.org/python-list/
https://developers.google.com/edu/python/lists
https://docs.python.org/3/tutorial/datastructures.html
https://wiki.python.org/moin/TimeComplexity


Lists
Not homogeneous i.e A single list may contain DataTypes like Integers, Strings, as well as Objects
mutable, hence, they can be altered even after their creation.
List in Python are ordered and have a definite count
Each element in the list has its definite place in the list,
which allows duplicating of elements in the list, with each element having its own distinct place and credibility


Complexity :
insert & Delete : O(n)
Iteration : O(n)
append : O(1)
pop last : O(1)
Get item : O(1)

"""


Fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#Not Homogenous
Fruits2 = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana',3,4,5,["a","b",3]]
print (Fruits)

Fruits.append("Mango")            #Add at the end
#Note : print(Fruits.append("Choco"))    #append does not return anything , just modifies the list

Fruits.insert (4,"Strawberries")  #Add at given position

print(Fruits.count("apple"))      #Return the number of times x appears in the list

Fruits.remove("apple")
#Remove the first item (not all occurances) from the list whose value is equal to x. It raises a ValueError if there is no such item.

print(Fruits.index("kiwi"))  #list.index(x[, start[, end]])
#Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

Fruits.pop(1)  #Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.

Fruits.sort(key=str.lower,reverse=True)  #sort in place, Reverse boolean parameter optional,can be set to True

#Fruits.extend(Fruits2)   # or Fruits = Fruits + Fruits2 , Extend the list by appending all the items from the iterable
Fruits = Fruits + Fruits2

print (Fruits)

print(len(Fruits))

#Playing with index

print(Fruits[-1])
#negative sequence indexes represent positions from the end of the array.
# Instead of having to compute the offset as in List[len(List)-3],it is enough to just write List[-3].
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item and so on.

print(Fruits[-1][1])    #Nested Indexing

#Slicing
# Print elements of a range
# using Slice operation
Sliced_List = Fruits[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a
# pre-defined point to end
Sliced_List = Fruits[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = Fruits[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = Fruits[:-2]
print("\nSkip last 2 , Elements sliced till 2nd element from last: ")
print(Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = Fruits[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = Fruits[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)

"""
Notes :
these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.
methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 
This is a design principle for all mutable data structures in Python.

Another thing you might notice is that not all data can be sorted or compared. 
For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types.

"""


#FUNCTIONS 

List1=[3,6,793,78,6]
List2=[False]

print(len(List1))
print(min(List1))
print(max(List1))
print(sum(List1))
print(all(List2))   #Returns true if all element are true or if list is empty