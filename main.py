from config import key
import requests #for web
from speech import mic1 #for mic

def chat1(chat):
    messages = [] #list which has all mesdsages 
    system_message = "You are an AI Bot, your name is Jarvis" #system message is the first message that the bot sends to Gemini
    message = {"role":"user", "parts": [{"text":system_message+" "+chat}]} #message is a dictionary with role and parts
    messages.append(message) #appending the message to the list
    data = {"contents": messages }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)
    t1 = response.json()
    print(t1.get("candidates")[0].get("content").get("parts")[0].get("text"))
    

#chat = "Who is MS Dhoni"
chat = mic1()
chat1(chat)