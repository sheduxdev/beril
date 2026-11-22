#!/bin/sh
# diagnostic CGI, called as /cgi-bin/diagnostic.cgi?host=example.com
echo "Content-Type: text/plain"
echo
HOST="$QUERY_STRING"
HOST="${HOST#host=}"
echo "probing $HOST"
sh -c "/bin/ping -c 1 $HOST"
