"""
this file contains the unit test routines
"""

import numpy as np

from conversion_routines.convert_rpg_bin import convert_data

PATH_TO_FILES = '../example_data/binary/Y2020/M07/D16/'


def test_convert_data():
    """unit test for main class"""
    obj = convert_data(PATH_TO_FILES, 'irt')
    # print(obj.header)
    # assert obj.filename is FILE
    assert obj.header['_code'] == 671112000
    assert np.allclose(obj.header['_xmin'], -45.383614)
    assert np.allclose(obj.header['_xmax'], 14.072856)
    assert obj.header['_time_ref'] == 1
    assert obj.header['_n_f'] == 1
    assert np.allclose(obj.header['_f'], 10.5)
    assert obj.header['n'] == 36760
