# Wake-on-LAN Script (WakeOnBoot)

This is a simple Python script that enables Wake-on-LAN (WoL) on a network interface and adds a systemd service to automatically enable WoL on boot. 

## Getting Started

These instructions will help you run the script on your local machine and enable WoL on a network interface.

### Prerequisites

- Python 3.5 or later
- ethtool
- systemd (for Linux users)

### Installing

1. Clone this repository to your local machine.
2. Open the `WakeOnBoot.py` file in your favorite text editor.
3. Replace `<network-interface>` on line 4 with the name of the network interface you want to enable WoL on.
2. Replace `<network-interface>` on line 13 with the name of the network interface you want to enable WoL on.
4. Save the file.
5. Open a terminal and navigate to the directory containing `WakeOnBoot.py`.
6. Run the script by typing `sudo python3 WakeOnBoot.py` in the terminal.


## Contributing

If you find any issues with the script or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
