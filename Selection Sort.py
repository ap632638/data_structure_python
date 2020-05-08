def selection_sort(list1):
	for i in range(len(list1)):
		minimum = i
		for j in range(i+1,len(list1)):
			if(list1[j]<list1[minimum]):
				minimum = j
		if(minimum != i):
			temp = list1[minimum]
			list1[minimum] = list1[i]
			list1[i] = temp
	return list1
list1 = list(map(int,input("Enter space seprated list: \n").split()))
print(selection_sort(list1))