#!/bin/bash

# Ensure the log directory exists
mkdir -p /logs/verifier

# Run pytest and output the required ctrf.json report
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json

# Write the final score to the correct reward file path
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi