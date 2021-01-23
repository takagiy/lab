#!/bin/sh

for f in checkset*.py; do
  echo $f
  python $f | grep ER
done
