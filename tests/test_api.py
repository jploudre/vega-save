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
        save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_gantt.png")
        save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_gantt2.png", mode="vega-lite")

        save_from_file(os.path.join(self.examples_dir, "bar.vl2.json"), "test_bar.png")


    def test_from_api(self):
        save(LINE_GRAPH, "test_gantt2.png", mode="vega-lite")
