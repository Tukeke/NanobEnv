#!/bin/sh
# just an example of how you could handle your downloads
# try some pattern matching on the uri to determine what we should do

# stupid cookies :(
#cp ~/.config/uzbl/cookies.txt /tmp/.cookies.txt
#chmod 0600 /tmp/.cookies.txt

dest="$HOME/download"
dest="/tmp/download"
mkdir "$dest" 2> /dev/null

# Some sites block the default wget --user-agent..
GET="wget --user-agent=Firefox"

#TARGET=$(mktemp "--tmpdir=$dest")
#GET="curl -c /tmp/.cookies.txt --output $TARGET --user-agent Firefox"

url="$8"

http_proxy="$9"
export http_proxy

test "x$url" = "x" && { echo "you must supply a url! ($url)"; exit 1; }

cd "$dest"
xterm -e sh -c "echo 'Downloading $url?' ; read x ; $GET '$url' ; echo ; echo 'saved $url to $dest' ; read x"
