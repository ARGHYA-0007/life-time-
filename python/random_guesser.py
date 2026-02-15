import random
random=random.randint(1,101)
for i in range(0,100):
    guess=int(input("\nguess the number: "))
    if guess==random:
        print("this time you got it right")
        break
    elif guess>random:
        print("try some lesser")
    else:
        print("try some greater")
print(f"you guess it in {i+1} try")