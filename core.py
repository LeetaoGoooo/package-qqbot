import requests
from qqbot import QQBotSlot as qqbotslot,RunBot
from package import Package

user_package = Package()

@qqbotslot
def onQQMessage(bot,contact,member,content):
    # print(contact.name)
    if not bot.isMe(contact,member):
        if member is None:
            text = user_package.handle_message_str(contact,content)
        else:
            text = user_package.handle_message_str(member.name,content)
        bot.SendTo(contact,text)

RunBot()