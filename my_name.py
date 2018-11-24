class Anonymous():
    """收集匿名调查问卷的答案"""

    def __init__(self,a_question):
        """存储一个问题，并为存储答案做准备"""
        self.question = a_question
        self.responses = []
    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_re(self,new_re):
        """存储单份调查问卷的回复"""
        self.responses.append(new_re)

    def show(self):
        """显示收集到的所有答卷"""
        print('调查结果：')
        for a in self.responses:
            print(a)

question = '你喜欢哪个城市？'
my_survey = Anonymous(question)

my_survey.show_question()  #显示问题
print('按q退出')
while True:
    response = input('城市：')
    if response == 'q':
        break
    my_survey.store_re(response)  #存储答案

my_survey.show()  #显示调查结果