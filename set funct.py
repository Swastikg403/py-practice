#unordered and mutable

#add()
a={'1','2','3'}
a.add(4)

#update()  adds multiple elments
a.update([5,6])

#remove() if element present then remove it otherwise error 

#a.discard('3')  same as remove but no error thrown

#a.pop()  => removes any arbiatry elemnet usually first one removed because index not here and returns that elemsnt to be roemeved
b={'4','5'}
c=a.union(b)
#returns set with combine elements of a and b

#intersection

#difference
a={'1','2','3'}
b={'2','4'}
a.difference(b)
a.symmetric_difference(b)

