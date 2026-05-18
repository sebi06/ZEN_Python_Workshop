# GitHub Copilot Instructions — ZEN Python Workshop

## Repository Purpose

Educational workshop repository demonstrating Python tooling around **CZI image files**, **OME-ZARR**, and **deep-learning models** for microscopy. Targets ZEN software users and microscopy data scientists.

## Environment & Tooling

- **Package manager**: [Pixi](https://pixi.sh) — use `pixi install` to set up, `pixi run <task>` to execute tasks. Do **not** suggest `conda` or plain `pip` as the primary environment tool.
- **Python version**: 3.12
- **Environment name**: `zen-python` (defined in `pixi.toml`)
- **Key tasks** (defined in `pixi.toml`):
  - `pixi run start-napari` — launch Napari viewer
  - `pixi run start-omeui` — launch the CZI-to-OME-ZARR converter GUI

## Key Packages

| Package | Role |
|---|---|
| `pylibCZIrw` | Read/write CZI files (Python wrapper for libCZI C++) |
| `czitools` | Higher-level CZI metadata and pixel data utilities |
| `aicspylibczi` | Alternative CZI reader |
| `ngff-zarr` | Write OME-ZARR (NGFF) with multi-scale pyramids |
| `ome-zarr` | OME-ZARR reader/writer (ome-zarr-py) |
| `ngio` | Next-generation I/O for OME-ZARR |
| `napari` | Image viewer (with napari-czitools, napari-czann-segment plugins) |
| `pyclesperanto` | GPU-accelerated image processing |
| `czmodel` | Package/consume CZANN (ONNX + metadata) deep-learning models |

## Code Conventions

- **Path handling**: Always use `pathlib.Path`. For scripts in `scripts/`, derive paths relative to `Path(__file__).parent.parent` (repo root) — never use raw relative paths like `../` that depend on cwd.
- **OME-ZARR stores are directories**: use `os.path.isdir()` / `Path.is_dir()`, never `isfile()`, to check existence.
- **Notebook data downloads in Colab**: use `https://github.com/sebi06/ZEN_Python_Workshop/raw/main/...` (follows LFS redirects). Do **not** use `raw.githubusercontent.com` (returns LFS pointer stubs). For binary files stored in Git LFS, `media.githubusercontent.com/media/sebi06/...` is the alternative.
- **Git LFS**: `.czi`, `.czann`, `.npy`, `.pt`, `.zip` files are tracked via Git LFS. Do not suggest committing these as regular git objects.
- **Numpy in Colab**: Colab's pre-installed NumPy is often too old. Always add `! pip install --upgrade numpy` before other installs in Colab cells, followed by a manual restart reminder — do **not** use `os.kill()` to force a restart.
- **xarray DataArrays with ome-zarr-py**: pass `.data` (the underlying dask/numpy array) to `ome_zarr.writer.write_image()` — passing an `xr.DataArray` directly causes a dask `AssertionError`.

## Project Structure

```
czi_data/          # Sample CZI files and CZANN model files (Git LFS)
czi_omezarr_utils/ # Local Python package (editable install)
notebooks/         # Jupyter notebooks (Colab-compatible)
  data/            # Small data files for notebooks (Git LFS)
scripts/           # Standalone Python scripts
presentations/     # Slide assets
images/            # README images
pixi.toml          # Environment definition
pyproject.toml     # Package metadata for czi_omezarr_utils
```

## Notebook Guidelines

- All notebooks must be runnable both **locally** (via pixi) and on **Google Colab**.
- The `IN_COLAB` flag pattern must be at the top of every notebook:
  ```python
  try:
      import google.colab
      IN_COLAB = True
  except:
      IN_COLAB = False
  ```
- Data paths must use `os.getcwd()` (not `parents[N]`) — the notebook cwd is always the `notebooks/` directory in both environments.
- Do not use `if IN_COLAB / if not IN_COLAB` branching purely for file paths when `os.getcwd()` works uniformly.

## Disclaimer

All code is experimental. ZEISS does not officially support the scripts and plugins in this repository.
