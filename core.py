import requests
from qqbot import QQBotSlot as qqbotslot,RunBot
from package import Package

user_package = Package()

@qqbotslot
def onQQMessage(bot,contact,member,content):
    if not bot.isMe(contact,member):
        # 群组聊天
        if member is not None:
            text = user_package.handle_message_str(member.name,content)
            bot.SendTo(contact,member.name+" :"+text)
        # 一对一聊天
        else:
            text = user_package.handle_message_str(contact,content)
            bot.SendTo(contact,text)

RunBot()