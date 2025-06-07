#!/usr/bin/env python3
"""Generate the example `tensors.npy` dataset.

This script creates the small demo dataset used throughout the
repository. The file will be written to `data/tensors.npy` relative to
the repository root. Existing files will be overwritten.
"""
from pathlib import Path
import numpy as np

def main() -> None:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    arr = np.array([0.1, 0.2], dtype=np.float64)
    out_path = data_dir / "tensors.npy"
    np.save(out_path, arr)
    print(f"Saved demo dataset to {out_path} ({arr.shape}, {arr.dtype})")

if __name__ == "__main__":
    main()
