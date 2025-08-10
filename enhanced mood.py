print("hello! i am AI bot! What's your name? ")
name=input()
print(f"nice to meet you, {name}!")

chat = True
while chat:
    print("how are you feeling today (good/bad/okay)? ")
    mood=input().lower()
    if mood =="good":
        print("im glad to hear that! ")
    elif mood== "bad":
        print("im sorry to hear that. hope things get better soon...")   
    elif mood=="okay":
        print("got it. somtimes ok is just right.")    
    else:
        print("i see. sometimes it is hard to put feelings into words.")   
    print("what is your favourite thing todo in free time?")    
    hobby=input()
    print(f"wow. {hobby} is a wonderful thing to keep one engaged...")
    print(" do you want to continue chatting?(write exit to exit)")
    yn=input().lower()
    if yn == "exit":
        print(f"it was nice chatting with you, {name}! Goodbye!!")
        chat = False

 
