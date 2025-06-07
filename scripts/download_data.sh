#!/usr/bin/env bash
# Fetch the dataset using DVC.
# Assumes a DVC remote has been configured.
set -euo pipefail
pip install --quiet dvc

dvc pull
