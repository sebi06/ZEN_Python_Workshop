# Changelog

All notable changes to this project are documented here.

---

## [2026.05.18]

### Added
- `.github/copilot-instructions.md` — Copilot coding conventions for this repo
- `CHANGELOG.md` — this file
- Git LFS tracking for all binary assets (`.czi`, `.czann`, `.npy`, `.pt`, `.zip`)

### Removed
- `env_omezarr.yml` and `env_smartmic.yml` moved to `legacy/` — superseded by `pixi.toml`

### Changed
- `pixi.toml` — fixed task definitions: `start-napari` and `start-omeui`
- `scripts/use_ngio.py` — fixed path resolution using `Path(__file__).parent.parent`
- `README.md` — fixed typos, grammar, broken links, and inverted disclaimer logic
- `notebooks/omezarr_from_czi_5d.ipynb` — fixed filepath handling and xarray → dask write path
- `notebooks/using_pylibCZIrw.ipynb` — fixed Colab download URLs (LFS-compatible) and `.npy` path
- `notebooks/read_czi_metadata.ipynb` — added NumPy upgrade step and Colab restart notice
- `notebooks/read_czi_segment_voroni_otsu.ipynb` — added NumPy upgrade and `pyclesperanto[cuda]` install
- `notebooks/process_omezarr_HCS_plate.ipynb` — fixed data path and `isfile` → `isdir` for OME-ZARR store

### Fixed
- Colab download failures caused by `raw.githubusercontent.com` not serving Git LFS content
- NumPy version conflicts in Colab (pre-installed 1.x too old for scikit-image / pyclesperanto)
- `pyclesperanto` missing GPU backend in Colab (`pyclesperanto[cuda]` required)
- `AssertionError` when passing `xr.DataArray` directly to `ome_zarr.writer.write_image()`
