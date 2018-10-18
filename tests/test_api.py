# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 <company or person>
#
import unittest
import os
from vegasave import save, save_from_file, chart_driver
from tests.example_graphs import LINE_GRAPH


class TestStarter(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(__file__)
        self.examples_dir = os.path.join(self.test_dir, "example_graphs")

    def test_from_file(self):
        save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_gantt.png")
        save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_gantt2.svg", mode="vega-lite")

        save_from_file(os.path.join(self.examples_dir, "bar.vl2.json"), "test_bar.png")

    def test_save_multiple_from_file(self):
        with chart_driver() as chart_context:
            save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_mult1.png", driver=chart_context)
            save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_mult2.svg", driver=chart_context)
            save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_mult3.png", driver=chart_context)

    def test_no_kwargs_when_driver(self):
        try:
            with chart_driver() as chart_context:
                save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_mult1.png", driver=chart_context,
                               foo_bar=123)
            self.fail()
        except ValueError:
            pass
        try:
            with chart_driver() as chart_context:
                save_from_file(os.path.join(self.examples_dir, "gantt.vl2.json"), "test_mult1.svg", driver=chart_context,
                               web_driver='chrome')
            self.fail()
        except ValueError:
            pass

    def test_from_api(self):
        save(LINE_GRAPH, "test_gantt2.png", mode="vega-lite")
