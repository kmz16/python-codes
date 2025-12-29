print("welconme calcutor ")
a=float(input("first enter "))
b=float(input("two enter "))

c=input("in . ?(yes/no) ").strip().lower()
if c == "no":
   
   g=input("-,+,/,* in please enter ").strip().lower()
   
   if g == "-":
      d=int(a+b)
      print(f"answer {d}")
   if g == "+":
      e=int(a-b)
      print(f"answer {e}")
   
   if g == "/":
      f=int(a/b)
      print(f"answer {f}")
    
   if g == "*":
      k=int(a*b)
      print(f"answer {k}")

if c == "yes":
   
   g=input("-,+,/,* in please enter ").strip().lower()
   
   if g == "-":
      d=str(a+b)
      print(f"answer {d}")
   if g == "+":
      e=str(a-b)
      print(f"answer {e}")
   
   if g == "/":
      f=str(a/b)
      print(f"answer {f}")
    
   if g == "*":
      k=str(a*b)
      print(f"answer {k}")
   
