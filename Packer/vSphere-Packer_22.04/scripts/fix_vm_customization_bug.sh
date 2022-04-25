#!/bin/env bash

# Apply workaround to fix VMware customization bug (https://kb.vmware.com/s/article/59687)
sudo /usr/bin/sed -i 's/\[Unit]/\[Unit\]\nAfter=dbus.service/' /lib/systemd/system/open-vm-tools.service