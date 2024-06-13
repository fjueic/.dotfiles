#!/bin/bash

PID=$(ps aux | grep "node app.js --markdown-preview-server" | grep -v grep | awk '{print $2}')
kill $PID
