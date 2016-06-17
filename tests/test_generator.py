import unittest
from tempfile import TemporaryDirectory
import os
from os.path import join as pjoin, getsize as filesize
from textwrap import dedent

from yaml import dump as ymldump

import cv_generator.generator

class CVGeneratorTest(unittest.TestCase):
    """Testing the CVGenerator class"""

    TEST_DATA = {
        'title': 'A test file',
        'body': 'Test body'
    }

    TEST_TEMPLATE = dedent('''\
    \\documentclass[12pt]{article}
    \\title{\\VAR{data.title}}
    \\begin{document}
    \\VAR{data.body}
    \\end{document}
    ''')

    def setUp(self):
        self._cwd = os.getcwd()
        self.data_dir = TemporaryDirectory()
        self.template_dir = TemporaryDirectory()
        self.tempwd = TemporaryDirectory()
        self.configuration = {
            'latex': {
                'program': 'pdflatex',
                'root': 'main.tex',
                'format': 'pdf'
            }
        }
        self.out_file = pjoin(self.tempwd.name, 'main.pdf')
        with open(pjoin(self.data_dir.name, 'data.yml'), 'w') as data_file:
            ymldump(self.TEST_DATA, stream=data_file)
        with open(pjoin(self.template_dir.name, 'main.tex'), 'w') as template_file:
            template_file.write(self.TEST_TEMPLATE)
        os.chdir(self.tempwd.name)

    def tearDown(self):
        os.chdir(self._cwd)

    def test_process(self):
        cv_generator.generator.process(
            configuration=self.configuration,
            data_dir=self.data_dir.name,
            template_dir=self.template_dir.name
        )
        self.assertGreater(filesize(self.out_file), 0)
