#display the first time is came:
h1 = int(input("enter your h1: "))
m1 = int(input("enter your m1: "))
h2 = int(input("enter your h2: "))
m2 = int(input("enter your m2: "))

if( h1 < h2):
    print(h1, ":" , m1)
else:
  if ( h1 == h2):
     if ( m1 <= m2 ):
         print( h1 , ":" , m1)
      
          
     else:
         print(m2)
      
  else:
      print(h2, ":" , m2)
    
       
    


