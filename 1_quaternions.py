# Задача 2.1. Кватернионы
import unittest



class Quaternion:
    """
    Класс для представления и работы с кватернионами.

    Атрибуты:
    :param w: действителоьная часть кватерниона
    :param x: первая мнимая компонента кватерниона
    :param y: вторая мнимая компонента кватерниона
    :param z: третья мнимая компонента кватерниона
    """

    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """
        Сложение двух кватернионов.

        :param other: кватернион для сложения
        :return: результат сложения в виде нового кватерниона
        """
        return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Вычитание двух кватернионов.

        :param other: кватернион для вычитания
        :return: результат вычитания в виде нового кватерниона
        """
        return Quaternion(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """
        Умножение двух кватернионов или умножение кватерниона на скаляр.

        :param other: кватернион или скаляр для умножения
        :return: результат умножения в виде нового кватерниона
        """
        if isinstance(other, Quaternion):
            w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
            z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
            return Quaternion(w, x, y, z)
        elif isinstance(other, (int, float)):
            return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Умножение возможно только с кватернионом или скаляром.")

    def conjugate(self):
        """
        Вычисление сопряженного кватерниона.

        :return: сопряженный кватернион
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm(self):
        """
        Вычисление нормы (модуля) кватерниона.

        :return: норма кватерниона
        """
        return (self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __truediv__(self, other):
        """
        Деление двух кватернионов.

        :param other: кватернион для деления
        :return: результат деления в виде нового кватерниона
        """
        conj = other.conjugate()
        norm_sq = other.norm() ** 2
        return self * conj * (1.0 / norm_sq)

    def scalar_mul(self, other):
        """
        Скалярное умножение двух кватернионов.

        :param other: кватернион для скалярного умножения
        :return: результат скалярного умножения
        """
        return self.w * other.w + self.x * other.x + self.y * other.y + self.z * other.z

    def rotate_vector(self, vector):
        """
        Поворот вектора в пространстве с использованием кватерниона.

        :param vector: вектор (x, y, z) для поворота
        :return: перевернутый (или повёрнутый) вектор
        """
        q_vector = Quaternion(0, *vector)
        rotated_vector = self * q_vector * self.conjugate()
        return rotated_vector.x, rotated_vector.y, rotated_vector.z



class TestQuaternion(unittest.TestCase):
    def setUp(self):
        self.q1 = Quaternion(1, 2, 3, 4)
        self.q2 = Quaternion(5, 6, 7, 8)
        self.scalar = 2
        self.vector = (1, 0, 0)

    def test_addition(self):
        result = self.q1 + self.q2
        self.assertEqual(result.w, 6)
        self.assertEqual(result.x, 8)
        self.assertEqual(result.y, 10)
        self.assertEqual(result.z, 12)

    def test_subtraction(self):
        result = self.q1 - self.q2
        self.assertEqual(result.w, -4)
        self.assertEqual(result.x, -4)
        self.assertEqual(result.y, -4)
        self.assertEqual(result.z, -4)

    def test_multiplication(self):
        result = self.q1 * self.q2
        expected_result = Quaternion(-60, 12, 30, 24)
        self.assertAlmostEqual(result.w, expected_result.w)
        self.assertAlmostEqual(result.x, expected_result.x)
        self.assertAlmostEqual(result.y, expected_result.y)
        self.assertAlmostEqual(result.z, expected_result.z)

    def test_scalar_multiplication(self):
        result = self.q1 * self.scalar
        self.assertEqual(result.w, 2)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)
        self.assertEqual(result.z, 8)

    def test_division(self):
        result = self.q1 / self.q2
        expected_result = Quaternion(0.4023, 0.0460, 0.0, 0.0920)
        self.assertAlmostEqual(result.w, expected_result.w, places=4)
        self.assertAlmostEqual(result.x, expected_result.x, places=4)
        self.assertAlmostEqual(result.y, expected_result.y, places=4)
        self.assertAlmostEqual(result.z, expected_result.z, places=4)

    def test_scalar_mul(self):
        result = self.q1.scalar_mul(self.q2)
        self.assertEqual(result, 70)

    def test_norm(self):
        result = self.q1.norm()
        self.assertAlmostEqual(result, 5.477225575051661)

    def test_conjugate(self):
        result = self.q1.conjugate()
        self.assertEqual(result.w, 1)
        self.assertEqual(result.x, -2)
        self.assertEqual(result.y, -3)
        self.assertEqual(result.z, -4)

    def test_rotate_vector(self):
        q_rotation = Quaternion(0.7071, 0.7071, 0, 0)  # Поворот на 90 градусов вокруг оси X
        vector = (0, 1, 0)  # Вектор для поворота
        result = q_rotation.rotate_vector(vector)
        expected_result = (0.0, 0.0, 1.0)  # Вектор (0, 1, 0) повернется в (0, 0, 1)
        for r, e in zip(result, expected_result):
            self.assertAlmostEqual(r, e, places=4)

if __name__ == '__main__':
    unittest.main()