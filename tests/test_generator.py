import unittest
from cv_generator.generator import CVGenerator

class TestCVGenerator:
    """Testing the CVGenerator class"""
    def setup(self):
        self.generator = CVGenerator()

    def test_process(self):
        self.generator.process()
