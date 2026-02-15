tables=int(input("enter you number:  "))
x=tables
lists=[]
for i in range(1,11):
    print(f"{tables}X{i}={tables*i}")
    lists.append(f"{tables}X{i}={tables*i}\n")
with open ("tables.txt","a") as f:
        f.write(f"TABLE OF {x}\n")
        f.writelines((lists))
        f.write("\n")
