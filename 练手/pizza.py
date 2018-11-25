import json

def get_name():
    f='name.json'
    try:
        with open(f) as obj:
            name=json.load(obj)
    except FileNotFoundError:
        return None
    else:
        return name

def earn_name():
    name=input('请输入你的用户名：')
    f='name.json'
    with open(f,'w') as obj:
        json.dump(name.obj)
    return name

def out_name():
    name=get_name()
    if name:
        print('欢迎回来，'+name)
    else:
        name=earn()
        print('系统将会保存你的账户，'+name)

out_name()

input()