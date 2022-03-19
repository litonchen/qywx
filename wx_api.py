import datetime,time,talib,warnings ,xlrd,requests,json
from datetime import timedelta
import pandas as pd
from requests_toolbelt import MultipartEncoder
import connect_config as cc

class wx(object):
    def __init__(self):
        self.agentid = cc.agentid
        self.secret = cc.secret
        self.corpid = cc.corpid
        self.access_token= self.get_token()

    def get_token(self):
        Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        Data = {
            "corpid": self.corpid,
            "corpsecret": self.secret
        }
        r = requests.get(url=Url, params=Data)
        token = r.json()['access_token']
        return token

    def get_media_id(self):
        filepath=self.filepath
        filename=self.filename
        post_file_url = f"https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={self.access_token}&type=file"
        m = MultipartEncoder(
            fields={filename: ('file', open(filepath + filename, 'rb'), 'text/plain')},
        )
        r = requests.post(url=post_file_url, data=m, headers={'Content-Type': m.content_type})
        self.media_id=json.loads(r.text)['media_id']
        return json.loads(r.text)['media_id']

    def sendImg(self,filepath, filename):
        self.filepath =  filepath
        self.filename =  filename
        self.get_media_id()
        data = {
            "touser": "@all",
            "toparty": "@all",
            "msgtype" : "image",
            "agentid" : self.agentid,
            "image": {
                "media_id": self.media_id
            },
            "safe":0
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(self.access_token), data=json.dumps(data))

    def send_txt(self) :
        data = {
            "touser": "@all",
            "toparty": "@all",
            "agentid" : self.agentid,
            "msgtype": "text",  # 消息类型，此时固定为text
            "text": {
                "content": "上海今日天气：32度，大部分多云，降雨概率：10%",  # 文本内容，最长不超过2048个字节，必须是utf8编码
                "mentioned_list":["@all"],  # userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
                "mentioned_mobile_list":["@all"]  # 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
            }
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(self.access_token), data=json.dumps(data))

    def send_markdown(self) :
        send_data = {
            "touser": "@all",
            "toparty": "@all",
            "agentid" : self.agentid,
            "msgtype": "markdown",  # 消息类型，此时固定为markdown
            "markdown": {
                "content": "# **今日交易**<font color=\"warning\">**总结**</font>\n" +  # 标题 （支持1至6级标题，注意#与文字中间要有空格）
                           "#### **浮动盈亏：{}**\n".format("30310 ") +  # 加粗：**需要加粗的字**
                           "> 本日交易：<font color=\"info\"> {} </font> \n".format(" 成交明细 ") +  # 引用：> 需要引用的文字
                           "> 卖出204001，单笔十万：<font color=\"warning\">{} 十万</font> \n".format('10')  +  # 字体颜色(只支持3种内置颜色)
                           "> 卖出131810，单笔千元：<font color=\"warning\">{} 千元</font>".format("5")   # 绿色：info、灰色：comment、橙红：warning
            }
                    }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(self.access_token), data=json.dumps(send_data))

