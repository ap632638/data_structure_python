def merge_sort(arr):
	if(len(arr)==1):
		return arr
	else:
		start=0
		end=len(arr)
		mid=(start+end)//2
		l1=merge_sort(arr[0:mid])
		l2=merge_sort(arr[mid:end])
		return merge(l1,l2)
def merge(l1,l2):
	i,j=0,0
	merge_list=[]
	while(i<len(l1) and j<len(l2)):
		if(l1[i]<l2[j]):
			merge_list.append(l1[i])
			i+=1
		else:
			merge_list.append(l2[j])
			j+=1
	if(i<len(l1)):
		merge_list.extend(l1[i:])
	if(j<len(l2)):
		merge_list.extend(l2[j:])
	return merge_list

list1 = list(map(int,input("Enter space seprated list: \n").split()))
print(merge_sort(list1))