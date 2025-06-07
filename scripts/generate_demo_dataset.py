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

    # Create a richer collection of tensors demonstrating different shapes.
    vector = np.linspace(0, 1, 10, dtype=np.float64)
    matrix = np.random.rand(5, 5).astype(np.float32)
    cube = np.random.rand(4, 4, 4).astype(np.float32)
    hypercube = np.random.rand(2, 2, 2, 2).astype(np.float32)

    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    grid_x, grid_y = np.meshgrid(x, y)
    sine_wave = (np.sin(grid_x) * np.cos(grid_y)).astype(np.float32)

    all_tensors_path = data_dir / "all_tensors.npz"
    np.savez(all_tensors_path,
             arr=arr,
             vector=vector,
             matrix=matrix,
             cube=cube,
             hypercube=hypercube,
             sine_wave=sine_wave)
    print(f"Saved extended dataset to {all_tensors_path}")

if __name__ == "__main__":
    main()
