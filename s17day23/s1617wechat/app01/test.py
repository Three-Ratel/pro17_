import re

msg = """window.QRLogin.code = 200; window.QRLogin.uuid = "gc8KHu2Yng==";"""
data = re.findall('uuid = "(.*)";', msg)
print(data[0])