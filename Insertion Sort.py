def insertion_sort(list1):
	for i in range(1,len(list1)):
		j=i
		while(j>=1):
			if(list1[j]<list1[j-1]):
				temp = list1[j]
				list1[j] = list1[j-1]
				list1[j-1] = temp
			j-=1
	return list1
list1 = list(map(int,input("Enter space seprated values for list: \n").split()))
print(insertion_sort(list1))