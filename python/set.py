x={12345,3456,56789}
y={12345,3456,56789,1234567}
print(x)
print(len(x))
#x.remove(123)#will show error if 12345 not found
x.discard(123)#will not show error if 12345 not found
#x.pop()#removes a random element which is not useful in set acc to me
print(x.union(y))#union of two sets
print(x.intersection(y))#intersection of two sets
print(x.difference(y))#elements in x but not in y
print(y.difference(x))#elements in y but not in x
print(y.issubset(x))#is x a subset of y
print(y-x) #elements in y but not in x