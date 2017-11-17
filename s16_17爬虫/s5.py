from bs4 import BeautifulSoup

html_doc="""
<html><head><title>The dormouse's story</title></head>
<body>
888
    <div class='c1'>
         <p class='c2'>
            </p>
              <div id='i1'>
            <a>link</a>
        
        </div>
    </div>
</body>
</html>
"""
from bs4.element import Tag
soup=BeautifulSoup(html_doc,features="html.parser")
tags=soup.find(attrs={'class':'c2'})
tag=Tag(name='i',attrs={'id':'it'})
tag.string='asdfg'
print(tag)
import copy
new_copy=copy.deepcopy(tags)
soup.find(id='i1').append(tag)
print(soup)
#
#  print(tags.text)
# print(list(tags.stripped_strings))
# for item in tags.children:
#     print('item is:',item,type(item))
# tags.string='12233'
# print(tags)
# print(tags.previous)
# print(list(tags.previous_elements))
# print(tags.previous_sibling)
# print(tags.previous_siblings)

# for tag in tags:
#     print(tag.name)
#2attrs
# soup=BeautifulSoup(html_doc,features="html.parser")
# tag=soup.find(class_='c1') #id不用写
# # print(tag.attrs)
# tag.attrs['id']=1
# del tag.attrs['class']
# # print(tag)
# # print(soup)
# # print(tag.children)
# # print(list(tag.children))
# # print(list(tag.descendants))
# # print(tag.find_all(recursive=False))
#
# # tag.clear()
# # print(soup)
# # v=tag.extract()
# # print('v is :',v)
# # print(soup)
# #
# # print('tag is :',tag,type(tag))
# # print(tag.decode())
# # print(tag.encode())
# # print(tag.decode_contents())
# # from bs4.element import Tag
# # Tag.get_text()
# # Tag.text()
# # tag.text
# # tag.get_text('id')
#
#
#
#
#
