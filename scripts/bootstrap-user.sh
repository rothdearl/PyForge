#!/bin/bash

# Install Pyr-CLI: use --break-system-packages on externally managed environments.
python3 -m pip install ../ --user "$@"

# Remove build files.
rm -r ../build/
rm -r ../pyr_cli.egg-info/
