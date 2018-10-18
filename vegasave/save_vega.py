# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 <company or person>
#
"""
The entry point for this application.
"""
import base64
import json
import os
import six

from vegasave.vega_verisons import get_corresponding_vega_versions, get_corresponding_vega_lite_versions

__version__ = "0.1.0"


supported_file_formats = ["svg", "png"]
EXTRACT_CODE = {
    'png': """
        var spec = arguments[0];
        var mode = arguments[1];
        var scaleFactor = arguments[2];
        var done = arguments[3];

        if(mode === 'vega-lite'){
          // compile vega-lite to vega
          const compiled = vl.compile(spec);
          spec = compiled.spec;
        }

        new vega.View(vega.parse(spec), {
              loader: vega.loader(),
              logLevel: vega.Warn,
              renderer: 'none',
            })
            .initialize()
            .toCanvas(scaleFactor)
            .then(function(canvas){return canvas.toDataURL('image/png');})
            .then(done)
            .catch(function(err) { console.error(err); });
        """,
    'svg': """
        var spec = arguments[0];
        var mode = arguments[1];
        var scaleFactor = arguments[2];
        var done = arguments[3];

        if(mode === 'vega-lite'){
          // compile vega-lite to vega
          const compiled = vl.compile(spec);
          spec = compiled.spec;
        }

        new vega.View(vega.parse(spec), {
              loader: vega.loader(),
              logLevel: vega.Warn,
              renderer: 'none',
            })
            .initialize()
            .toSVG(scaleFactor)
            .then(done)
            .catch(function(err) { console.error(err); });
        """,
    'vega': """
        var spec = arguments[0];
        var mode = arguments[1];
        var done = arguments[3];

        if(mode === 'vega-lite'){
          // compile vega-lite to vega
          const compiled = vl.compile(spec);
          spec = compiled.spec;
        }

        done(spec);
        """}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Embedding Vega-Lite</title>
  <script src="vega-{vega_version}.js" charset="UTF-8"></script>
  <script src="vega-lite-{vegalite_version}.js"></script>
  <script src="vega-embed-{vegaembed_version}.js"></script>
</head>
<body>
  <div id="vis"></div>
</body>
</html>
"""

def print_version():
    """
    Print the version
    :return:
    """
    print("Version: {}".format(__version__))


def save_from_file(json_spec_file_name, save_location, **kwargs):
    with open(json_spec_file_name) as f:
        data = json.load(f)

    save(data, save_location, **kwargs)


def save(spec, file_name, mode=None, scale_factor=1, web_driver='chrome', driver_timeout=20,
         vega_version=None, vega_lite_version=None, vega_embed_version=None):
    """
    Run your application.
    :return:
    """
    print_version()
    vega_version = '4.2.0'
    vega_embed_version = '3.18.2'
    vega_lite_version = '2.6.0'

    # selenium is an optional dependency, so import it here
    try:
        import selenium.webdriver
    except ImportError:
        raise ImportError("selenium package is required for saving chart as {0}".format(supported_file_formats))

    if not isinstance(file_name, six.string_types):
        raise ValueError("Must specify file name: {}".format(supported_file_formats))

    render_format = file_name.split('.')[-1]
    if render_format not in supported_file_formats:
        raise NotImplementedError("File extension (render_format) must be one of the following:"
                                  " {}".format(supported_file_formats))

    if mode is None:
        mode = spec['$schema'].split('/')[-2]
    if mode not in ['vega', 'vega-lite']:
        raise ValueError("mode must be either 'vega' or 'vega-lite'")

    if mode == 'vega':
        vega_version = vega_version if vega_version else str(spec['$schema'].split('/')[-1]).lstrip('v').rstrip('.json')
        vega_lite_version = vega_lite_version if vega_lite_version else get_corresponding_vega_versions(vega_version).vega_lite
        vega_embed_version = vega_embed_version if vega_embed_version else get_corresponding_vega_versions(vega_version).vega_embded
    elif mode == 'vega-lite':
        vega_lite_version = vega_lite_version if vega_lite_version else str(spec['$schema'].split('/')[-1]).lstrip('v').rstrip('.json')
        vega_version = vega_version if vega_version else get_corresponding_vega_lite_versions(vega_lite_version).vega
        vega_embed_version = vega_embed_version if vega_embed_version else get_corresponding_vega_lite_versions(vega_lite_version).vega_embded
    else:
        raise ValueError("Cannot determine vega/vega-lite version")

    if vega_version is None:
        # TODO: Depending on the mode, this can be found from the $schema
        raise ValueError("must specify vega_version")

    if vega_embed_version is None:
        # TODO: Depending on mode/version, this can be determined programtically
        raise ValueError("must specify vegaembed_version")

    if mode == 'vega-lite' and vega_lite_version is None:
        # TODO: Depending on the mode, this can be found from the $schema
        raise ValueError("must specify vega-lite version")

    if web_driver == 'chrome':
        web_driver_class = selenium.webdriver.Chrome
        web_driver_options_class = selenium.webdriver.chrome.options.Options
    elif web_driver == 'firefox':
        web_driver_class = selenium.webdriver.Firefox
        web_driver_options_class = selenium.webdriver.firefox.options.Options
    else:
        raise ValueError("webdriver must be 'chrome' or 'firefox'")

    webdriver_options = web_driver_options_class()
    webdriver_options.add_argument("--headless")

    if issubclass(web_driver_class, selenium.webdriver.Chrome):
        # for linux/osx root user, need to add --no-sandbox option.
        # since geteuid doesn't exist on windows, we don't check it
        if hasattr(os, 'geteuid') and (os.geteuid() == 0):
            webdriver_options.add_argument('--no-sandbox')

    # Update HTML file with the correct versions
    htmlfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "js", "download_template.html"))
    new_html = HTML_TEMPLATE.format(vega_version=vega_version,
                                    vegalite_version=vega_lite_version,
                                    vegaembed_version=vega_embed_version)
    with open(htmlfile, 'w') as f:
        f.write(new_html)

    driver = web_driver_class(options=webdriver_options)

    try:
        driver.set_page_load_timeout(driver_timeout)
        driver.get("file://" + htmlfile)
        online = driver.execute_script("return navigator.onLine")
        if not online:
            raise ValueError("Internet connection required for saving "
                             "chart as {0}".format(render_format))
        driver_render = driver.execute_async_script(EXTRACT_CODE[render_format], spec, mode, scale_factor)

        _save_render_to_location(file_name, driver_render, render_format)

    finally:
        driver.close()


def _save_render_to_location(file_name, render, render_format):
    if render_format == 'png':
        render = base64.decodebytes(render.split(',', 1)[1].encode())
        mode = 'wb'
    elif render_format == 'svg':
        mode = 'w'
    else:
        raise ValueError("render_format must be one of {}".format(supported_file_formats))

    with open(file_name, mode) as f:
        f.write(render)
