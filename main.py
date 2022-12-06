import datetime
import time
from urllib.parse import quote
import string
import urllib
import json, requests
from bs4 import BeautifulSoup
import random
import socket
import subprocess
filepath="go-cqhttp.bat"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
def get_group(id):
    response = requests.post('http://127.0.0.1:5700/get_group_member_list?group_id='+str(id)).json()
    for i in response['data']:
        if(i['card']!=''):
            print(i['card']+str(i['user_id']))
        else:
            print(i['nickname']+str(i['user_id']))
def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    msg_type = resp_dict['msg_type']  # 回复类型（群聊/私聊）
    number = resp_dict['number']  # 回复账号（群号/好友号）|
    msg = resp_dict['msg']  # 要回复的消息

    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0
def request_to_json(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="\n":
            return json.loads(msg[i:])
    return None

#需要循环执行，返回值为json格式
def rev_msg():# json or None
    Client, Address = ListenSocket.accept()
    Request = Client.recv(1024).decode(encoding='utf-8')
    rev_json=request_to_json(Request)
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json
def get_img_random():
    for j in [0,24,48,72]:
        # 获取网站数据
        url = requests.get('https://www.duitang.com/search/?kw=美女&type=feed&start={}'.format(j))
        # url.encoding = 'utf-8'  #如果需要用到页面中的汉字内容，则需要进行解码，否则中文会出现乱码
        html = url.text
        # 解析网页
        soup = BeautifulSoup(html, 'html.parser')
        # 获取所有的img标签
        movie = soup.find_all('div', class_='mbpho')
        # print(movie)
        # 获取src路径
        for i in movie:
            imgsrc = i.find_all('img')[0].get('src')
            img_list.append(imgsrc)
    return img_list
def birthday_book(birthday,key):
    url = "http://apis.juhe.cn/fapig/birthdayBook/query?" + 'keyword={}&key=72b3f19d5229375977331e62f4f72568'.format(birthday)
    # 发送get请求
    r = requests.get(url)
#     print(r)
    # 获取返回的json数据
    result = r.json()['result'][key].replace('<p>','').replace('</p>','')
#     print(result)
    return result
def chat(rev):
        try:
            if(0<=now.hour<=6):
                if rev["message_type"] == "private": #私聊
                    qq = rev['sender']['user_id']
                    if(qq==286913237):
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '趁凡哥还没发现航宝快睡觉，如果室友打呼，简繁现在做法让她做噩梦惊醒'})
                        send_msg({'msg_type': 'private', 'number': qq, 'msg':'[CQ:poke,qq={}]'.format(qq)})
                    else:
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '凡哥已经睡觉了，简繁祝你早点休息，嘿嘿'})
                        send_msg({'msg_type': 'private', 'number': qq, 'msg':'[CQ:poke,qq={}]'.format(qq)})
            elif(6<now.hour<=8):
                if rev["message_type"] == "private": #私聊
                    qq = rev['sender']['user_id']
                    if(qq==286913237):
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '凡哥正在和梦里的航宝再见，航宝再等等吧'})
                        send_msg({'msg_type': 'private', 'number': qq, 'msg':'[CQ:poke,qq={}]'.format(qq)})
                    else:
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '凡哥还在睡觉，简繁正在努力叫他起床'})
                        send_msg({'msg_type': 'private', 'number': qq, 'msg':'[CQ:poke,qq={}]'.format(qq)})
            elif rev["message_type"] == "private": #私聊
    #             print(rev['raw_message'])
                if '爆照' in rev['raw_message']:
                    i = random.randint(0, len(img_list))
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:image,file={},type=flash,id=40004]'.format(get_img_random()[i])})
                elif rev['raw_message']=='凡凡':
                    qq = rev['sender']['user_id']
                    if (qq == 286913237):
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '简繁代凡凡陪航宝宝一会，我们聊天吧'})
                    else:
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '凡凡的昵称只属于航宝'})
                elif rev['raw_message']=='凡宝':
                    qq = rev['sender']['user_id']
                    if (qq == 286913237):
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '是的是的，你也是我的航宝'})
                    else:
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '我是航航的宝'})
                elif rev['raw_message']=='老公':
                    qq = rev['sender']['user_id']
                    if (qq == 286913237):
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '简繁代凡哥称呼老婆，因为凡哥的粗心，简繁代他陪航宝一会'})
                    else:
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '简繁表示，以后叫凡哥'})
                elif rev['raw_message']=='宝贝':
                    qq = rev['sender']['user_id']
                    if (qq == 286913237):
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '简繁觉得，你也是凡哥心中独一无二的宝贝，凡哥最喜欢航宝了'})
                    else:
                        send_msg({'msg_type': 'private', 'number': qq, 'msg': '凡哥这么帅当然人人都喜欢啦'})
                elif rev['raw_message']=='在吗':
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type':'private','number':qq,'msg':'我在'})
                elif rev['raw_message']=='宝宝':
                    qq = rev['sender']['user_id']
                    if(qq==286913237):
                        send_msg({'msg_type':'private','number':qq,'msg':'宝宝'})
                    else:
                        send_msg({'msg_type':'private','number':qq,'msg':'你的宝宝不是我'})
                else:
                    message = rev['raw_message']
    #                 url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + message
                    url = 'https://v.api.aa1.cn/api/api-xiaoai/talk.php?msg='+message+'&type=text'
                    s = quote(url, safe=string.printable)
                    with urllib.request.urlopen(s) as response:
                        html = response.read()
                        qq = rev['sender']['user_id']
    #                   send_msg({'msg_type': 'private', 'number': qq,'msg': eval(html.decode("utf-8"))["content"].replace('{br}', '\n')})
                        send_msg({'msg_type': 'private', 'number': qq,'msg': html.decode("utf-8")})

        except:
            qq = rev['sender']['user_id']
            send_msg({'msg_type': 'private', 'number': qq, 'msg': '暂未支持'})
def birthday(str):
    dict={'性格':'nature','爱情':'love','财运':'money','事业':'business','健康':'health','幸运数字':'lucky_num','适合的恋爱对象':'in_love','适合的朋友对象':'friend'}
    str_list = str.split(' ')
#     print(str_list[0])
    key = str_list[1]
    result = birthday_book(str_list[0],dict[key])
    return result


ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1', 5701))
ListenSocket.listen(100)

HttpResponseHeader = '''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
'''

# 将获取到的响应内容进行解码，并将json字符串内容转换为python字典格式
# 通过下标取到机器人回复的内容

img_list = []
flag = 0
while (1):
    now = datetime.datetime.now()
    rev = rev_msg()
    if rev["post_type"] == "message":
        if (flag):
            try:
                qq = rev['sender']['user_id']
                print(rev['raw_message'])

                send_msg({'msg_type': 'private', 'number': qq, 'msg': birthday(rev['raw_message'])})
                flag = 0
            except:
                qq = rev['sender']['user_id']
                send_msg({'msg_type': 'private', 'number': qq,
                          'msg': '你的输入格式可能有错误，不然为啥没有结果，简繁需要像这样的输入2001-10-20 性格'})

        elif rev['raw_message'] == "生日书":
            qq = rev['sender']['user_id']
            send_msg({'msg_type': 'private', 'number': qq,
                      'msg': '请输入你的生日以及想要咨询的内容,空格隔开，输入格式："2001-10-20性格"，咨询内容包括：性格,爱情,财运,事业,健康,幸运数字,适合的恋爱对象,适合的朋友对象'})
            flag = 1
        else:
            chat(rev)
    #     else:
    #         continue
    elif (now.hour == 0 and now.minute == 10):

        send_msg({'msg_type': 'private', 'number': 657407891, 'msg': '晚安！'})
        send_msg({'msg_type': 'private', 'number': 657407891, 'msg': '[CQ:poke,qq={}]'.format(657407891)})
        send_msg({'msg_type': 'private', 'number': 286913237, 'msg': '晚安！'})
        send_msg({'msg_type': 'private', 'number': 286913237, 'msg': '[CQ:poke,qq={}]'.format(286913237)})
        time.sleep(60)
        continue
    elif (now.hour == 8 and now.minute == 30):

        send_msg({'msg_type': 'private', 'number': 286913237, 'msg': '起床了！'})
        send_msg({'msg_type': 'private', 'number': 286913237, 'msg': '[CQ:poke,qq={}]'.format(286913237)})
        send_msg({'msg_type': 'private', 'number': 657407891, 'msg': '起床了'})
        send_msg({'msg_type': 'private', 'number': 657407891, 'msg': '[CQ:poke,qq={}]'.format(657407891)})
        time.sleep(60)
        continue
    elif (now.hour == 1 and now.minute == 0):
        send_msg({'msg_type': 'private', 'number': 657407891, 'msg': '早点休息！'})
        send_msg({'msg_type': 'private', 'number': 657407891, 'msg': '[CQ:poke,qq={}]'.format(286913237)})
        time.sleep(60)
    else:
        continue

