#!/usr/bin/env bash

ulimit -Sv 50000 # ~= 50MB memory limit

# Erase environment, set time limit and run# Erase environment, set time limit and run
eval "$(printf 'env -i PATH=/bin:/usr/bin timeout 1 %q' "$*" | sed  's/\\\ / /g')"
