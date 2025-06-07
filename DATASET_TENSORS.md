# Tensor Summary

The datasets `tensors.npy` and `all_tensors.npz` are tracked using DVC and contain numerical values used for examples in the project. The following table summarizes the tensors stored in these files.

| Tensor | Shape | Dtype | Description | Units |
|-------|-------|-------|-------------|-------|
| `tensors` | (2,) | float64 | Example numeric tensor for demonstration. | arbitrary |
| `vector` | (10,) | float64 | Linearly spaced vector from 0 to 1. | arbitrary |
| `matrix` | (5, 5) | float32 | Random matrix. | arbitrary |
| `cube` | (4, 4, 4) | float32 | Random cube. | arbitrary |
| `hypercube` | (2, 2, 2, 2) | float32 | Random hypercube. | arbitrary |
| `sine_wave` | (50, 50) | float32 | 2D sine wave. | arbitrary |

The tensors originate from the repository's `scripts/generate_demo_dataset.py` script. This script creates the simple float64 vector `[0.1, 0.2]` and a collection of additional tensors which are stored in `data/all_tensors.npz`. After pulling the data with DVC you can load them in Python:

```python
import numpy as np

tensor = np.load("data/tensors.npy")
print(tensor.shape)  # (2,)
print(tensor.dtype)  # float64

all_tensors = np.load("data/all_tensors.npz")
print(all_tensors["vector"].shape)
```
