f=open("input.txt","r")
string=[]
string.extend(f.read())
print "e number:%d"%string.count('e')
print "space number:%d"%string.count(' ')
print "length:%d"%len(string)
print "radio of e:%5.2f%%"%(float(string.count('e'))/len(string)*100)
print "radio of space:%5.2f%%"%(float(string.count(' '))/len(string)*100)