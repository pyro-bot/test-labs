import unittest
from calc import factorial, div, minus
import threading as th

buf = {}


class uTest(unittest.TestCase):

    # Work Test
    # ================================================================================
    def test_work_1_test(self):
        global buf
        buf['fact'] = factorial(5)
        self.assertEqual(factorial(5), 120, 'Функция работает не правильно')

    def test_work_2_div(self):
        global buf
        buf['div'] = div(buf['fact'], 2)
        self.assertEqual(buf['div'], 60, 'Деление не работает')

    def test_work_3_minus(self):
        global buf
        buf['minus'] = minus(buf['div'], 10)
        self.assertEqual(buf['minus'], 50, 'Вычетание не работает')
    # =================================================================================

# Tests Div function
# ============================================================================
    def test_div_type(self):
        with self.assertRaises(TypeError):
            div('asdasd', 10)
            div(10, 'adsas')

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_div_long(self):
        try:
            div(10**20, 10**20)
        except:
            self.fail('Функция не умеет работать с большими числами')
# ==============================================================================

# Tests function Minus
# ====================================================================================
    def test_minus_type(self):
        with self.assertRaises(TypeError):
            minus('asdasd', 10)
            minus(10, 'adsas')

    def test_minus_long(self):
        try:
            minus(10**20, 10**20)
        except:
            self.fail('Функция не умеет работать с большими числами')
# ====================================================================================

# Tests factorial
# ========================================================================================
    def test_to_string(self):
        with self.assertRaises(TypeError):
            factorial('a')

    def test_big_integer(self):
        try:
            factorial(100000)
        except:
            self.fail('Функция ну умеет работать с большими числами')

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_less_zero(self):
        self.assertEqual(factorial(-10), 1)

    def test_only_int(self):
        with self.assertRaises(TypeError):
            factorial(5.5)
# ========================================================================================


if __name__ == '__main__':
    unittest.main()
