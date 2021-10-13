
lst1=[i for i in range(3,100,3)]
lst2=[i for i in range(5,100,5)]
lst3=list((set(lst1).intersection(set(lst2))))
print(lst3)