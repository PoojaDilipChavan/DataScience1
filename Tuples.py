"""
Tuples
https://www.geeksforgeeks.org/python-tuples/?ref=lbp
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
https://docs.python.org/3/library/stdtypes.html#typesseq
https://wiki.python.org/moin/TimeComplexity                      -- complexity for tuples is same as lists (indexed) 


created by placing sequence of values separated by ‘comma’ with or without the use of parentheses for grouping of data sequence.

can contain any number of elements and of any datatype (like strings, integers, list, etc.)
can contain duplicates

accessed via unpacking or indexing

immutable objects : An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered.
A new object has to be created if a different value has to be stored.
They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

Time complexity :
same as list : 
access= O(1)
iterate = O(n)

"""

tuple1=()       #Creation of empty tuple , paranthesis necessary
print(len(tuple1))

tuple1 = "lol",   #creation of tuple with single elemenet , comma necessary
print(len(tuple1))

tuple1= (1,2,3,"Pooja","sudhir",[5,7,"lol"],1,2)     #can have duplicates
tuple2= 189,"mgf",90,"hfk"    #can be used without paranthesis
print(tuple1+tuple2)          #concatenation of tuples

#Indexing & unpacking
print(tuple1[3])
print(tuple1[::-1])

print(tuple1[3:5])    #slicing

Tuple3 = tuple('GEEKSFORGEEKS')

# Removing First element
print("Removal of First Element: ")
print(Tuple3[1:])

a,b,c,d=tuple2   #Unpacking of tuples , In unpacking of tuple number of variables on left hand side should be equal to number of values in given tuple a.
print(a)
print(b)
print(c)
print(d)


tuple4=8,9,"a"
del tuple4      #deletion of tuple, Tuples are immutable and hence they do not allow deletion of a part of it
#print(tuple4)


#Functions
tuple4=8,77,89,4,5,7
print(len(tuple4))
print(max(tuple4))
print(min(tuple4))
print(sum(tuple4))

print(sorted(tuple4))       #sorting ,	input elements in the tuple and return a new sorted list

list1=["bfk",5,4,3,2,9]
tuple5=tuple(list1)         #Convert an iterable to a tuple.

print(tuple5)

