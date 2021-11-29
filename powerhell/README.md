Powerhell
==============

## Status
* Meta: Done
* Tech: Needs manual setup on a Windows server

## Description
Easy/Beginner PowerShell Remoting JEA Restricted Shell, need to abuse some functions to leak the sourcecode, spot a path traversal and get the flag

## CTF Description

You just popped a machine on your engagement and are spawned inside a powershell session. But wait! It got no scripting support and a very wierd environment. Are you just-enough-attacker to read the flag?

```
$cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList ("powerhell", (ConvertTo-SecureString -String "CSR2021!@" -AsPlainText -Force))

Enter-PSSession -ComputerName 34.68.181.45 -Credential $cred -Authentication Negotiate
```

**Linux Users:** You can use PowerShell Remoting from Linux. Install the `powershell` and `gss-ntlmssp` packages, spawn an `pwsh` and proceed to login just as usual.

## Infos

* Author: 0x4d5a
* Ports: 5985
* Category: Misc/Pwn
* Flag: CSR{p0w3rrrsh3ll_mag1cian_sp0tt3d}
* Points: ???
