# Max Packge

>用qq机器人获取美团和饿了么最大红包

## 功能

1. 分享红包链接到机器人,根据提示输入手机号码

2. 领取最大红包

![](http://ww1.sinaimg.cn/large/006wYWbGly1fowkc0crx3j30bh0cswf3.jpg)

3. 添加聊天机器人

## change

默认情况下关闭聊天功能,启用聊天:

修改<code>core.py</code>中<code>user_package.handle_message_str(member.name,content)</code>为
<code>user_package.handle_message_str(member.name,content,True)</code>

## 环境

python3.6


## 运行

修改<code>chat.py</code>中的<code>apiKey</code>[可选]

```bash
pip install -r requirements.txt
python core.py
```

## 感谢

感谢[zhuweiyou](https://github.com/zhuweiyou) 分享的抢红包接口
[game-helper/hongbao](https://github.com/game-helper/hongbao)
