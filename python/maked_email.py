x=input("enter you email")
y=len(x)
x_list=list(x)
for i in range (2,y-9):
    x_list[i]="*"
masked_email = "".join(x_list)
print("".join(x_list))