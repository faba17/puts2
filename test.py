import unittest
import main


class TestCalculator(
  unittest.TestCase):

  def setUp(self):
    main.app.testing = True
    self.app = main.app.test_client()

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

if __name__ == '__main__':
  unittest.main()