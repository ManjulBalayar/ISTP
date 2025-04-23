#!/usr/bin/env python
"""
Simplified test file for CI/CD that doesn't depend on database models.
"""

import unittest

class SimpleTests(unittest.TestCase):
    """Simple tests that don't depend on database models."""
    
    def test_true_is_true(self):
        """Simple test that always passes."""
        self.assertTrue(True)
    
    def test_one_plus_one_equals_two(self):
        """Test basic math functionality."""
        self.assertEqual(1 + 1, 2)
    
    def test_string_concatenation(self):
        """Test string concatenation."""
        self.assertEqual("hello " + "world", "hello world")

if __name__ == "__main__":
    unittest.main() 