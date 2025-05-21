<!-- [![Python package](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/actions/workflows/python-package.yml/badge.svg)](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/actions/workflows/python-package.yml)-->
[![Pylint](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/actions/workflows/pylint.yml/badge.svg)](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/actions/workflows/pylint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/releases/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/graphs/commit-activity)
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/RSAtmos_LIM.svg?style=social&label=Follow%20%40RSAtmos_LIM)](https://twitter.com/RSAtmos_LIM)
![Mastodon Follow](https://img.shields.io/mastodon/follow/109461236453474330?domain=https%3A%2F%2Fmeteo.social&logoColor=%230066cc&style=social)

<!-- [![Release][release-shield]][release-url] -->
<!-- [![PyPi version](https://badgen.net/pypi/v/pip/)](https://pypi.com/project/pip) -->

<!-- [![Twitter](https://img.shields.io/twitter/follow/RSAtmos_LIM?style=for-the-badge)](https://twitter.com/RSAtmos_LIM) -->

# Convert RPG microwave radiometer HATPRO binaries to netcdf files

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Introduction">Introduction</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- Introduction -->
## Introduction

This repository was created to convert binary to netcdf files of an microwave radiometer HATPRO manufactured by Radiometer Physics GmbH.

<!-- GETTING STARTED -->
## Getting Started

<!-- Installation -->
## Installation


Below is an example of how run the script, which reads in the data and plots the results. This method relies on external dependencies such as xarray, numpy and others (see `setup.py`).

1. Install from github
   ```sh
    git clone https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc
    cd convert_RPG_HATPRO_binaries_to_nc
    python3 -m venv venv
    source venv/bin/activate
    pip3 install --upgrade pip
    pip3 install .
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. tbd

<!--  <img src="eval_ac/results_ln2_cal.png" width="70%"> -->

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] add more binary conversion routines like IWV, LWP, SPC, ...
- [ ] add meaningful docstrings
- [ ] make documentation --> readthedocs
- [ ] enable pip install ...
- [ ] Released version 1
- [ ] Add Tests

See the [open issues](https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

[Andreas Foth](https://www.uni-leipzig.de/personenprofil/mitarbeiter/dr-andreas-foth)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
Most code is based on 
* [igmk GitHub](https://github.com/igmk/actris_mwr_pro)
* [cloudnetpy GitHub](https://github.com/actris-cloudnet/mwrpy.git)

Special thanks for templates and help during implementation.

* [Readme Template](https://github.com/othneildrew/Best-README-Template)
* [cloudnetpy GitHub](https://github.com/actris-cloudnet/cloudnetpy.git)

<p align="right">(<a href="#top">back to top</a>)</p>
