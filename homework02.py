#-*-coding=utf-8-*-
money=5000
print u'輸入提款金額:'
a=raw_input()
withdraw=int(a)
if withdraw>money:
	str='您的存款餘額不足\n'
	print str.decode('utf-8')
elif withdraw==money:
	str='您的存款無剩餘存款\n'
	print str.decode('utf-8')
else:
	str='您的存款還剩%d元\n' %(money-withdraw)
	print str.decode('utf-8')

f=open("ATM.txt","a")
f.write(str)
f.close