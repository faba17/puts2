import unittest
import main


class TestCalculator(
  unittest.TestCase):

  def setUp(self):
    main.app.testing = True
    self.app = main.app.test_client()

  def test_mul(self):
    solution = self.app.get('/mul?a=10&b=12&c=13')
    self.assertEqual(b'1560.000000', solution.data.strip())

    solution = self.app.get('/mul?a=2/6&b=3/12&c=1/15')
    self.assertEqual(b'0.005556', solution.data.strip())

    solution = self.app.get('/mul?a=8.9&b=4.2&c=1.3')
    self.assertEqual(b'48.594000', solution.data.strip())

    solution = self.app.get('/mul?a=9&b=3.534&c=1.314')
    self.assertEqual(b'41.793084', solution.data.strip())

    solution = self.app.get('/mul?a=9/2&b=1&c=2')
    self.assertEqual(b'9.000000', solution.data.strip())

if __name__ == '__main__':
  unittest.main()