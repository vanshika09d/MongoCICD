import unittest
import urllib.request

class TestWebpage(unittest.TestCase):
    def test_webpage_running(self):
        response = urllib.request.urlopen('http://localhost:8081')
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
