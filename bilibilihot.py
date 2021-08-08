# coding=utf-8
"""
从土味情话中获取每日一句。
https://api.bilibili.com/x/web-interface/ranking/v2?rid=129&type=all
https://api.bilibili.com/x/web-interface/ranking/v2?rid=119&type=all
 """
import requests
import json
from urllib import parse
import math

def BvToAv(Bv):
    # 1.去除Bv号前的"Bv"字符
    BvNo1 = Bv[2:]
    keys = {
        '1': '13', '2': '12', '3': '46', '4': '31', '5': '43', '6': '18', '7': '40', '8': '28', '9': '5',
        'A': '54', 'B': '20', 'C': '15', 'D': '8', 'E': '39', 'F': '57', 'G': '45', 'H': '36', 'J': '38', 'K': '51',
        'L': '42', 'M': '49', 'N': '52', 'P': '53', 'Q': '7', 'R': '4', 'S': '9', 'T': '50', 'U': '10', 'V': '44',
        'W': '34', 'X': '6', 'Y': '25', 'Z': '1',
        'a': '26', 'b': '29', 'c': '56', 'd': '3', 'e': '24', 'f': '0', 'g': '47', 'h': '27', 'i': '22', 'j': '41',
        'k': '16', 'm': '11', 'n': '37', 'o': '2',
        'p': '35', 'q': '21', 'r': '17', 's': '33', 't': '30', 'u': '48', 'v': '23', 'w': '55', 'x': '32', 'y': '14',
        'z': '19'

    }
    # 2. 将key对应的value存入一个列表
    BvNo2 = []
    for index, ch in enumerate(BvNo1):
        BvNo2.append(int(str(keys[ch])))

    # 3. 对列表中不同位置的数进行*58的x次方的操作

    BvNo2[0] = int(BvNo2[0] * math.pow(58, 6))
    BvNo2[1] = int(BvNo2[1] * math.pow(58, 2))
    BvNo2[2] = int(BvNo2[2] * math.pow(58, 4))
    BvNo2[3] = int(BvNo2[3] * math.pow(58, 8))
    BvNo2[4] = int(BvNo2[4] * math.pow(58, 5))
    BvNo2[5] = int(BvNo2[5] * math.pow(58, 9))
    BvNo2[6] = int(BvNo2[6] * math.pow(58, 3))
    BvNo2[7] = int(BvNo2[7] * math.pow(58, 7))
    BvNo2[8] = int(BvNo2[8] * math.pow(58, 1))
    BvNo2[9] = int(BvNo2[9] * math.pow(58, 0))

    # 4.求出这10个数的合
    sum = 0
    for i in BvNo2:
        sum += i
    # 5. 将和减去100618342136696320
    sum -= 100618342136696320
    # 6. 将sum 与177451812进行异或
    temp = 177451812

    return sum ^ temp

# __all__ = ['get_bilibili_info']
htt=f'h'.lower()+'ttps://www.bilibili.com/video/av'

# httpp=str(htt.lower())
# httpp2=httpp.lower()

# 科技
def get_bilibili_info():

    print('获取...')
    try:
        resp = requests.get('https://api.bilibili.com/x/web-interface/ranking/v2?rid=188&type=all')
        if resp.status_code == 200:
            content_dict = resp.json()


            data = content_dict.get("data").get("list")
            result1 = []
            srt22=""
            for i in data:
                result1.append("|"+i.get("title")+"|"+"UP主：@"+i.get("owner").get("name")+">>>"+htt+str(BvToAv(i.get("bvid"))))

            for player in result1[:10]:
                msgg = str(result1.index(player)+1)+'' + player.title() + "\n\n"

                srt22 = srt22 + msgg.lower()
            return srt22


            # for i in result1:
            #
            #
            #  print(result1.index(i) + 1, i)


        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


# 知识
def get_bilibili_zs():

    print('获取...')
    try:
        resp = requests.get('https://api.bilibili.com/x/web-interface/ranking/v2?rid=36&type=all')
        if resp.status_code == 200:
            content_dict = resp.json()


            data = content_dict.get("data").get("list")
            result1 = []
            srt22=""
            for i in data:
                result1.append("|"+i.get("title")+"|"+"UP主：@"+i.get("owner").get("name")+">>>"+htt+str(BvToAv(i.get("bvid"))))

            for player in result1[:10]:
                msgg = str(result1.index(player)+1)+'' + player.title() + "\n\n"

                srt22 = srt22 + msgg.lower()
            return srt22


            # for i in result1:
            #
            #
            #  print(result1.index(i) + 1, i)


        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


# 舞蹈
def get_bilibili_wd():

    print('获取...')
    try:
        resp = requests.get('https://api.bilibili.com/x/web-interface/ranking/v2?rid=129&type=all')
        if resp.status_code == 200:
            content_dict = resp.json()


            data = content_dict.get("data").get("list")
            result1 = []
            srt22=""
            for i in data:
                result1.append("|"+i.get("title")+"|"+"UP主：@"+i.get("owner").get("name")+">>>"+htt+str(BvToAv(i.get("bvid"))))

            for player in result1[:10]:
                msgg = str(result1.index(player)+1)+'' + player.title() + "\n\n"

                srt22 = srt22 + msgg.lower()
            return srt22


            # for i in result1:
            #
            #
            #  print(result1.index(i) + 1, i)


        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


# 鬼畜
def get_bilibili_gc():

    print('获取...')
    try:
        resp = requests.get('https://api.bilibili.com/x/web-interface/ranking/v2?rid=119&type=all')
        if resp.status_code == 200:
            content_dict = resp.json()


            data = content_dict.get("data").get("list")
            result1 = []
            srt22=""
            for i in data:
                result1.append("|"+i.get("title")+"|"+"UP主：@"+i.get("owner").get("name")+">>>"+htt+str(BvToAv(i.get("bvid"))))

            for player in result1[:10]:
                msgg = str(result1.index(player)+1)+'' + player.title() + "\n\n"

                srt22 = srt22 + msgg.lower()
            return srt22


            # for i in result1:
            #
            #
            #  print(result1.index(i) + 1, i)


        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None




if __name__ == '__main__':

    is_tomorrow =get_bilibili_info()
    url = 'https://service-etcne5bg-1254304775.gz.apigw.tencentcs.com/release/Wecom_push'
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    # 'application/x-www-form-urlencoded'
    # 'application/json;charset=utf-8'
    FormData={
    'sendkey': 'akb48',
    'msg_type': 'text',
    'msg': is_tomorrow

}

    res = requests.post(url=url, json=FormData)
    # content = requests.post(url=url, data=FormData).text

    print(res.text)


    print(is_tomorrow)
