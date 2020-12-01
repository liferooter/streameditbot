#!/usr/bin/env bash

ulimit -Sv 50000 # ~= 50MB memory limit
env -i PATH=/bin:/usr/bin timeout 2 bash -c "$*" # Erase environment, set time limit and run