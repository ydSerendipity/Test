import time
from selenium import webdriver
import re
import requests
from http import cookiejar


def get_g_tk(cookie):

    hashes = 5381
    for letter in cookie['p_skey']:

        hashes += (hashes << 5) + ord(letter)
    return hashes & 0x7fffffff


def login():

    browser = webdriver.Chrome()
    browser.get('https://i.qq.com/')
    browser.maximize_window()
    time.sleep(2)
    browser.switch_to.frame("login_frame")
    browser.find_element_by_id('switcher_plogin').click()
    browser.find_element_by_id('u').clear()
    browser.find_element_by_id("u").send_keys("账号")
    browser.find_element_by_id('p').clear()
    browser.find_element_by_id("p").send_keys("密码")
    browser.find_element_by_id("login_button").click()
    time.sleep(2)
    print("空间登陆成功")
    browser.switch_to.default_content()
    return browser


def back_session(browser):

    my_session = requests.session()
    cooikes = browser.get_cookies()
    cookie = {}
    for elem in cooikes:
        cookie[elem['name']] = elem['value']
    headers = {
        'host': 'h5.qzone.qq.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    c = requests.utils.cookiejar_from_dict(
        cookie, cookiejar=None, overwrite=True)
    my_session.headers = headers
    my_session.cookies.update(c)
    return my_session


def get_qq(my_session, g_tk, qzonetoken):

    url = "https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=1837074495&do=1&rd=0.743191121678668&fupdate=1&clean=1&g_tk=" + \
        str(g_tk) + "&qzonetoken=" + qzonetoken
    res = my_session.get(url)
    friendlist = re.compile('"uin":(.*?),').findall(res.text)
    time.sleep(2)
    return friendlist


def get_message(my_session, qq, g_tk, qzonetoken):

    url = 'https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + str(qq) + '&inCharset=utf-8&outCharset=utf-8&hostUin=' + str(
        qq) + '&notice=0&sort=0&pos=0&num=20&cgi_host=http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6&code_version=1&format=jsonp&need_private_comment=1&g_tk=' + str(g_tk) + '&qzonetoken=' + str(qzonetoken)
    res = my_session.get(url)
    # 说说总数
    num = re.compile('"total":(.*?),').findall(res.text)[0]
    content_list = re.compile(
        '"certified".*?"conlist":(.*?),', re.S).findall(res.text)

    if(len(content_list) == 0):
        print("该好友说说数目为零或者你被禁止查看此好友空间")
        return False

    if int(num) % 20 == 0:
        page = int(num) / 20
    else:
        page = int(num) / 20 + 1

    for i in range(0, int(page)):
        pos = i * 20
        try:
            url = 'https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + str(qq) + '&inCharset=utf-8&outCharset=utf-8&hostUin=' + str(qq) + '&notice=0&sort=0&pos=' + str(
                pos) + '&num=20&cgi_host=http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6&code_version=1&format=jsonp&need_private_comment=1&g_tk=' + str(g_tk) + '&qzonetoken=' + qzonetoken
            res = my_session.get(url)
            content_list = re.compile(
                '"certified".*?"conlist":(.*?),', re.S).findall(res.text)
            time_list = re.compile(
                '"certified".*?"createTime":"(.*?)"', re.S).findall(res.text)
            for c, t in zip(content_list, time_list):
                c = c.replace('[{"con":', '')
                with open("qq_text_1.txt", 'a', encoding='utf-8') as f:
                    f.write(t)
                    f.writelines(c)
                    f.write('\n')
        except Exception as e:
            print("爬取失败")


def main():
    driver = login()
    time.sleep(3)
    html = driver.page_source
    xpat = r'window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)'
    qzonetoken = re.compile(xpat).findall(html)[0]
    cookies = driver.get_cookies()
    cookie = {}
    for elem in cookies:
        cookie[elem['name']] = elem['value']
    g_tk = get_g_tk(cookie)
    my_session = back_session(driver)
    driver.close()
    friendlist = get_qq(my_session, g_tk, qzonetoken)
    # for friend in friendlist:
    #     print(friend)
    # print(len(friendlist))

    for i in range(0, len(friendlist)):

        get_message(my_session, friendlist[i], g_tk, qzonetoken)
        time.sleep(8)


if __name__ == '__main__':
    main()
