# coding=utf-8
import json
import requests


def send_message_text(SESSDATA: str, token: str, sender: int, receiver: int, content: str):
    """
    发送文字私信
    :param SESSDATA: 登录token，可在cookies获取
    :param token: 私信验证token，可在cookies-bili_jct获取
    :param sender: 发送者uid
    :param receiver: 收信者uid
    :param content: 文字内容
    :return: 为空
    """
    try:
        data = requests.post(url="http://api.vc.bilibili.com/web_im/v1/web_im/send_msg",
                             cookies={"SESSDATA": SESSDATA},
                             data={
                                 "msg[sender_uid]": sender,
                                 "msg[receiver_id]": receiver,
                                 "msg[receiver_type]": 1,
                                 "msg[msg_type]": 1,
                                 "msg[content]": json.dumps({"content": content}),
                                 "csrf_token": token
                             })
        if json.loads(data.text)["msg"] != "ok":
            print("Some things went wrong. Check data.")
            print(data.text)
    except Exception as e:
        print(e)
