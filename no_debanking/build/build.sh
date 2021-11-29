#!/bin/bash

export ROOT=$(pwd)
export TREE=$ROOT/custom
export BUILDROOT=buildroot
export CCACHE=/tmp/.buildroot-ccache

if [ ! -d "$BUILDROOT" ]; then
    mkdir -p $BUILDROOT
    touch $BUILDROOT/.nobackup
    echo "Fetching buildroot"
    wget https://buildroot.org/downloads/buildroot-2021.02.7.tar.gz -O buildroot.tar.gz

    echo "Extracting"
    tar -xf buildroot.tar.gz -C $BUILDROOT --strip-components 1
else
    echo "Reusing old build. In case of errors or to force a rebuild delete the folder buildroot."
    sleep 5
fi

cd $BUILDROOT

echo "Applying config"
make BR2_EXTERNAL=$TREE challenge_defconfig

echo "Building"
KBUILD_BUILD_USER=Bob KBUILD_BUILD_HOST=Builder make BR2_CCACHE_DIR=$CCACHE

cp output/images/{bzImage,rootfs.ext2} $ROOT/../Challenge