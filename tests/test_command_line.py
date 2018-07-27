# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 <company or person>
#
import unittest
import subprocess
import os


class TestStarter(unittest.TestCase):

    def setUp(self):
        self.save_command = ['vega_save']
        self.test_dir = os.path.dirname(__file__)
        self.examples_dir = os.path.abspath(os.path.join(self.test_dir, "example_graphs"))

    def test_run(self):
        command = self.save_command + [os.path.join(self.examples_dir, "gantt.vl2.json"), 'vega-lite', 'test_gg.png']
        print(command)
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = pipe.communicate()
        # print(stdout)
        # self.assertEquals(stdout.splitlines(), "Version: 0.1.0\nHello World!\n".splitlines())
        self.assertEqual(pipe.returncode, 0)
