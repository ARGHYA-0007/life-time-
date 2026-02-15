with open("censor.txt","w") as f:
    f.write("""Agent Mira kept the secret in her notebook. She wrote down the password and marked the file confidential.
When the ssn slipped into the wrong hands, a leak followed. The document was labeled classified and forbidden
to share. Later she warned, "No spoilers — don't reveal the plot," but someone typed a badword1 in the comments.
""")
censor_words = [
    "secret",
    "password",
    "confidential",
    "ssn",
    "leak",
    "spoiler",
    "forbidden",
    "classified",
    "badword1",  
    "badword2" 
]
f=open("censor.txt","r")
content=f.read()
for word in censor_words:
    content=content.replace(word,"#"*len(word))
f=open("censor.txt","w")
f.write(content)
f.close()