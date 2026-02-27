#!/bin/bash

# Install Pyr-CLI: virtual environment
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ../
