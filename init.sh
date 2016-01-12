#!/bin/bash

echo "init virtural env"
virtualenv venc --no-site-packages
#source venc/bin/activate
source venc/bin/activate
pip install -r requirements
mkdir app
cp venc/lib/python2.7/site-packages/bottle.py app/
