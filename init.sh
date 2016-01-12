#!/bin/bash

echo "init virtural env"
virtualenv venc
. venc/bin/activate --no-site-packages
source ./venc/bin/activate
pip install -r requirements
