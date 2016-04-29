import unittest
import cv_generator.generator

class CVGeneratorTest(unittest.TestCase):
    """Testing the CVGenerator class"""

    def setUp(self):
        self.config = {}

    def test_process(self):
        cv_generator.generator.process
