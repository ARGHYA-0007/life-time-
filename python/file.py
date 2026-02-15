# making a new file and writing there
x="aniruddha student of roll number 10  getting 30/50 so bad downfall.\nbut no problem life is full of up and down.\nbut why he is getting only downsss "
f=open("anidownfall.txt","w")
f.write(x)
f.close()


# reading the file which i made before and write in it
f=open("anidownfall.txt")# in open() function by default it use read mode 
                         #we no need to tell it for read mode
print(f.read())
f.close()#closing file after doing thing is imp like closing fridge after use


#more file functions
i=open("arghya.txt","w")
i.write("i dont care\nwho are you\nbut dont bully me\nmy life my rules\n")
i.close()
i=open("arghya.txt")
x=i.readlines()#<readlines()> function is for printing all the line at one call
print(x,type(x))#type of the out put of the function <readlines()> is list
i.close()


#<readline()> function
i=open("arghya.txt")
x=i.readline() #<readline()> function reading one line one only and using 
               #againg the same thing will print the next line one by one
print(x)
x=i.readline()
print(x)
x=i.readline()
print(x)
x=i.readline()
print(x)

i.close()
# <with statement> using that statement we no need to close() the file it do automatically
with open("arghya.txt") as f:#when we get out of the with statement the automatically the file 
    print(f.read())          #will be closed
#if the string is in the file or not
i=open("arghya.txt")
content= i.read()
if "life" in content:
    print("yes")
else:
    print("no sorry ")