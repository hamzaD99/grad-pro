import telepot
from telepot.loop import MessageLoop
import telegram_sender
import cv2
import os

bot = telegram_sender.bot
known_chatId = telegram_sender.chat_id
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        if command == '/photo' and str(chat_id) == known_chatId:
            video_capture = cv2.VideoCapture(0)
            ret, frame = video_capture.read()
            cv2.imwrite('temp.jpg',frame)
            bot.sendPhoto(chat_id, open('temp.jpg','rb'))
            os.remove('temp.jpg')
            video_capture.release()
            cv2.destroyAllWindows()
        else:
            bot.sendMessage(chat_id, 'Unknown command.')

MessageLoop(bot, handle).run_as_thread()

print("Bot is listening for commands...")

while True:
    pass
