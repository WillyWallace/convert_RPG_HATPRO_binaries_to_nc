import numpy as np
from os import path, makedirs
from convert_rpg_bin import convert_data, make_xarray
from get_attributes import get_data_attributes, add_global_attrs
from utils import get_file_list

raw_path = '../data/binary/'
out_path = '../data/nc/'

data_types = ['cbh', 'irt']

years = [2020]
months = [7 , 8, 9, 10]
days = np.arange(1, 31)

for yy in years:
    for mm in months:
        for dd in days:
            for data_type in data_types:
                path_to_files = raw_path + \
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
                    out_path_1 = out_path + data_type + '/' + \
                        str(yy).zfill(2) + '/' + \
                        str(mm).zfill(2) + '/'
                    if not path.exists(out_path_1):
                        makedirs(out_path_1)
                    data.to_netcdf(out_path_1 + outfilename + '.nc')
