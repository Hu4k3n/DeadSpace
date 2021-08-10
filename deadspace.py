from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
import logging
import youtube_dl
import os
import sys
import subprocess
updater=Updater(token='<Token>',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    print ("New User detected")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome To HurakenTunes\n\nHow to use\nShare the link of the youtube video you wish to convert\nDo wait the server is not always running\n\nSincerely,\nHuraken.")
def ost (update,context):
        cmd=update.message.text
        cmd=cmd.strip('\n')
        print ("Command:"+str(cmd))
        print ("Report:")
        #os.system(str(cmd))
        subprocess.call([str(cmd)+" 2>&1 | tee output.txt"],shell=True)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Executed")
        f=open("output.txt","r")
        x=f.readlines()
        #for i in x :
        i="".join(j for j in x)
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(i))
        print("\n")
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, ost)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()
