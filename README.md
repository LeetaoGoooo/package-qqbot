# Max Packge

>用qq机器人获取美团和饿了么最大红包

## 功能

1. 分享红包链接到机器人,根据提示输入手机号码

2. 领取最大红包

![](http://ww1.sinaimg.cn/large/006wYWbGly1fowkc0crx3j30bh0cswf3.jpg)

3. 添加聊天机器人

## change

默认情况下关闭聊天功能,启用聊天:

修改<code>core.py</code>中<code>user_package.handle_message_str(xxx,content)</code>为
<code>user_package.handle_message_str(xxx,content,True)</code>

## 说明

由于 smartqq 协议的限制，每次登录成功后的 cookie 会每在 1 ~ 2 天后失效，将被腾讯服务器强制下线，此时<b>必须</b>手工扫码重新登录，因此无法稳定的长期保持在线,详细说明[如何稳定的长期保持在线](https://github.com/pandolia/qqbot/blob/master/faq.md#%E5%A6%82%E4%BD%95%E7%A8%B3%E5%AE%9A%E7%9A%84%E9%95%BF%E6%9C%9F%E4%BF%9D%E6%8C%81%E5%9C%A8%E7%BA%BF)

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
