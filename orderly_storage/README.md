# orderly storage

## Status

- TODO: Add theming??
- Otherwise ready to test

## Description

The binary spawns two threads that communicate via message passing. The current message state is
tracked with a volatile instead of an atomic boolean, which results in a data race and UB. In this
case it leads to a race condition were messages are sometimes only partially transmitted. This leads
to a type confusion in the message kind, which can be used to read and write OOB of the storage
buffer. The intended solution overwrites the GOT entry of `puts` with the address of `execl` to
spawn a shell.

Questions for tester: How long did it take you to find the bug, how long to write the exploit? Does
the `inline` annotation make it too obvious where the bug is? How much pain was getting the race to
a reliable corruption? Did you choose a different exploitation path than the intended solution? Did
you encounter any annoyances during exploitation? How many points should this task be worth?

## CTF Description

Store all your data in this ordered memory storage, new and improved with a front- and a backend!

## Infos

- Author: LevitatingLion
- Ports: 3141
- Category: pwn
- Flag: `CSR{The execution of a program contains a data race if it contains two conflicting actions in different threads, at least one of which is not atomic, and neither happens before the other. Any such data race results in undefined behavior.}`
- Points: 300
