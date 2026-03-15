#Personal chat assistant

import datetime
import time

name=input("welcome,enter your name:")
presenthour=datetime.datetime.now().hour

if 5<= presenthour<=11:
   print("good morning",name)
elif 11<= presenthour<=17:
   print("good afternoon",name)
elif 17<= presenthour<=20:
   print("good evening",name)
else:
    print("good night")   


print("Namaste ! Welcome to your chatbot")
print("You can ask me any query, type 'bye'to exit from bot")

#chatbot memory creation (dictionary of responses)

responses = {
    "hello": "hi,welcome. how can i help you?",
    "how are you":"i m very fine. thank you",
    "who are you":"i am smart buddy",
    "motivate me":"keep going one day your hardwork becomes your big achivement",
    "happy" : "great to hear that"
 }

#meton /function to get response of chatbot
def getResponseOfBot(userquery):
    userquery=userquery.lower()
    for eachkey in responses:
        if eachkey in userquery:
            return responses[eachkey]
    return"i m not able to tell that yet .i m in leraing mood"        

#take input
while True:
    userInput=input("please ask your query:")
    reply=getResponseOfBot(userInput)
    print("Bot Response :", reply)

    if "bye" in userInput.lower():
        break
