if __name__=="__main__":
    import wx_api
    from wx_api import wx
    wx_push=wx()
    wx_push.send_txt()
    wx_push.sendImg('./','bullbear.jpeg')
    wx_push.send_markdown()
