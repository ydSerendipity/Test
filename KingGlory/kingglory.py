import requests
# import os
# from urllib.request import urlretrieve

# 右上方有个get请求,将get后的网址赋给heros_url
heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90001a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=F6DFAFC3BED1C29825EC8D404110F5C5&ovr=7.0&device=HUAWEI_HUAWEI+CAZ-TL10&net_type=1&client_id=&info_ms=&info_ma=hoeVma%2BgYmXjgZG7TVJzaoLyRRILGMIaVltuIflvZFE%3D&mno=0&info_la=mh%2FAbS1DsM0kM7IDlFIbYQ%3D%3D&info_ci=mh%2FAbS1DsM0kM7IDlFIbYQ%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=zRqQJG5mLlFy6mYG4YA%2BE0UcqUCBAXmZcXNHROzwWy8%3D&os_level=24&os_id=c0be30adbd11c768&resolution=1080_1788&dpi=480&client_ip=192.168.2.114&pdunid=WWUDU16A29002522"

#将图片保存到文件夹
# def imgs_download(heros_url, headers):
#     res = requests.get(url=heros_url, headers=headers).json()
#     hero_path = "heros_img"
#     for hero in res['list']:
#         img_url = hero['cover']
#         hero_name = hero['name'] + ".png"
#         filename = hero_path + "/" + hero_name
#         if hero_path not in os.listdir():
#             os.makedirs(hero_path)
#         urlretrieve(url=img_url, filename=filename)


def hero_info(heros_url, headers):
    res = requests.get(url=heros_url, headers=headers).json()
    for hero in res['list']:
        id = hero['hero_id']
        info_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id=" + id + "&channel_id=90001a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=F6DFAFC3BED1C29825EC8D404110F5C5&ovr=7.0&device=HUAWEI_HUAWEI+CAZ-TL10&net_type=1&client_id=UTAH2jTRdl%2FfxnOjEiOS4A%3D%3D&info_ms=%2BpdbZccbIPeH%2BTpoBwY0gw%3D%3D&info_ma=hoeVma%2BgYmXjgZG7TVJzaoLyRRILGMIaVltuIflvZFE%3D&mno=0&info_la=mh%2FAbS1DsM0kM7IDlFIbYQ%3D%3D&info_ci=mh%2FAbS1DsM0kM7IDlFIbYQ%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=zRqQJG5mLlFy6mYG4YA%2BE0UcqUCBAXmZcXNHROzwWy8%3D&os_level=24&os_id=c0be30adbd11c768&resolution=1080_1788&dpi=480&client_ip=192.168.2.114&pdunid=WWUDU16A29002522"
        res = requests.get(url=info_url, headers=headers).json()
        print(hero['name'] + " : ")
        print("历史上的他/她 : " + res['info']['history_intro'])
        print("背景故事 : " + res['info']['background_story'])
        print("对抗技巧 : " + res['info']['hero_tips'])
        print("团战思想 : " + res['info']['melee_tips'] + "\n")


def main():
    headers = {
        # 将Fiddler右上方的内容填在headers中
        "Accept-Charset": "UTF-8",
        "Accept-Encoding": "gzip,deflate",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; HUAWEI CAZ-TL10 Build/HUAWEICAZ-TL10)",
        "X-Requested-With": "XMLHttpRequest",
        "Content-type": "application/x-www-form-urlencoded",
        "Connection": "Keep-Alive",
        "Host": "gamehelper.gm825.com"
    }
    # 英雄的列表显示在json格式下
    # res = requests.get(url=heros_url, headers=headers).json()
    # 打印列表
    # print(res['list'])
    # 计算有多少个英雄
    # print(len(res['list']))
    # imgs_download(heros_url, headers)
    hero_info(heros_url, headers)


if __name__ == "__main__":
    main()
