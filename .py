def check_even_odd(n):
   if not isinstance(n,int):
      break
   if n%2==0:
      print("even")
   else:
      print("odd")
check_even_odd(10)
check_even_odd(11)
result=check_even_odd(5.25)
print("function returned :{result}")
