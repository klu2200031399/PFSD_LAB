import string
import random
s=10
ran= ''.join(random.sample(string.ascii_uppercase+string.digits,k=s))
print(ran)
s1=4
ran1 =''.join(random.sample(string.digits,k=6))
print(ran1)