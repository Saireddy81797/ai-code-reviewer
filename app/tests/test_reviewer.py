import unittest
from app.reviewer import analyze_code

class TestReviewer(unittest.TestCase):

    def test_simple_code(self):
        code = "def add(a, b): return a + b"
        result = analyze_code(code)
        self.assertIn("complexity", result)
        self.assertIn("security_issues", result)

    def test_security_issue(self):
        code = "eval('2+2')"
        result = analyze_code(code)
        self.assertTrue(any("eval" in issue for issue in result["security_issues"]))

if __name__ == "__main__":
    unittest.main()
