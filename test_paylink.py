# test_paylink.py
"""
Tests for PayLink module.
"""

import unittest
from paylink import PayLink

class TestPayLink(unittest.TestCase):
    """Test cases for PayLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PayLink()
        self.assertIsInstance(instance, PayLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PayLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
