import unittest
from main import calc


class TestCalcFunction(unittest.TestCase):

    def test_valid_input(self):
        # Тест с корректными значениями
        result = calc(credit=100000, years=5, procent=10)
        # Пример ожидаемого ежемесячного платежа
        expected_monthly_payment = 2125
        # Пример ожидаемой переплаты
        expected_overpayment = 27482
        self.assertEqual(
            result,
            ["ежемесячный платёж", expected_monthly_payment,
            "переплата", expected_overpayment]
        )

    def test_invalid_credit(self):
        # Тест с некорректным значением кредита
        with self.assertRaises(ValueError) as context:
            calc(-100, 5, 10)
        self.assertEqual(str(context.exception), "Некорректный размер данных")

        with self.assertRaises(ValueError) as context:
            calc("100000", 5, 10)
        self.assertEqual(str(context.exception), "Некорректный тип данных")

    def test_invalid_years(self):
        # Тест с некорректным значением срока кредита
        with self.assertRaises(ValueError) as context:
            calc(100000, -5, 10)
        self.assertEqual(str(context.exception), "Некорректный размер данных")

        with self.assertRaises(ValueError) as context:
            calc(100000, "five", 10)
        self.assertEqual(str(context.exception), "Некорректный тип данных")

    def test_invalid_procent(self):
        # Тест с некорректным значением процента
        with self.assertRaises(ValueError) as context:
            calc(100000, 5, -15)
        self.assertEqual(str(context.exception), "Некорректный размер данных")

        with self.assertRaises(ValueError) as context:
            calc(100000, 5, "ten")
        self.assertEqual(str(context.exception), "Некорректный тип данных")
