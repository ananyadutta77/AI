import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}WELCOME TO SENTIMENT SPY!!{Style.RESET_ALL}")
user_name=input(f"{Fore.MAGENTA}PLEASE ENTER YOUR NAME: {Style.RESET_ALL}").strip()
if not user_name:
    user_name="Mystery Agent"
convo_history=[]
print(f"\n{Fore.BLUE}HELLO, AGENT {user_name}") 
print("type a sentence and i will analyse your sentiments with TextBlob and show you the sentiment...")  
print(f"Type{Fore.YELLOW}'reset'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN}," 
      f"or{Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:
    user_input=input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or valid command...{Style.RESET_ALL}")
        continue
    if user_input.lower()=="exit":
        print(f"{Fore.MAGENTA}Exiting Sentiment Spy... Farewell, Agent {user_name}...{Style.RESET_ALL}")
        break
    elif user_input.lower()=="reset":
        convo_history.clear()
        print(f"{Fore.BLUE}All conversation history cleareddd!{Style.RESET_ALL}")
    elif user_input.lower()=="history":
        if not convo_history:
            print(f"{Fore.BLUE}No conversation history yettt...{Style.RESET_ALL}") 
        else:
            print(f"{Fore.YELLOW}conversation history:-{Style.RESET_ALL}")     
            for idx, (text,polarity,senti_type) in enumerate(convo_history, start=1):
                if senti_type=="Positive":
                    color=Fore.GREEN
                    emoji="😊"
                elif senti_type=="Negative":
                    color=Fore.RED
                    emoji="😥"    
                else:
                    color=Fore.YELLOW
                    emoji="🙃"    
                print(f"{idx}. {color}{emoji}  {text}"
                      f"(Polarity: {polarity:.2f},{senti_type}){Style.RESET_ALL}") 
        continue    
    polarity=TextBlob(user_input).sentiment.polarity      
    if polarity>0.25:
        senti_type="Positive"
        color=Fore.GREEN
        emoji="😊"
    elif polarity<-0.25:
        senti_type="Negative"
        color=Fore.RED
        emoji="😥"    
    else:
        senti_type="Neutral"
        color=Fore.YELLOW
        emoji="🙃"  
    convo_history.append((user_input,polarity,senti_type)) 
    print(f"{color}{emoji} {senti_type} sentiment detected!!"
          f"(Polarity:{polarity:.2f}){Style.RESET_ALL}")  


