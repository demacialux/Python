import json

def high_score_record():
    high = 'high_score.json'
    try:
        with open(high) as f_obj:
            high_score = json.load(f_obj)

    except FileNotFoundError:
        high_score = input('最高分：')
        with open(high,'w') as f_obj:
            json.dump(high_score,f_obj)
            print('high_score')

    else:
        print(high_score)

high_score_record()