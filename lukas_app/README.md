Lukas App
=========

## Status
* Meta: okay(ish)
* Tech: poc done (needs some nice css etc. but is working)

## Description

For testing lukas-app.de (and some subdomains) need to be directed to localhost or the containers ip.
Listing the domains would give away part of the challenge, so maybe just add them as you go.

During the CTF lukas-app.de will need to point to a server where the containers are directly reachable
on port 80 and 443. There shouldn't be any high ressource requirements so a small shared host for all
players should be totally fine.

See WRITEUP.md for details on how to solve this challenge.

## CTF Description

After the excellent success of the luca-app we now decided to build our own tracing apps.
We still have some technical difficulties but you may still want to have a look: https://lukas-app.de

## Infos

* Author: lukas2511
* Ports: 80, 443 (needs domain lukas-app.de)
* Category: web
* Flag: CSR{%79%6f%75%20%63%61%6e%27%74%20%65%73%63%61%70%65%20%74%68%65%20%64%6f%75%62%6c%65%20%64%6f%74%73}
* Points: 300

