# Dataset Repository

This repository hosts metadata and configuration files used to manage datasets for the project. Actual dataset files are stored externally and retrieved on demand with [DVC](https://dvc.org/).

For an overview of tensors contained in the dataset, see [DATASET_TENSORS.md](./DATASET_TENSORS.md).

## Project goals


- Provide a centralized location for dataset version control.
- Ensure reproducible experiments by tracking data with DVC.
- Offer simple instructions for obtaining and using the datasets.

## Downloading data

Datasets are tracked using DVC so that the repository remains lightweight. To fetch the data:

1. Install DVC if you have not already:

   ```bash
   pip install dvc
   ```

2. Configure your DVC remote (only needed once):

   ```bash
   dvc remote add -d storage <remote-url>
   # dvc remote modify storage access_key_id <key>  # if credentials are required
   # dvc remote modify storage secret_access_key <secret>
   ```

3. Pull the dataset files:

   ```bash
   dvc pull
   ```

After the command completes, the data described by the repository's DVC files will appear in the workspace.

## Scripts

Helper scripts for working with the example dataset are located in the `scripts/` directory.

- `generate_demo_dataset.py` creates `data/tensors.npy` locally.
- `download_data.sh` installs DVC and pulls the dataset from a configured remote.

### Generating the demo dataset
Run:
```bash
python scripts/generate_demo_dataset.py
```

### Downloading with DVC
If you have configured a DVC remote, run:
```bash
./scripts/download_data.sh
```


## Usage

With the data downloaded you can import it in your experiments or notebooks. Example notebooks demonstrating basic usage are provided in the `notebooks/` directory.

## Repository structure

- `data/` - directory where dataset files will reside after running `dvc pull`.
- `dvc.yaml` - DVC pipeline definitions for dataset preparation (if present).
- `notebooks/` - Jupyter notebooks with sample Tensorus workflows.

## License

The dataset files are released into the public domain under the CC0 1.0
Universal license. Code and configuration contained in this repository
remain available under the MIT License. See the [LICENSE](./LICENSE)
file for full details.

## Contributing

We welcome contributions of new datasets, notebooks, and documentation.
Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to
get started. By participating in this project you agree to abide by our
[Code of Conduct](./CODE_OF_CONDUCT.md).
