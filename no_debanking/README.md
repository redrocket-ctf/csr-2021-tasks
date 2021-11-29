NOdeBANKing
=========

## Status
* Tech: Done
* Meta: Done, exploit missing because annoying to script
* More info in TODO.md

## Description
Reverse a customized Linux Kernel with debugging prevention and find and exploit a logic bug. The "public" part can be found in `buildroot/outputs/images` and no greping for the flag isn't a solution.

WARNING: The public part needs to be build separately. Take care not to include the flag in the public image. It can be changed in `secret_app.c`.

## CTF Description
A suspicious file has appeared on one of our extra super secure machines but the manufacturer prohibits debugging. We think something is wrong with `ptrace`.

Login is `notroot` without password. For your convenience the password for `root` on the test image is `123456` (but of course not on the server).

## Infos

* Author: lukas
* Ports: 5432
* Category: rev
* Flag: CSR{https://www.youtube.com/watch?v=ClTS8qlhAx4}
* Points: 400
