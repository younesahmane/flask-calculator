import unittest
from your_flask_app import app  # Import your Flask app here

class TestCalculatorAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True  # Enable testing mode

    def test_add(self):
        response = self.app.get('/add/5/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 8)

    def test_subtract(self):
        response = self.app.get('/subtract/10/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 6)

    def test_multiply(self):
        response = self.app.get('/multiply/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 6)

    def test_divide(self):
        response = self.app.get('/divide/8/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 4)

    def test_divide_by_zero(self):
        response = self.app.get('/divide/8/0')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

if __name__ == '__main__':
    unittest.main()
