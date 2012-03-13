 ssh -X -Y $(finger $USER|awk '/On/ { print $11}') "notify-send \"$1\" \"$2\""
