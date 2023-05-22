"""
This file contains all the meta information.
"""

from collections.abc import Callable
from typing import TypeAlias
from collections import namedtuple

import datetime


FIELDS = (
    'long_name',
    'standard_name',
    'units',
    'comment',
    'definition',
    )

MetaData = namedtuple('MetaData', FIELDS, defaults=(None,) * len(FIELDS))


global_attributes = {
    'principal_investigator': 'Heike Kalesse-Los, Andreas Foth',
    'contact_person': 'Andreas Foth',
    'author': 'Andreas Foth',
    'history': 'Data converted from original RPG binaries',
    'source': 'micorwave radiometer manufactured by Radiometer Physics GmbH (RPG)',
    'comments': '',
    'conventions': 'CF-1.8',
    'date_of_creation': str(datetime.datetime.utcnow()),
}

DIMS_brt = {
    'rain': ['time'],
    'tb': ['time', 'frequency'],
    '_angles': ['time'],
    'elevation_angle': ['time'],
    'azimuth_angle': ['time'],
}

DIMS_irt = {
    'rain': ['time'],
    'irt': ['time', 'ir_wavelength'],
    '_angles': ['time'],
    'ir_elevation_angle': ['time'],
    'ir_azimuth_angle': ['time'],
}

DIMS_met = {
    'rain': ['time'],
    'air_pressure': ['time'],
    'air_temperature': ['time'],
    'relative_humidity': ['time'],
    'wind_direction': ['time'],
    'wind_speed': ['time'],
    'rainfall_rate': ['time'],
}

DIMS_cbh = {
    'cbh': ['time'],
    'rain': ['time'],
}

FuncType: TypeAlias = Callable[[str], dict]
dims_reader: dict[str, dict] = {
    "brt": DIMS_brt,
    "irt": DIMS_irt,
    "met": DIMS_met,
    "cbh": DIMS_cbh,
}


ATTRIBUTES_COM = {
    "time": MetaData(
        long_name="Time (UTC) of the measurement",
        units="seconds since 1970-01-01 00:00:00.000",
        comment="Time indication of samples is at end of integration-time",
    ),
    "time_bnds": MetaData(
        long_name="Start and end time (UTC) of the measurements",
        units="seconds since 1970-01-01 00:00:00.000",
    ),
    "latitude": MetaData(
        long_name="Latitude of measurement station",
        standard_name="latitude",
        units="degrees_north",
    ),
    "longitude": MetaData(
        long_name="Longitude of measurement station",
        standard_name="longitude",
        units="degrees_east",
    ),
    "altitude": MetaData(
        long_name="Altitude above mean sea level of measurement station",
        standard_name="altitude",
        units="m",
    ),
    "rain": MetaData(
        long_name="Rain flag, 0: no rain, 1: rain",
        standard_name="rain",
        units="",
    ),
}


ATTRIBUTES_brt = {
    "frequency": MetaData(
        long_name="Nominal centre frequency of microwave channels",
        standard_name="radiation_frequency",
        units="GHz",
        comment="1) For double-sideband receivers, frequency corresponds to the\n"
        "local oscillator frequency whereas the radio frequency of the upper/lower\n"
        "sideband is frequency+/-sideband_IF_separation. 2) In case of known\n"
        "offset between the real and the nominal frequency of some channels,\n"
        "frequency+freq_shift gives more accurate values.",
    ),
    "receiver_nb": MetaData(
        long_name="Microwave receiver number",
        units="1",
    ),
    "receiver": MetaData(
        long_name="Corresponding microwave receiver for each channel", units="1"
    ),
    "bandwidth": MetaData(
        long_name="Bandwidth of microwave channels",
        units="GHz",
    ),
    "n_sidebands": MetaData(
        long_name="Number of sidebands",
        units="1",
        comment="0: direct-detection receivers, 1: single-sideband,\n"
        "2: double-sideband. The frequency separation of sidebands\n"
        "is indicated in sideband_IF_separation.",
    ),
    "sideband_IF_separation": MetaData(
        long_name="Sideband IF separation",
        comment="For double sideband channels, this is the positive and negative\n"
        "IF range distance of the two band passes around the centre frequency\n"
        "(which is the LO frqeuency)",
        units="GHz",
    ),
    "beamwidth": MetaData(
        long_name="Beam width (FWHM) of the microwave radiometer",
        units="degree",
    ),
    "freq_shift": MetaData(
        long_name="Frequency shift of the microwave channels",
        comment="For more accurate frequency values use frequency + freq_shift.",
        units="GHz",
    ),
    "tb": MetaData(
        long_name="Microwave brightness temperature",
        standard_name="brightness_temperature",
        units="K",
    ),
    "azimuth_angle": MetaData(
        long_name="Azimuth angle",
        standard_name="sensor_azimuth_angle",
        units="degree",
        comment="0=North, 90=East, 180=South, 270=West",
    ),
    "elevation_angle": MetaData(
        long_name="Sensor elevation angle",
        units="degree",
        comment="0=horizon, 90=zenith",
    ),
    "tb_accuracy": MetaData(
        long_name="Total absolute calibration uncertainty of brightness temperature,\n"
        "one standard deviation",
        units="K",
        comment="specify here source of this variable, e.g. literature value,\n"
        "specified by manufacturer, result of validation effort\n"
        "(updated irregularily) For RDX systems, derived from analysis\n"
        "performed by Tim Hewsion (Tim J. Hewison, 2006: Profiling Temperature\n"
        "and Humidity by Ground-based Microwave Radiometers, PhD Thesis,\n"
        "University of Reading.) Derived from sensitivity analysis of LN2\n"
        "calibration plus instrument noise levels (ACTRIS work), \n"
        "currently literature values (Maschwitz et al. for HATPRO, ? for radiometrics)",
    ),
    "tb_cov": MetaData(
        long_name="Error covariance matrix of brightness temperature channels",
        units="K*K",
        comment="the covariance matrix has been determined using the xxx method\n"
        "from observations at a blackbody target of temperature t_amb",
    ),
    "t_amb": MetaData(
        long_name="Ambient target temperature",
        units="K",
    ),
    "t_rec": MetaData(
        long_name="Receiver physical temperature",
        units="K",
    ),
    "t_sta": MetaData(
        long_name="Receiver temperature stability",
        units="K",
    ),
    "ir_zenith_angle": MetaData(
        long_name="Infrared sensor zenith angle",
        units="degree",
        comment="90=horizon, 0=zenith",
    ),
}


ATTRIBUTES_irt = {
    "ir_wavelength": MetaData(
        long_name="Wavelength of infrared channels",
        standard_name="sensor_band_central_radiation_wavelength",
        units="m",
    ),
    "ir_bandwidth": MetaData(
        long_name="Bandwidth of infrared channels",
        units="m",
        comment="Channel centre frequency.",
    ),
    "ir_beamwidth": MetaData(
        long_name="Beam width of the infrared radiometer",
        units="degree",
    ),
    "irt": MetaData(long_name="Infrared brightness temperatures", units="K"),
    "ir_azimuth_angle": MetaData(
        long_name="Infrared sensor azimuth angle",
        standard_name="sensor_azimuth_angle",
        units="degree",
        comment="0=North, 90=East, 180=South, 270=West",
    ),
    "ir_elevation_angle": MetaData(
        long_name="Infrared sensor elevation angle",
        units="degree",
        comment="0=horizon, 90=zenith",
    ),
}


ATTRIBUTES_met = {
    "air_temperature": MetaData(
        long_name="Air temperature",
        standard_name="air_temperature",
        units="K",
    ),
    "relative_humidity": MetaData(
        long_name="Relative humidity",
        standard_name="relative_humidity",
        units="1",
    ),
    "air_pressure": MetaData(
        long_name="Air pressure",
        standard_name="air_pressure",
        units="Pa",
    ),
    "rainfall_rate": MetaData(
        long_name="Rainfall rate",
        standard_name="rainfall_rate",
        units="m s-1",
    ),
    "wind_direction": MetaData(
        long_name="Wind direction",
        standard_name="wind_from_direction",
        units="degree",
    ),
    "wind_speed": MetaData(
        long_name="Wind speed",
        standard_name="wind_speed",
        units="m s-1",
    ),
}


ATTRIBUTES_cbh = {
    "cbh": MetaData(
        long_name="Cloud base height",
        standard_name="cloud_base_height",
        units="m",
    ),
}


att_reader: dict[str, dict] = {
    "brt": ATTRIBUTES_brt,
    "irt": ATTRIBUTES_irt,
    "met": ATTRIBUTES_met,
    'cbh': ATTRIBUTES_cbh,
}
