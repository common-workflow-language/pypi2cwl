import os
import shutil
import subprocess
from io import StringIO
from unittest import TestCase, mock

import sys

from pypi2cwl import pypi2cwl

class GeneralTestCase(TestCase):
    test_dir = "test_dir/"

    def setUp(self):
        os.mkdir(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_script(self):
        subprocess.call("pypi2cwl cnvkit -d test-dir", shell=True)

    def test_pypi_packages_names(self):
        k = os.getcwd()
        for package in ['.3,%#!^@-?', 'non_existent_name']:
            args = ['pypi2cwl', package]
            with mock.patch('sys.stdout', new=StringIO()) as fakeOutput, mock.patch.object(sys, 'argv', args):
                with self.assertRaises(SystemExit):
                    pypi2cwl.main()
