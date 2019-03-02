# Quick Start

To get started using this project:

> python setup.py install

to install vega-save.

## Simple Use Case

> import vegasave
> 
> with vegasave.chart_driver() as chart_context:
>     vegasave.save(spec_json1, 'save_location1.png', driver=chart_context)
>     vegasave.save(spec_json2, 'save_location2.png', driver=chart_context)
