user = int (input())
#print (user)
sum = 0
for numidx in range(user):
	enter = input()
	lastnum = int (enter[-1])
	#print (lastnum)
	actnum = int(enter[:-1])
	total = actnum**lastnum
	sum = sum + total
print (sum)