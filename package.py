import os
import re
import requests

class Package(object):
    __slots__ = ['_record']

    def __init__(self):
        self._record = Record()

    def handle_message_str(self, member, message_str):
        """
        :param message_str:
        :return:
        """
        try:
            # judge if share url or get package
            if message_str[:5] == 'https':
                if message_str.find("https://activity.waimai.meituan.com/") != -1 or message_str.find("https://h5.ele.me/hongbao/") != -1:
                    self._record.record(member,message_str)
                    return "请输入手机号码:"
                else:
                    return "请确保,饿了么是以https://h5.ele.me/hongbao/开头的链接,美团是以https://activity.waimai.meituan.com/开头的链接"
            else:
                # check phone
                if self.check_phone_number_format(message_str.strip()):
                    # get record
                    url = self._record.get_record(member)
                    if url == False:
                        return "请先分享红包链接!"
                    # destory
                    self._record.destory_record(member)
                    return self.get_max_package(message_str,url)
                return "请分享红包链接!"
        except Exception as e:
            return "请分享红包链接"

    
    def check_phone_number_format(self,phone):
        """
        check phone number format
        :param phone
        :return boolean
        """
        pattern = re.compile('^0?(13[0-9]|14[56789]|15[012356789]|166|17[012345678]|18[0-9]|19[89])[0-9]{8}$')
        if_match = pattern.match(phone)
        if phone:
            return True
        return False

    def get_max_package(self,phone,url):
        data = {"url":url,"mobile":phone}
        res = requests.post('http://101.132.113.122:3007/hongbao',data=data)
        response_json = res.json()
        print(response_json)
        return response_json['message']



class Record(object):
    """
        record the relation of member to url
    """
    @staticmethod
    def record(member,url):
        file_name = str(member)+".txt"
        with open(file_name,'w') as f:
            f.write('{} {}'.format(str(member),url.strip()))

    @staticmethod
    def get_record(member):
        file_name = str(member) + ".txt"
        try:
            with open(file_name,'r') as f:
                member_url = f.read()
                return member_url.split(" ")[1]
        except expression as e:
            return False


    @staticmethod
    def destory_record(member):
        try:
            path = str(member)+".txt"
            os.remove(path)
        except expression as e:
            print(str(e))

