#!/bin/bash

python3 /src/messager.py --enable "${INPUT_ENABLE}" \
  --token "${INPUT_TOKEN}" \
  --title "${INPUT_TITLE}" \
  --content "${INPUT_CONTENT}"
