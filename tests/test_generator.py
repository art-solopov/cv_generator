import unittest
from cv_generator.generator import CVGenerator

class CVGeneratorTest(unittest.TestCase):
    """Testing the CVGenerator class"""
    def setUp(self):
        self.generator = CVGenerator()

    def test_process(self):
        self.generator.load_data()
