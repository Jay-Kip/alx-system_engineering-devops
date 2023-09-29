#!/usr/bin/env bash
# Bash script that displays the content of the file /etc/passwd
while IFS=":" read -r username _ userid _ _ homedir _; do
	#Display the username, User ID and home dir
	echo "Username: $username"
	echo "User ID: $userid"
	echo "Home Directory: $homedir"
	echo
done < /etc/passwd
