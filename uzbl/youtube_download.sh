#!/bin/dash
DIR=/tmp/download
mkdir -p $DIR
cd $DIR
xterm -h -e sh -c "echo 'Getting URL...' ; echo ; youtube-dl -t '$1'"
