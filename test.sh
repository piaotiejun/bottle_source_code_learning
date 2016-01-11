#!/bin/bash

echo "init virtural env"
virtualenv vencs
. venc/bin/activate --no-site-packages
source ./venc/bin/activate
pip install -r requirements
