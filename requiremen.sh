#!/bin/bash
pkg update
pkg install python
pip install virtualenv
virtualenv env
source env/bin/activate
pip install qrcode
deactivate
exit

