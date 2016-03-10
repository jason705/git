num=input("input number:")
for x in range(2,num):
 if num%x==0:
  print "%d isn't prime number" %num
  break
else:
 print "%d is prime number" %num