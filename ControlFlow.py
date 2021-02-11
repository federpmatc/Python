if (False) :
     print ("Hello, it's true")
     print ("good bye")
if (False) :
    print ("") 


for counter in range(1, 6) :
    print(counter)

#can also be written like this:

numbers = range(1,6)
for count in numbers:
	print (count)
while True:
    print("Enter a # divisble by 3")
    response = input()
    if int(response) % 7 == 0:
        break

response = 1
while (int(response) % 7) != 0:
    print("Enter a #3")
    response = input()
    if int(response) % 7 == 0:
        break

c=5
while c != 0:
    print (c)
    c -= 1

#bool(0) == FALSE
c = 4
while c :
    print (c)
    c -= 1

c=5
#True is case sensitive
while True:
    print (c)
    c -= 1
    if c == 0:
        break


