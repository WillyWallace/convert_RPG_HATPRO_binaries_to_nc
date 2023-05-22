"""Module for Level 1 Metadata"""

from meta import (global_attributes,
                  FIELDS, att_reader,
                  ATTRIBUTES_COM,
                  ATTRIBUTES_brt,
                  ATTRIBUTES_irt,
                  ATTRIBUTES_met,
                  ATTRIBUTES_cbh)


def add_global_attrs(_data):
    """Adds global attributes"""
    for key, values in global_attributes.items():
        _data.attrs[key] = values
    return _data


def get_data_attributes(data, data_type: str):
    """Adds Metadata for RPG MWR Level 1 variables for NetCDF file writing.
    Args:
        data: RpgArray instances.
        data_type: Data type of the netCDF file.

    Returns:
        Dictionary

    Raises:
        RuntimeError: Specified data type is not supported.

    Example:
        from level1.lev1_meta_nc import get_data_attributes
        att = get_data_attributes('data','data_type')
    """
    if data_type not in (
            "brt",
            "irt",
            "met",
            "cbh",
    ):
        raise RuntimeError(
            ["Data type " + data_type + " not supported for file writing."]
        )

    if data_type in ("brt", "irt", "met", "cbh"):
        read_att = att_reader[data_type]
        attributes = dict(ATTRIBUTES_COM, **read_att)

    elif data_type == "brt":
        attributes = dict(
            ATTRIBUTES_COM, **ATTRIBUTES_brt, **ATTRIBUTES_irt, **ATTRIBUTES_met, **ATTRIBUTES_cbh
        )

    data = add_var_attrs(data, attributes)

    return data


def add_attrs(var, data_set, attributes):
    """Loop over attributes"""
    if var in attributes:
        j = 0
        for i in attributes[var]:
            if i is not None:
                # print(field[j])
                # print(i)
                data_set[var].attrs[FIELDS[j]] = i
            j = j + 1
    return data_set


def add_var_attrs(xrdata, attributes):
    """Adds attributes"""
    for var in xrdata.data_vars:
        add_attrs(var, xrdata, attributes)

    for var in xrdata.coords:
        add_attrs(var, xrdata, attributes)

    return xrdata
