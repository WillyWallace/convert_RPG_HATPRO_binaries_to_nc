"""Module for general helper functions."""

import glob
import time

# from numpy import ma
from datetime import datetime, timezone
from typing import NamedTuple
from numpy import ma

import numpy as np


SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400
FILL_VALUE_FLOAT = -999.0
FILL_VALUE_INT = -99
EPOCH = tuple[int, int, int]


class MetaData(NamedTuple):
    """named tuple"""
    long_name: str
    units: str
    standard_name: str | None = None
    definition: str | None = None
    comment: str | None = None


def seconds2hours(time_in_seconds: np.ndarray) -> np.ndarray:
    """Converts seconds since some epoch to fraction hour.
    Args:
        time_in_seconds: 1-D array of seconds since some epoch that starts on midnight.
    Returns:
        Time as fraction hour.
    Notes:
        Excludes leap seconds.
    """
    seconds_since_midnight = np.mod(time_in_seconds, SECONDS_PER_DAY)
    fraction_hour = seconds_since_midnight / SECONDS_PER_HOUR
    if fraction_hour[-1] == 0:
        fraction_hour[-1] = 24
    return fraction_hour


def epoch2unix(epoch_time, time_ref, epoch: EPOCH = (2001, 1, 1)):
    """Converts seconds since (2001,1,1,0,0,0) to unix time in UTC.

    Args:
        epoch_time (ndarray): 1-D array of seconds since (2001,1,1,0,0,0)
        time_ref (ndarray): 1: UTC, 0: Local Time
        epoch (ndarray): ...

    Returns:
        ndarray: Unix time in seconds since (1970,1,1,0,0,0).

    """

    delta = (datetime(*epoch) - datetime(1970, 1, 1, 0, 0, 0)).total_seconds()
    unix_time = epoch_time + int(delta)
    if time_ref == 0:
        for index, _ in enumerate(unix_time):
            unix_time[index] = time.mktime(
                datetime.fromtimestamp(unix_time[index], timezone.utc).timetuple()
            )
    return unix_time


def seconds2date(time_in_seconds: float, epoch: EPOCH = (1970, 1, 1)) -> list:
    """Converts seconds since some epoch to datetime (UTC).
    Args:
        time_in_seconds: Seconds since some epoch.
        epoch: Epoch, default is (1970, 1, 1) (UTC).
    Returns:
        [year, month, day, hours, minutes, seconds] formatted as '05' etc (UTC).
    """

    epoch_in_seconds = datetime.timestamp(datetime(*epoch, tzinfo=timezone.utc))
    timestamp = time_in_seconds + epoch_in_seconds
    return datetime.utcfromtimestamp(timestamp).strftime("%Y %m %d %H %M %S").split()


def get_file_list(path_to_files: str, extension: str):
    """Returns file list for specified path."""
    f_list = sorted(glob.glob(path_to_files + "/*." + extension))
    if len(f_list) == 0:
        f_list = sorted(glob.glob(path_to_files + "/*." + extension.lower()))
    if len(f_list) == 0:
        print(
            [
                "Error: no binary files with extension "
                + extension
                + " found in directory "
                + path_to_files
            ]
        )
    return f_list


def append_data(data_in: dict, key: str, array: ma.MaskedArray) -> dict:
    """Appends data to a dictionary field (creates the field if not yet present).
    Args:
        data_in: Dictionary where data will be appended.
        key: Key of the field.
        array: Numpy array to be appended to data_in[key].
    """
    data = data_in.copy()
    if key not in data:
        if array.ndim == 1:
            data[key] = array[:]
        else:
            data[key] = array[:, :]
    else:
        data[key] = ma.concatenate((data[key], array))
    return data
