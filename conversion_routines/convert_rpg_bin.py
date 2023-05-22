"""
This module contains the conversion routines
"""

from conversion_routines.rpg_bin import RpgBin
from conversion_routines.utils import get_file_list

import xarray as xr
import conversion_routines.meta as meta


def convert_data(
    path_to_files: str,
    data_type: str,
) -> RpgBin:
    """Load and prepare data for netCDF writing"""

    if data_type == 'brt':
        brt_files = get_file_list(path_to_files, "BRT")
        rpg_bin = RpgBin(brt_files)
        rpg_bin.data['frequency'] = rpg_bin.header['_f']
    elif data_type == 'hkd':
        file_list_hkd = get_file_list(path_to_files, "HKD")
        rpg_bin = RpgBin(file_list_hkd)
    elif data_type == 'bls':
        file_list_bls = get_file_list(path_to_files, "BLS")
        rpg_bin = RpgBin(file_list_bls)
    elif data_type == 'irt':
        file_list_irt = get_file_list(path_to_files, "IRT")
        print(file_list_irt)
        rpg_bin = RpgBin(file_list_irt)
        rpg_bin.data['ir_wavelength'] = rpg_bin.header['_f']
    elif data_type == 'cbh':
        file_list_cbh = get_file_list(path_to_files, "CBH")
        rpg_bin = RpgBin(file_list_cbh)
    else:  # data_type == 'met':
        file_list_met = get_file_list(path_to_files, "MET")
        rpg_bin = RpgBin(file_list_met)

    return rpg_bin


def make_xarray(rpg, data_type):
    """make xarray dataset from dict"""

    # global coords, data_set
    allvarnames = []
    allshapes = []
    # rpg.data = get_data_attributes(rpg.data, data_type)
    for name, values in rpg.data.items():
        allvarnames.append(name)
        allshapes.append(values.shape)
    dims = meta.dims_reader[data_type]
    coords = [i for i in allvarnames if i not in dims]
    varis = [i for i in allvarnames if i not in coords]
    variables = {}
    coordinates = {}
    for var, values in rpg.data.items():
        if var in coords:
            coordinates.update(
                {
                    var: values
                }
            )

        elif var in varis:
            variables.update(
                {
                    var: (dims[var], values)
                }
            )

    return xr.Dataset(variables, coords=coordinates)
