#-*-coding:utf-8-*-
import random
count=0
n=0
min=1
max=99
password=random.randint(1,99)
while n!=password:
	print u'輸入%d到%d數字:' %(min,max)
	n=input()
	if n<password and n>min:
		min=n
		count+=1
	elif n>password and n<max:
		max=n
		count+=1
print u'答案是%d，共猜了%d次' %(password,count)
