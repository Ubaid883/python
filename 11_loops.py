x=6
while(x<=5):
  print(x)
  x=x+1

#for loop

for x in range(1,10):
     print(x)

#Arry 
days=["mon","thu","sat","wed","thr","fri","sun"]
for d in days:
    # if (d=="thr"):break  # loop stop
    if (d=="thr"):continue   # skip d
    print(d)

days=["mon","thu","sat","wed","thr","fri","sun"]
for d in days:
   print(d)