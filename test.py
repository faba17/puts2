import unittest
import main


class TestCalculator(
  unittest.TestCase):

  def setUp(self):
    main.app.testing = True
    self.app = main.app.test_client()

  def test_div(self):
    solution = self.app.get('/div?a=10&b=12&c=13')
    self.assertEqual(b'0.064103', solution.data.strip())

    solution = self.app.get('/div?a=2/6&b=3/12&c=1/15')
    self.assertEqual(b'20.000000', solution.data.strip())

    solution = self.app.get('/div?a=8.9&b=4.2&c=1.3')
    self.assertEqual(b'1.630037', solution.data.strip())

    solution = self.app.get('/div?a=9&b=3.534&c=1.314')
    self.assertEqual(b'1.938120', solution.data.strip())

    solution = self.app.get('/div?a=9/2&b=1&c=2')
    self.assertEqual(b'2.250000', solution.data.strip())

if __name__ == '__main__':
  unittest.main()