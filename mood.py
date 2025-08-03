print("hello! i am AI bot! What's your name? ")
name=input()
print(f"nice to meet you, {name}!")
print("how are you feeling today (good/bad)? ")
mood=input().lower()
if mood =="good":
    print("im glad to hear that! ")
elif mood== "bad":
    print("im sorry to hear that. hope things get better soon...")   
else:
    print("i see. sometimes it is hard to put feelings into words.")   
print(f"it was nice chatting with you, {name}! Goodbye!!")      

