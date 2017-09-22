import  hashlib

def encrypt(pwd):
    import hashlib
    obj = hashlib.md5()
    obj.update('123'.encode('utf-8'))
    data = obj.hexdigest()
    print(data)
    return data