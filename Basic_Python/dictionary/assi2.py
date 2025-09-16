"""Q.2)  You have a list of email addresses and you want to extract the domain part (the part
 after '@') from each email address."""
 
email=[
     {"email":"vaibhav@gmail.com"},
     {"email":"tejas@gmail.com"},
     {"email":"sai@gmail.com"},
     {"email":"raj@gmail.com"},
     {"email":"aditya@gmail.com"},
     {"email":"shrya@gmail.com"}
 ]
domain=[]
for em in email:
    st=em["email"]
    idx=st.find("@")
    domain.append(st[idx+1:])
for i in domain:
    print(i)