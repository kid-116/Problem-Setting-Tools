#!/bin/bash

echo "Extracting inputs..."
python3 ./extract.py
export len=$?
echo "$len inputs files found"

echo "Verifying inputs..."
g++ ./verifier.cpp -o verifier
./verifier

echo "Generating outputs..."
g++ ./v1.cpp -o main

for i in $(seq -f "%02g" 0 $(($len - 1)))
do
    echo -n "."
    ./main $i
done
echo