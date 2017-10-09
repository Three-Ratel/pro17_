li = [
    {'user': 'xxx', 'pwd': 'xxx', 'id': 1, "children": [], 'parent_id': None},
    {'user': 'xxx', 'pwd': 'xxx', 'id': 2, "children": [], 'parent_id': None},
    {'user': 'xxx', 'pwd': 'xxx', 'id': 3, "children": [], 'parent_id': 1},
    {'user': 'xxx', 'pwd': 'xxx', 'id': 4, "children": [], 'parent_id': 2},
    {'user': 'xxx', 'pwd': 'xxx', 'id': 5, "children": [], 'parent_id': 1},
    {'user': 'xxx', 'pwd': 'xxx', 'id': 6, "children": [], 'parent_id': 3},
]
# result = [
#     {'user':'xxx','pwd':'xxx','id':1,"children":[{'user':'xxx','pwd':'xxx','id':3,"children":[ {'user':'xxx','pwd':'xxx','id':6,"children":[],'parent_id':3},],'parent_id':1},{'user':'xxx','pwd':'xxx','id':5,"children":[],'parent_id':1},],'parent_id':None},
#     {'user':'xxx','pwd':'xxx','id':2,"children":[{'user':'xxx','pwd':'xxx','id':4,"children":[],'parent_id':2},],'parent_id':None},
# ]
dic = {}
for item in li:
    dic[item['id']] = item
# print(dic)

# 此时dic内容为:{1: {'user': 'xxx', 'pwd': 'xxx', 'id': 1, 'children': [], 'parent_id': None}, 2: {'user': 'xxx', 'pwd': 'xxx', 'id': 2, 'children': [], 'parent_id': None}, 3: {'user': 'xxx', 'pwd': 'xxx', 'id': 3, 'children': [], 'parent_id': 1}, 4: {'user': 'xxx', 'pwd': 'xxx', 'id': 4, 'children': [], 'parent_id': 2}, 5: {'user': 'xxx', 'pwd': 'xxx', 'id': 5, 'children': [], 'parent_id': 1}, 6: {'user': 'xxx', 'pwd': 'xxx', 'id': 6, 'children': [], 'parent_id': 3}}


for k, v in dic.items():
# print(dic[v])
#     print(k, v)
    flag=bool(v['parent_id'])
    if flag: #取出所有子元素
        parent=dic[v['parent_id']]
        dic[v['parent_id']]['children']=v
    # print (v['children'])
        # if parent['parent_id']:
        #     print(parent)
# print(dic)
for k,v in dic.items():
    flag=v['children']
    if flag:
        print(v)
        p_flag=v['parent_id']
        print(p_flag)
        lis=[]
        if p_flag:
            # lis.append(v)
            dic[p_flag]['children']=v

print('终极dic内容是',dic)
result=[]
for k,v in dic.items():
    print('列表的元素',v)
    if not v['parent_id']:
        result.append(v)
print('result内容是',result)

for i in result:
    print('内容',i)
# flag=bool(v['parent_id'])
# if flag:#取出所有children
#     partent=dic[flag]
#     print(partent)

# for item in li:
#     flag = bool( item['parent_id'])
#     if flag:#取出所有children
#         parent=li[item['parent_id'] - 1] #parent
#         # print(item)
#         # print(parent)
#         if parent['parent_id'] != None:#父级的parent不为None 即是第六条结果
#             print(parent)
#             parent['children']=item         #
