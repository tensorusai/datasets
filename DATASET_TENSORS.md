# Tensor Summary

The dataset `tensors.npy` is tracked using DVC and contains numerical values used for examples in the project. The following table summarizes the tensors stored in this file.

| Tensor | Shape | Dtype | Description | Units |
|-------|-------|-------|-------------|-------|
| `tensors` | (2,) | float64 | Example numeric tensor for demonstration. | arbitrary |

The file originates from the repository's `scripts/generate_demo_dataset.py` script. This script creates a small float64 vector `[0.1, 0.2]` with shape `(2,)` and saves it as `data/tensors.npy`. After pulling the data with DVC you can load the tensor in Python:

```python
import numpy as np

tensor = np.load("data/tensors.npy")
print(tensor.shape)  # (2,)
print(tensor.dtype)  # float64
```
