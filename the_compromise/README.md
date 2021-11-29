The Compromise
=========

## Status
* Meta: Done
* Tech: Done

## Description
Parsing and encryting of CobaltStrike C2 DNS traffic.

## CTF Description
The SOC team of the BrighSoul QPL (Quantum Physic Labs) is continuously monitoring HTTP proxy and DNS outbound traffic and has identified suspicious DNS traffic to the server authoritative (NS) for the domain thedarkestside.org. Upon investigation, they presume that an internal windows workstation with has been compromised with a Colbalt Strike beacon running as the executable named ntupdate.exe. The workstation belongs to the R&D team and they are suspicions that files containing critical Intellectual Property information have been exfiltrated. You are a member of the CSIRT team and your objective is to identify which data has been leaked. You receive the following information:
•	A pcap file of the DNS traffic that transitted through the internal DNS server during the estimated timespan of the attack.
•	A bin file with the memory dump of the ntupdate.exe process (procdump –ma ntupdate.exe) on the victim workstation.


## Infos

* Author: Didier Stevens, Firat Acar
* Ports: -
* Category: forensic
* Flag: CSR{Schro3dinger%%3quation_}
* Points: 300
