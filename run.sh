#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$DIR/2dsim/" && http-server -c-1 -a 127.0.0.1 -o ||
echo "Please run"
echo
echo "     sudo npm install -g http-server"