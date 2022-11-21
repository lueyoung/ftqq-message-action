#!/bin/bash

python3 /src/messager.py --enable "${INPUT_ENABLE}" \
  --sckey "${INPUT_SCKEY}" \
  --title "${INPUT_TITLE}" \
  --content "${INPUT_CONTENT}"
