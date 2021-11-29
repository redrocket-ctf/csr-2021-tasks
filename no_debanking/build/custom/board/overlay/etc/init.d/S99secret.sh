#!/bin/bash

setfattr -n security.nodebug -v 1 /usr/bin/secret_app
cp /usr/bin/secret_app /home/notroot/secret_app
setfattr -n security.nodebug -v 1 /home/notroot/secret_app