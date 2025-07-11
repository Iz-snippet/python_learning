# a spam comment is defined as a a text containsing following keywords:
# "make a lot of money ", "buy now", "subscribe this","click this". write a program to detect these spams

p1="make a lot of money "
p2="buy now"
p3="subscribe this"
p4="click this"

massage=input ("enetr your massage:- ")

if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("it is a scam.")

else:
    print("it is not a scam.")