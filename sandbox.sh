#!/usr/bin/env bash

ulimit -Sv 50000 # ~= 50MB memory limit

for arg in "$@"
do
  cmd="$cmd '$arg'"
done

# Erase environment, set time limit and run
eval "env -i PATH=/bin:/usr/bin timeout 1 $cmd"
