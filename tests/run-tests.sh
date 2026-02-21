#!/bin/bash

# Default to no code coverage.
CODE_COVERAGE=false

# Check if --code-coverage is provided.
while [[ $# -gt 0 ]]; do
    case "$1" in
        --code-coverage)
            CODE_COVERAGE=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Run tests.
if [ "$CODE_COVERAGE" = true ]; then
    # Install required packages: use --break-system-packages on externally managed environments.
    pip3 install coverage --upgrade --user

    coverage run -m unittest discover -t ../ "tests" -q
    coverage report -m
    coverage html
else
    python3 -m unittest discover -t ../ "tests" -q
fi

# Remove the __pycache__ folder.
rm -r __pycache__
