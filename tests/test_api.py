# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 <company or person>
#
import unittest
import os
from vegasave import save, save_from_file
from .example_graphs import LINE_GRAPH


class TestStarter(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(__file__)
        self.examples_dir = os.path.join(self.test_dir, "example_graphs")

    def test_from_file(self):
        save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "vega-lite", "test_gantt.png")

    def test_from_api(self):
        save(LINE_GRAPH, "vega-lite", "test_gantt2.png")
