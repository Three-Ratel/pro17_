import requests
from bs4 import BeautifulSoup
#模拟首次打开
r0 = requests.get(
    url='http://dig.chouti.com/'
)
r0_cookie_dict = r0.cookies.get_dict()

#登陆请求
r1 = requests.post(
    url='http://dig.chouti.com/login',
    data={
        'phone': '86' + '15652625974',
        'password': 'Ad177674',
        'oneMonth': 1,

    },
    cookies = r0_cookie_dict
)
print(r1.text)
r1_cookie_dict=r1.cookies.get_dict()


#点赞请求
r2=requests.post(
    url='http://dig.chouti.com/link/vote?linksId=14796866',
    cookies=r0_cookie_dict
)
