
 - **企业微信通知（一对一）**

企业微信通知有两种方式，一种是企业微信群机器人（一对多）；一种是企业微信通知（一对一）
企业微信通知是一个应用采用api方法，群通知是采用webhook。
两种方法都是采用相同语法的富文字(markdown)。因此同一个信息能同时发送企业微信通知和群通知。

> **企业微信群机器人（一对多）：**
优点：取得一个webhook就能发送消息，一对多的通知
缺点：得先有三个以上企业微信账号，才能成立聊天群

> **企业微信通知（一对一）：**
优点：有企业微信账号就能建企业微信通知，一对一的通知
缺点：需要取得corpid、AgentID、secret。代码逻辑比较复制
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/bot_demo.png)


这篇代码是介绍**企业微信通知（一对一）**。企业微信群机器人（一对多）请参考[这一篇](https://github.com/litonchen/wx_bot)


 - [ ] **- 企业微信通知**
企业微信通知（一对一）是一个微信企业号的应用，可以当成是一个已经加入对方企业微信的好友，因此能直接发送信息。
企业微信通知（一对一）共需要**企业ID、AgentID、Secret**三组入参
然后更新connect_config.py里面三个入参
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/9.connec_config.png)


 **1. 创建企业**
 
 
首先登入注册一个企业微信，登入[企业微信网页](https://work.weixin.qq.com/)：https://work.weixin.qq.com/
然后按照以下流程。
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/1.newcorp.png)

 **2. 点击应用管理**
![点击应用管理](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/2.application.png?token=GHSAT0AAAAAACAP34VHG6LZBK5DZG5DY2OUZCHP3JQ)

**3.点击创建应用**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/3.create.png)

**4.命名应用**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/4.name.png)

**5.复制(AgentID、Secret)** 
![](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/5.secret.png?token=GHSAT0AAAAAACAP34VGJNMZ5IODBZLDYFDCZCHQN5Q)

**6.企业ID  (corpid)**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/8.corpid.png)
