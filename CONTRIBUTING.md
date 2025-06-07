# Contributing Guide

Thank you for considering contributing to this dataset repository. We welcome improvements to datasets, notebooks, and documentation.

## Getting Started

1. Fork the repository and create your feature branch.
2. Make your changes with descriptive commit messages.
3. Open a pull request against the `main` branch.

Please open an issue first if you plan to contribute a new dataset or a major change.

## Datasets

- Use [DVC](https://dvc.org/) to track all dataset files.
- Place raw data in the `data/` directory and commit the corresponding `.dvc` file.
- Provide a short Markdown file describing the dataset and update `DATASET_TENSORS.md` or other summary documents as appropriate.
- Ensure that your dataset is released under a license that permits redistribution. By contributing, you agree to release data under the CC0 1.0 Universal license.

## Notebooks

- Add example notebooks under the `examples/` directory.
- Keep notebook outputs minimal. Clear large cell outputs before committing.
- Use relative paths so notebooks work from a fresh clone after running `dvc pull`.

## Documentation

- Documentation is written in Markdown.
- Keep a concise style and use relative links.
- Update the table of contents or references in existing documents when adding new files.

## Code Style

Follow existing code and documentation conventions. Run linters or formatting tools if applicable. Make sure your changes build or run correctly before opening a pull request.

Thank you for helping improve this project!
