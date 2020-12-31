#list is ordered and changable and allows duplicate members
thislist = ["apple","banana","mango","orange","cherry","pineapple","jackfruit"]
print(thislist)
print(thislist[2])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:3])
print(thislist[3:])
print(thislist[-4:-1])
for x in thislist:
    print(x)
if "apple" in thislist:
    print("yess")
print(len(thislist))
thislist.append("kiwi") #add in the last in the list
print(thislist)
thislist.insert(2,"olla") #insert any where
print(thislist)
thislist.remove("olla")
print(thislist)
thislist.pop() #removes last element added
del thislist[3] #removes element from index value
print(thislist)
thislist.clear() #empties the list
print(thislist)

