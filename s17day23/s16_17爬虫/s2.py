import requests
from bs4 import BeautifulSoup
#获取token和cookie
r1 = requests.get(url='https://github.com/login')
s1 = BeautifulSoup(r1.text, 'html.parser')
val = s1.find(attrs={'name': 'authenticity_token'}).get('value')
r1_cookie_dict=r1.cookies.get_dict()
#2.发送用户认证
r2 = requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': val,
        'login': 'windfishing5@gmail.com',
        'password': 'Ad177674',
    },
    cookies=r1_cookie_dict
)
r2_cookie_dict = r2.cookies.get_dict()

all_cookie_dict={}
all_cookie_dict.update(r1_cookie_dict)
all_cookie_dict.update(r2_cookie_dict)
#3.访问其他页面
r3=requests.get(
    url='https://github.com/',
    cookies=all_cookie_dict
)
print(r3.text)