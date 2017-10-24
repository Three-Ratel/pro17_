import requests
from bs4 import BeautifulSoup

response=requests.get('http://www.autohome.com.cn/news/')
# print(response.text)
# with open('autohome_news','wb') as f:
#     f.write(response.content)
with open('autohome_new_txt','r',encoding='utf-8') as f:
    data=f.read()
# print(data)

soup=BeautifulSoup(data,'html.parser')
tag=soup.find(name='div',attrs={'id':'auto-channel-lazyload-article'})
# print(tag)
li_list=tag.find_all('li')
# print(li_list[0].find(name='h3').text)  #获取到标题对象  .text获取对象中的文本
for li in li_list:
    h3=li.find(name='h3')
    if not h3:
        continue
    print(h3.text)
    a_tag=li.find(name='a').get('href')   #.get获取对象的属性名对应的值
    # attrs_tag=li.find(name='a').attrs['href'] #效果同上
    print(a_tag)
    print(li.find('p').text)
    img_usl=li.find('img').get('src')
    print(img_usl)
    res=requests.get('http:'+img_usl)
    with open ('xxx.jpg','wb') as f:
        f.write(res.content)