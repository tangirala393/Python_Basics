'''
a = [1,2,3,4,5,6,7,8,9]

print("mean=",  int((sum(a)/len(a))))
b = int(len(a)/2)
print("median=", a[b])



#TO print middle letter of middle string in list
l1 = ["hare","rama","haZre","krishna","reddy"]
b=int(len(l1)/2)
c=l1[b]
print(len(c))
d=int(len(c)/2)
print(c[d])


#Python Numbers
a = 25e25

print(a)
print(type(a))

#
a = i+6j
print(a)
print(type(a))



#Python casting
a = 100
print(type(a))
a = float(a)
print(type(a))
b = str(a)
print(type(a))

b = "krishna"
c = int(b)
print(type(c))



#Python strings
a = "krishna reddy"

print(a[0])
print(a[2:5])

b = " krish "
print(b.strip(" "))
print(len(a))
print(a.lower())
print(a.upper())
print(a.capitalize())
b = "darling"
print(b.replace("d","k"))

print(b.split(b[1]))



#Python operators

a = 9
b = 20

add=a+b
sub=a-b
mul=a*b
div=a/b
modu=a%b
print(add,sub,mul,div,modu)


'''
#Python list

list1 = [1,3,5,6,"krish","reddy",29.8,'L']

list1[2]="koushik"
print(list1)
print(len(list1))
print(list1.append("rajesh"))
print(list1)
list1[2]="rajesh"
print(list1)
list1.insert(1,"orange")   #######  in print 
print(list1)
list1.remove(29.8)
print(list1)
list1.remove(list1[-1])  ######### not removing last element
print(list1)
print(list1.clear())
list2 = list(("k","g","f"))
print(list2)


      
