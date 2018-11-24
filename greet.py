import json

f='name.json'
with open(f) as obj:
    name=json.load(obj)
    print('欢迎回来！'+name)
    print('GitHub测试')
    print('再来一行')
