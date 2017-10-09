from django.shortcuts import render


# Create your views here.
def build_comment_data(li):
    dic = {}
    for item in li:
        item['children'] = []
        dic[item['id']] = item
    result = []
    for item in li:
        pid = item['parent_id']
        if pid:
            dic[pid]['children'].append(item)
        else:
            result.append(item)

    return


li = [
    {'id': 1, 'user': '银秋良', 'content': '灌我鸟事', 'parent_id': None},
    {'id': 2, 'user': '银秋良', 'content': '管我鸟事', 'parent_id': None},
    {'id': 3, 'user': '型谱', 'content': '你个文盲', 'parent_id': 1},
    {'id': 4, 'user': '详解', 'content': '好羡慕你们这些没脸的人呀', 'parent_id': 2},
    {'id': 5, 'user': '银秋良', 'content': '你是流氓', 'parent_id': 3},
    {'id': 6, 'user': '银秋良', 'content': '你冷库无情', 'parent_id': 5},
    {'id': 7, 'user': '银秋良', 'content': '你才冷酷无情', 'parent_id': 4},
    {'id': 8, 'user': '银秋良', 'content': '你无理取闹', 'parent_id': 4},
]


def build_comment_tree(com_list):
    com_list = build_comment_data(li)

    html = build_comment_tree(com_list)

    return render(request, 'comment_list.html', ['comment_html':html])


    html = ""

    for item in com_list:
        if not item['children']:
            html += tp1.format(item['user'], item['content'], "")
        else:
            html += tp1.format(item['user'], item['content']
            build_comment_data(item['children']))
