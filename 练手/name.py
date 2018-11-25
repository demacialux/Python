import unittest
from survey import Anonymous

class TestAnonyous(unittest.TestCase):
    """针对Anonyous类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供测试方法使用"""
        question = '你喜欢哪个城市？'
        self.my_survey = Anonymous(question)
        self.responses = ['杭州','扬州','广州']

    def test_store_single(self):
        """测试单个答案是否会被存储"""
        self.my_survey.store_re(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three(self):
        """测试三个答案是否会被存储"""
        for response in self.responses:
            self.my_survey.store_re(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
print('12345678')