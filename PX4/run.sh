#!/usr/bin/env bash
pushd PX4/Firmware
make posix_sitl_ekf2
popd
if [ -z "$1" ]; then
    echo "Launching only PX4"
    PX4/Firmware/build/posix_sitl_ekf2/px4 -d PX4/Firmware PX4/Firmware/posix-configs/SITL/init/ekf2/iris
else
    PX4/Firmware/build/posix_sitl_ekf2/px4 -d PX4/Firmware PX4/Firmware/posix-configs/SITL/init/ekf2/iris &
    echo "Launching mission: $1"
    sleep 100
    pkill -f px4
fi
