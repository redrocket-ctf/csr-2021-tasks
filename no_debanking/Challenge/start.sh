#!/bin/bash

function finish {
    rm -rf $SESSION
}

SESSION="$(openssl rand -hex 16)"
mkdir "./$SESSION"
cp rootfs.ext2 $SESSION

trap finish EXIT

timeout 10m qemu-system-x86_64 -M pc -m 256M -smp 1 \
    -kernel bzImage \
    -append "root=/dev/vda console=ttyS0,115200n8" \
    -drive file="$SESSION/rootfs.ext2",format=raw,if=virtio \
    -no-reboot \
    -monitor /dev/null \
    -nographic