import telepot
from dotenv import load_dotenv
import os
load_dotenv()

def getChatId():
    return bot.getUpdates()
def sendMessage(msg):
    bot.sendMessage(chat_id, msg)

bot = telepot.Bot(os.getenv('BOT_TOKEN'))
chat_id = os.getenv('CHAT_ID')

# print(getChatId())
sendMessage("Hello lhadslkdsadjas")