import json

def get_number():
    a='number.json'
    try:
        with open(a) as obj:
            number=json.load(obj)
    except FileNotFoundError:
        return None
    else:
        return number

def new_number():
    number=input('请输入一个数字：')
    a='number.json'
    with open(a,'w') as obj:
        json.dump(number,obj)
    return number

def out_number():
    number=get_number()
    if number:
        print('你最喜欢的数字是：'+number)
    else:
        number=new_number()
        print('你最喜欢的数字是：'+number)

out_number()

u=input('dfg')