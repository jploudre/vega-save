# -*- coding: utf-8 -*-
from collections import namedtuple

VegaVersions = namedtuple('VegaVersions', ['vega', 'vega_lite', 'vega_embded'])

vega_compatible_versions = {
    '4': VegaVersions('4.3.0', '2.6.0', '3.20.0'),
    '3': VegaVersions('3.3.1', '2.6.0', '3.20.0')
}

vega_lite_compatible_versions = {
    '3': VegaVersions('4.3.0', '3.0.0', '3.20.0'),
    '2': VegaVersions('3.3.1', '2.6.0', '3.20.0')
}


def get_corresponding_vega_versions(vega_version):
    major_version_num = vega_version.split('.')[0]

    return vega_compatible_versions[major_version_num]


def get_corresponding_vega_lite_versions(vega_lite_version):
    major_version_num = vega_lite_version.split('.')[0]

    return vega_lite_compatible_versions[major_version_num]
