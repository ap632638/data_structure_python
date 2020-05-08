def partition(list1, low, high):
	i = low-1
	pivot = list1[high]
	for j in range(low,high):
		if(list1[j]<pivot):
			i+=1
			temp = list1[i]
			list1[i] = list1[j]
			list1[j] = temp
	temp = list1[i+1]
	list1[i+1] = list1[high]
	list1[high] = temp
	return i+1
def quicksort(list1, low,high):
	if(low < high):
		d = partition(list1, low, high)
		quicksort(list1, low, d-1)
		quicksort(list1, d+1, high)
		return list1
list1 = list(map(int,input("Enter space seprated list: ").split()))
print(quicksort(list1,0,len(list1)-1))