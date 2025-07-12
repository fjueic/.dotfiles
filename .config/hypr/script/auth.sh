#!/bin/bash

# Get current username
USERNAME=$(whoami)

# Get password from argument or prompt
if [ -n "$1" ]; then
    PASSWORD="$1"
else
    read -sp "Enter password for $USERNAME: " PASSWORD
    echo
fi

# Check password using 'expect' (silent mode)
if expect <<EOF >/dev/null 2>&1
spawn su - $USERNAME -c "exit"
expect "Password:"
send "$PASSWORD\r"
expect eof
catch wait result
exit [lindex \$result 3]
EOF
then
    echo "true"
else
    echo "false"
fi
