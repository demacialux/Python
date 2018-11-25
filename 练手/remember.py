import json

name=input('你的名字：')
f='name.json'
with open(f,'w') as obj:
    json.dump(name,obj)
    print(name+'我们将保存你的用户名')