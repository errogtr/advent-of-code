#!/bin/bash

#!/usr/bin/env bash

YEAR=$1
DAY=$(printf "%02d" "$2")
EXAMPLE=$3

if [[ -z "$YEAR" || -z "$DAY" ]]; then
  echo "Usage: ./solve.sh <year> <day> [--example]"
  exit 1
fi

# Use poetry if present, otherwise python
if command -v poetry &> /dev/null; then
    RUNNER="poetry run python"
else
    RUNNER="python"
fi

$RUNNER src/aoc/$YEAR/day$DAY/solution.py $EXAMPLE
