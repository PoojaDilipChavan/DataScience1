"""
Sets
Unordered collection
Can not contain duplicates
Mutable - Can be modified after creating

Easy for checking whether a specific element is contained in the set than lists

Common uses include membership testing, removing duplicates from a sequence,
and computing mathematical operations such as intersection, union, difference, and symmetric difference.

There are currently two built-in set types, set and frozenset.



it is a hash table, implemented very similarly the Python dict with some optimizations
that take advantage of the fact that the values are always null (in a set, we only care about the keys.
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method),
and can be compared to other objects (it needs an __eq__() method).
Hashable objects which compare equal must have the same hash value.
"""

#The set type is mutable — the contents can be changed using methods like add() and remove().
#Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set.

set1={}     #Empty Set
set2={1,2,4,"Pooja"}


#Converting list to sets - get rid of duplicates
list1=[78,3,2,3,2,44,5]
set1=set(list1)

print(list1)
print(set1)

set2.add("Asha")    #Adding element to sets
print(set2)

#Mathematical Operations - Union , Intersection , Difference

setA={"Poo","Anj","Sallo","Apps"}
setB={"Poo","Anj","abha","Rodes","Shash"}

print(setA.union(setB))   #Method union / |
print(setA | setB)

print(setA.intersection(setB))   #Method intersection / &
print(setA & setB)

print(setA.difference(setB))   #Method difference / -
print(setB - setA)

#clear set contents
setA.clear()
print(setA)

#The frozenset type is immutable and hashable — its contents cannot be altered after it is created;
#it can therefore be used as a dictionary key or as an element of another set.

frozenset1=frozenset([2,3,45,66])       #frozenset
print(frozenset1)

#frozenset1.add(4)    Not allowed , as immutable error -'frozenset' object has no attribute 'add'

