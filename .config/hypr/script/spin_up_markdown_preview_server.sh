#!/bin/bash

cd ~/Obsidian/
if ps | rg "node app.js" > /dev/null; then
    echo "Markdown preview server is already running."
    exit 1
fi

echo "Starting markdown preview server..."
node app.js --markdown-preview-server 
