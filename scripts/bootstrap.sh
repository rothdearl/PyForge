#!/bin/bash

# Install Pyr-CLI: system-wide
python3 -m pip install ../ "$@"

# Remove build files.
rm -r ../build/
rm -r ../pyr_cli.egg-info/
