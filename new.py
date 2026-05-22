print("786 13")
name="tsb" #identifier(variable) can't start with digit and dont include specciaal symbols 
age=23 #number can be written without ""but string wil be written in it or single comma'name '
print("my name is",name)
name2=name 
print(name2) #we can store a variable in another variable
print(type(name)) #to print type of variable
print(type(age))
student=True #boolean and none type
partner=None
print(type(student),type(partner))
#keywords in phython can't be identifier (eg True False etc)
#phthon is case sensitive means eg A and a is different terms like True keyword must start from capital Tnother wise it is a variabl

#arithmetic operators also % for remainder and ** for power 
a=7
b=6
c=a+b
print(c)
print(a+b) #shift+alt+down arrow to write again
print(a-b)
print(a*b)
print(a/b)

#relational operators
print(a==b)
print(a!=b)#not equal
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

#assingnment operators 
#a=7 assisning 7 to a
num=10
num+=10 #num=num+10(20) same -=,%=,*=,/=,**=
print(num)

#logiccal operatorss and, or, not
#not reversal of true-false false to true
print(not True)
print(not (a>b))#a=7 b=6 a>b=true
#and or booleaan and give true when both are true or give true when even one is true
print((a>b) and (num>b))
print((a>b)or(a<b))

#type coversion (changing one variable form to another it is automatically done by compiler)
cc=2
d=3.33
sum=cc+d
print(sum)#answer automatially in ineteger
e=3.43
f=int(e)#type casting manual conversion
print(f)
