# kernel-switcher

## Overview
`kernel-switcher` is a Python GTK3 application that allows users to choose, download, compile, and install Linux kernels with ease. It simplifies the process of managing kernel versions on Linux systems.

## Features
- List available Linux kernels
- Download and compile selected kernels
- Switch to a new kernel version seamlessly

## Installation

### Prerequisites
Before installing `kernel-switcher`, ensure you have the following installed on your system:
- Python 3.x
- GTK3 and PyGObject
  - For Debian/Ubuntu: `sudo apt-get install python3-gi python3-gi-cairo libcairo2-dev gir1.2-gtk-3.0 pkg-config libgirepository1.0-dev`
  - For more detailed installation instructions, see [PyGObject Installation](https://pygobject.readthedocs.io/en/latest/getting_started.html)

### Setup
1. Clone the repository:
   ```
   git clone hhttps://github.com/omerbustun/kernel-switcher.git
   ```
2. Navigate to the cloned directory:
   ```
   cd kernel-switcher
   ```
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application:
```
python src/Main.py
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.

## License
This project is licensed under the GNU General Public License, version 3 (GPLv3). See the [LICENSE](LICENSE) file for the full license text.