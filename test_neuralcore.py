# test_neuralcore.py
"""
Tests for NeuralCore module.
"""

import unittest
from neuralcore import NeuralCore

class TestNeuralCore(unittest.TestCase):
    """Test cases for NeuralCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralCore()
        self.assertIsInstance(instance, NeuralCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
