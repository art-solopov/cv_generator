import unittest
import cv_generator.generator
from tempfile import TemporaryDirectory as tempdir
from os.path import join as pjoin, isfile
from yaml import dump as ymldump
from textwrap import dedent

class CVGeneratorTest(unittest.TestCase):
    """Testing the CVGenerator class"""

    TEST_DATA = {
        'title': 'A test file',
        'body': 'Test body'
    }

    TEST_TEMPLATE = dedent('''\
    \documentclass[12pt]{article}
    \title{\VAR{data.title}}
    \begin{document}
    \VAR{data.body}
    \end{document}
    ''')

    def setUp(self):
        self.configuration = {}
        self.data_dir = tempdir()
        self.template_dir = tempdir()
        with open(pjoin(self.data_dir.name, 'data.yml'), 'w') as data_file:
            ymldump(self.TEST_DATA, stream=data_file)
        with open(pjoin(self.template_dir.name, 'main.tex'), 'w') as template_file:
            template_file.write(self.TEST_TEMPLATE)

    def test_process(self):
        cv_generator.generator.process(
            configuration=self.configuration,
            data_dir=self.data_dir.name,
            template_dir=self.template_dir.name
        )
        self.fail('Incomplete test')
