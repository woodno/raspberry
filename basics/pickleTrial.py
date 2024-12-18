import pickle
mylist = [True]
mylist.append(True)
mylist.append(False)
mylist.append(True)
f = open('test.txt', 'w+b')
s = pickle.dump(mylist, f)
f.close()
f=open('test.txt', 'r+b')
newList = pickle.load(f)
f.close()
print (newList)