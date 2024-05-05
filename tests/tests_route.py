import unittest
from app import app
import sys
import os


class TestRoutes(unittest.TestCase):
    def make_request(self, url):
        tester = app.test_client(self)
        return tester.get(url)

    def test_home_route(self):
        response = self.make_request("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_about_route(self):
        response = self.make_request("/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Page", response.data)


# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Add more test methods for other routes

if __name__ == "__main__":
    unittest.main()
