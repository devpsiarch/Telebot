import os
import sys
import telebot
from groq import Groq
SYSTEM_PRE_PROMPT = "You are a helfull personal assistant named dave and a dear friend to me since a long time ago, you will always repond in a normal manner just as a human would."
#/**********/
#    defs
#/**********/
def read_confedentials(filename):
    file = open(filename,'r')
    lines = [line.strip() for line in file]
    file.close()
    return lines[0],lines[1]

def chat_bot(prompt:str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content":SYSTEM_PRE_PROMPT 
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    output = ""
    for chunk in completion:
        output += chunk.choices[0].delta.content or "" 
    return output

#---------------#
#     vars
#---------------#

BOT_TOKEN , API_TOKEN = read_confedentials("confidential.txt")
os.environ['GROQ_API_KEY'] = API_TOKEN
client = Groq()


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    reply = chat_bot(message.text)
    bot.reply_to(message,reply)


bot.infinity_polling()
