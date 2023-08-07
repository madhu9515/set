set_={1,2,3,4,5,2,4,8}
print(set_)       #{1, 2, 3, 4, 5, 8}


empty_set=set()     
empty_set.add(10)   
empty_set.add(20)   
print(empty_set)    #{10, 20}

set_.remove(2)
print(set_)       #{1, 3, 4, 5, 8}

empty_set.clear()
print(empty_set)

set1={1,2,8,'madhu',('ram',10)} #it allows only imutable datatype not mutable datatype
print(set1)      #{('ram', 10), 1, 2, 'madhu'}

print(set_.union(set1))    #{1, 2, 3, 4, 5, 'madhu', 8, ('ram', 10)}

print(set_.intersection(set1))
print(set1.intersection(set_))

set_.update((12,9))
print(set_)     #{1, 3, 4, 5, 8, 9, 12}



