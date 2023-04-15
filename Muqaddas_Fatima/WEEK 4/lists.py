#Lists in Python
#List is a data type that is used to store multiple items in a single variable. List items are ordered, changeable, and allow duplicate values.
friends= ["muqs" ,"amal","eman","eisha" ,"hala","maha"]
print(friends[2])
print(friends[-1])#return last item in index
print(friends[1:])#return from 1st index to last item in index
print(friends[:3])#return from 1st index to 3rd item in index but not 3rd one
print(friends[1:3])#return from 1st index to 3rd item in index but not 3rd one
friends[3]="zoha" #modify value at 3rd index

#list functions
lucky_number = [5,8,9,3,2,8]

friends.extend(lucky_number) #adds lucky nim to frnds list
friends.append("zara")
print(friends)

friends.insert(3,"kelly") #insert value at 3rd index
print("kelly" in friends) #check weather "kelly" is in list or not
friends.index("kelly") #check  "kelly" is present in which index and gives index num
friends.remove('zara') #remove value specified from list
friends.pop() #remove values from last of the list
friends.clear() # delete all the items from list
print(friends)
lucky_number.count(8) # count the occurence of 8 in list
lucky_number.sort()   # arrange elements in list in asc order
lucky_number.reverse() # reverse elements in list
friends2= friends.copy() # make copy of list
print(friends2)
