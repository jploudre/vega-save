# -*- coding: utf-8 -*-

LINE_GRAPH = {
    "$schema": "https://vega.github.io/schema/vega-lite/v2.6.0.json",
    "data": {
        "values": [
            {"a": "A", "b": 28},
            {"a": "B", "b": 55},
            {"a": "C", "b": 43}
        ]
    },
    "layer": [{
        "mark": "bar",
        "encoding": {
            "y": {"field": "a", "type": "ordinal"},
            "x": {"field": "b", "type": "quantitative"}
        }
    }, {
        "mark": {"type": "text", "style": "label"},
        "encoding": {
            "y": {"field": "a", "type": "ordinal"},
            "x": {"field": "b", "type": "quantitative"},
            "text": {"field": "b", "type": "quantitative"}
        }
    }],
    "config": {
        "style": {
            "label": {
                "align": "left",
                "baseline": "middle",
                "dx": 3
            }
        }
    }
}
