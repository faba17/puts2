import unittest
import main


class TestCalculator(
  unittest.TestCase):

  def setUp(self):
    main.app.testing = True
    self.app = main.app.test_client()

  def test_add(self):
    solution = self.app.get('/add?a=10&b=12&c=13')
    self.assertEqual(b'35.000000', solution.data.strip())

    solution = self.app.get('/add?a=2/6&b=3/12&c=1/15')
    self.assertEqual(b'0.650000', solution.data.strip())

    solution = self.app.get('/add?a=8.9&b=4.2&c=1.3')
    self.assertEqual(b'14.400000', solution.data.strip())

    solution = self.app.get('/add?a=9&b=3.534&c=1.314')
    self.assertEqual(b'13.848000', solution.data.strip())

    solution = self.app.get('/add?a=9/2&b=1&c=2')
    self.assertEqual(b'7.500000', solution.data.strip())  

  def test_sub(self):
    solution = self.app.get('/sub?a=10&b=12&c=13')
    self.assertEqual(b'-15.000000', solution.data.strip())

    solution = self.app.get('/sub?a=2/6&b=3/12&c=1/15')
    self.assertEqual(b'0.016667', solution.data.strip())

    solution = self.app.get('/sub?a=8.9&b=4.2&c=1.3')
    self.assertEqual(b'3.400000', solution.data.strip())

    solution = self.app.get('/sub?a=9&b=3.534&c=1.314')
    self.assertEqual(b'4.152000', solution.data.strip())

    solution = self.app.get('/sub?a=9/2&b=1&c=2')
    self.assertEqual(b'1.500000', solution.data.strip())

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
