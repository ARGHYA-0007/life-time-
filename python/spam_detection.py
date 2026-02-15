x=(input(print("Enter your message: ")))
p1="Free money"
p2="Act now"
p3="Limited offer"
p4="Congratulations"
p5="Click here"
p7="Win prize"
p8="Urgent response"
p9="Claim reward"
p10="Exclusive deal"
if (p1.lower() in x.lower() or p2.lower() in x.lower() or p3.lower() in x.lower() 
    or p4.lower() in x.lower() or p5.lower() in x.lower() or p7.lower() in x.lower()
      or p8.lower() in x.lower() or p9.lower() in x.lower() or p10.lower() in x.lower()):
    print("This is a spam message.")
else:
    print("This is not a spam message.")

