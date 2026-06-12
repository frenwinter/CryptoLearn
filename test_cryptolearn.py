# test_cryptolearn.py
"""
Tests for CryptoLearn module.
"""

import unittest
from cryptolearn import CryptoLearn

class TestCryptoLearn(unittest.TestCase):
    """Test cases for CryptoLearn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoLearn()
        self.assertIsInstance(instance, CryptoLearn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoLearn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
