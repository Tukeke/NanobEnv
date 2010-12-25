#!/bin/dash
DIR=/tmp/download
mkdir -p $DIR
cd $DIR
xterm -h -e sh -c "echo 'Getting URL...' ; echo ; youtube-dl --get-url '$1' | xsel -i ; xsel -o ; echo ; echo 'Saved URL in paste buffer' ; echo 'Play?' ; read x ; mplayer \$(xsel -o)"
