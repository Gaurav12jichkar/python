list1=[3,4,63,78,2,78]
s_list=list(map(lambda i:i**2,list1))
print(s_list)
squares=[lambda i=i:i**2 for i in range(1,11)]
for a in squares:
   print(a(),end=" ")
minimum=lambda a,b:a if a%b else b
print(minimum(2,8))

evenodd=lambda num:("even") if num%2==0 else ("odd")
print(evenodd(2))


