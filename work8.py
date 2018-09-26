import random
q=random.randint(0,2)
a=eval(input(">>"))
if a==q:
    print("ping")
elif a-q==1:
    print("win")
elif a-q==-2:
    print("win")
else:
    print("draw")
    
