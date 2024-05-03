#!/bin/bash

# Copyright (c) 2024 Yuichi Ito (yuichi@yuichi.com)
#
# This software is licensed under the Apache License, Version 2.0.
# For more information, please visit: https://github.com/yuichi110/drawlib
#
# This software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.

set -e

# cd to project root directory
cd "$(dirname "$0")"
cd ../

# activate
source .venv/bin/activate

# delete last build target contents
rm -rf ./docs/merged
rm -rf ./docs/html

# copy source to build target
rsync -ah ./docs/source/ ./docs/merged \
    --exclude ".pylintrc" --exclude ".gitkeep" --exclude "*.ttf" --exclude "__pycache__"

# generate rst apidoc to build target
sphinx-apidoc -f -o ./docs/merged/api ./drawlib \
    --module-first 

# build to html
sphinx-build -a ./docs/merged ./docs/html
