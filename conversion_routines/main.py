"""
This is the main routine which calls all others.
"""

from os import path, makedirs

import numpy as np

from conversion_routines.convert_rpg_bin import convert_data, make_xarray
from conversion_routines.get_attributes import get_data_attributes, add_global_attrs
from conversion_routines.utils import get_file_list


RAW_PATH = '../example_data/binary/'
OUT_PATH = '../example_data/nc/'

DATA_TYPES = ['cbh', 'irt']

YEARS = [2020]
MONTHS = [7]
DAYS = np.arange(15, 17)

for yy in YEARS:
    for mm in MONTHS:
        for dd in DAYS:
            for data_type in DATA_TYPES:
                path_to_files = RAW_PATH + \
                                'Y' + str(yy) + '/' + \
                                'M' + str(mm).zfill(2) + '/' + \
                                'D' + str(dd).zfill(2) + '/'

                if (get_file_list(path_to_files, data_type.upper()) == []) or (
                        path.exists(path_to_files) is False):
                    print('no ' + data_type + ' files on: ' + str(yy).zfill(2) + '-' +
                          str(mm).zfill(2) + '-' +
                          str(dd).zfill(2))
                else:
                    # read binaries
                    rpg = convert_data(path_to_files, data_type)

                    # make xarray
                    data_set = make_xarray(rpg, data_type)

                    # add variable attributes
                    data = get_data_attributes(data_set, data_type)

                    # add global attributes
                    data = add_global_attrs(data)

                    # write output netcdf
                    outfilename = str(yy).zfill(2) + str(mm).zfill(2) + str(dd).zfill(2) + \
                        '_' + data_type
                    out_path_1 = OUT_PATH + data_type + '/' + \
                                 str(yy).zfill(2) + '/' + \
                                 str(mm).zfill(2) + '/'
                    if not path.exists(out_path_1):
                        makedirs(out_path_1)
                    data.to_netcdf(out_path_1 + outfilename + '.nc')
