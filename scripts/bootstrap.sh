#!/bin/bash

# Install PyForge: use --break-system-packages on externally managed environments.
pip3 install ../ --user

# Remove build files.
#rm -r ../pyforge.egg-info/
#rm -r ../build/
