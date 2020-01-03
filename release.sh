#!/bin/bash

pyinstaller main.py --onefile
mv dist/main executables/v1.0.0/linux/flappyBird
rm -rf build/ dist/ main.spec
