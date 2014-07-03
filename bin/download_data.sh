#!/usr/bin/env bash

## paths relative to root of project
## ie: ./bin/download_data.sh

set -e 

#wget https://www.dropbox.com/s/7eq6or39ttbes3l/sw_emails.zip -P tmp/

if [ -d data/walker ]; then
    rm -rf data/walker
fi

mkdir -p data/walker

unzip tmp/sw_emails.zip -d data/walker/