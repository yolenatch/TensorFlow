# test_tensorflowai.py
"""
Tests for TensorFlowAI module.
"""

import unittest
from tensorflowai import TensorFlowAI

class TestTensorFlowAI(unittest.TestCase):
    """Test cases for TensorFlowAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TensorFlowAI()
        self.assertIsInstance(instance, TensorFlowAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TensorFlowAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
