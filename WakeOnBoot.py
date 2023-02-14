import subprocess

# Run ethtool to enable Wake-on-LAN on the network interface
subprocess.run(['ethtool', '-s', '<network-interface>', 'wol', 'g'])

# Add ethtool command to a systemd service
with open('/etc/systemd/system/wol.service', 'w') as f:
    f.write('''[Unit]
Description=Enable Wake-on-LAN on boot

[Service]
Type=oneshot
ExecStart=/sbin/ethtool -s <network-interface> wol g

[Install]
WantedBy=multi-user.target
''')

# Enable and start the systemd service
subprocess.run(['systemctl', 'enable', 'wol.service'])
subprocess.run(['systemctl', 'start', 'wol.service'])
