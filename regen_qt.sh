#!/bin/bash

# regenerates the qt resource files.

set -e

# this script assume you're on archlinux.

/usr/lib/qt6/rcc --no-compress -g python animecho.qrc -o animecho_rc.py

/usr/lib/qt6/rcc -g python eye_candies.qrc -o eye_candies_rc.py
