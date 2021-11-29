#!/bin/sh

socat TCP-LISTEN:5432,reuseaddr,fork,su=chall EXEC:"./start.sh",stderr
