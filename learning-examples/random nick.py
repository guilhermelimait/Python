
# toda vez que se roda, um novo nome é dado ao usuario

import random

list1 = ["Mad","Crazy","Wonder","Duck","Old"]
list2 = ["Ghost","Cosmonaut","Boobs","Ring","Joe","Bill"]

a = random.choice(list1)
b = random.choice(list2)
print (a,b)

print ()
for _ in range(len(list2)):
    print (f"{random.choice(list1)}_{random.choice(list2)}")