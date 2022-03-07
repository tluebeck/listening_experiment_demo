#!/bin/sh

# get absolute path
# from https://stackoverflow.com/questions/3572030/bash-script-absolute-path-with-os-x
realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

BASEDIR=$(dirname "${0}")
ABSDIR=$(realpath "${BASEDIR}")

# On macOS, use this:
# SSR fails to load for some reason in case only relative path is provided
open -n -a SoundScapeRenderer --args --brs "${ABSDIR}/demo_ssr_scene.asd" --tracker=patriot --tracker-port=/dev/tty.UC-232AC

# On linux, use this:
#ssr-brs "${BASEDIR}/stimuli.asd"
