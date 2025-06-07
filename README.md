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

## Usage

With the data downloaded you can import it in your experiments or notebooks. Example notebooks and scripts demonstrating basic usage will be available in the `examples/` directory as they are added.

## Repository structure

- `data/` - directory where dataset files will reside after running `dvc pull`.
- `dvc.yaml` - DVC pipeline definitions for dataset preparation (if present).
- `examples/` - example notebooks and scripts (coming soon).

## License

This project is distributed under the terms of the LICENSE file.
