#!/bin/bash

# Install Pyr-CLI in a virtual environment.
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ../
