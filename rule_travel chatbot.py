import re, random
from colorama import Fore, init
init(autoreset=True)
destination={
    "beaches":["bali","maldives","phuket"],
    "mountains":["himalayas","kanchenjunga","apes"],
    "cities":["banaras","shimla","bangalore"]
}
jokes=[
    "why don't programmers like nature? too many bugs!!"
    "why did the computer go to the doctor? it catched a virus!!"
    "why do travellers always feel warm? because of all their hotspots!"
]
def normalise_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())
def recommend():
    print(Fore.CYAN +"Travel Bot: beaches, mountains or cities?")
    preference=input(Fore.YELLOW+"You: ")
    preference=normalise_input(preference)
    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(suggestion)
        print(Fore.GREEN+f"Travel Bot: How about{suggestion}??")
        print(Fore.MAGENTA+"do you like it?(yes/no)")
        answer=input(Fore.GREEN+"You: ")
        if answer=="yes":
            print(Fore.GREEN+f"Awesome ! enjoy {suggestion}")
        elif answer=="no":
            print(Fore.RED+"Too Bad")
            recommend()
        else:
            print(Fore.RED+"Dw ill suggest againn") 
            recommend()
    else:
        print(Fore.MAGENTA+"SORRY I DONT UNDERSTAND")      
    show_help()
def packing_tips():
    print(Fore.CYAN+"Where to??")  
    location=normalise_input(input(Fore.YELLOW("You: ")))      
    print(Fore.CYAN+"How many days")  
    days=normalise_input(input(Fore.YELLOW("You: ")))
    print(Fore.GREEN+f"Packing tips for {location} location for {days} days:")   
    print(Fore.GREEN +"check weather") 
    print(Fore.GREEN+"pack versatile clothes") 
    print(Fore.GREEN+"bring a charger along.") 
def tell_joke():
    print(Fore.GREEN+f"Travel bot:{random.choice(jokes)}")       

def show_help():
    print(Fore.MAGENTA+"\nI can:")
    print(Fore.GREEN+"suggest travel spots:(say recommendation)")
    print(Fore.GREEN+"offer packing tips:(say packing)")
    print(Fore.GREEN+"say jokes:(say jokes)")
    print(Fore.CYAN+"type bye to end.\n")
def chat():
    show_help()
    while True:
        user_input=input(Fore.YELLOW+"You: ")
        user_input=normalise_input(user_input)
        if "recommend" in user_input or "suggest in user_input":
            recommend()
        elif "packing" in user_input :
            packing_tips()  
        elif "jokes" in user_input :
            tell_joke() 
        elif "help" in user_input :
            show_help()
        if "exit" in user_input or "bye":
            print(Fore.CYAN+"Good bye! Trravelll safeee!!!!")    
            break
        else:
            print(Fore.RED+"Could you rephrase?")
if __name__=="__main__":
    chat()



