import unittest
from factorial import factorial

class uTest(unittest.TestCase):

    def test_work_test(self):
        self.assertEqual(factorial(2),2,'Функция работает не правильно')
    
    def test_to_string(self):
        with self.assertRaises(TypeError):
            factorial('a')

    def test_big_integer(self):
        try:
            factorial(100000)
        except:
            self.fail('Функция ну умеет работать с большими числами')
    def test_zero(self):
        self.assertEqual(factorial(0),1)

    def test_less_zero(self):
        self.assertEqual(factorial(-10),1)
    
    def test_time(self):
        import threading as th
        thred=th.Thread(target=factorial,args=(100000,))
        thred.start()
        thred.join(5)
        if thred.isAlive():
            del thred
            self.fail('Время выполнения больше 5 сек')

    


if __name__=='__main__':
    unittest.main()