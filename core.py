import requests
from qqbot import QQBotSlot as qqbotslot,RunBot
from package import Package

user_package = Package()

@qqbotslot
def onQQMessage(bot,contact,member,content):
    # print(contact.name)
    if not bot.isMe(contact,member):
        if member is not None:
            text = user_package.handle_message_str(member.name,content)
            bot.SendTo(contact,member.name+" :"+text)

RunBot()