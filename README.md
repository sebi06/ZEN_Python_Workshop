# ZEN Python Workshop

## Disclaimer

This content of this repository is free to use for everybody and purely experimental. The authors undertakes no warranty concerning the use of the code examples, ose scripts, image analysis settings and ZEN experiments, especially not for the examples using 3rd python modules. Use them on your own risk.

**By using any of those examples you agree to this disclaimer.**

## General Remarks

This repository contains scripts and notebooks showcasing several tools and scripts centered around ZEN, CZI image files, deep-learning models and related python packages.

## Prerequisites

### Install Pixi

- Download and install Miniconda if needed: [Download Pixi](https://pixi.prefix.dev/latest/installation/)
- Pixi Binaries can be found here: [Pixi Binary Release](https://github.com/prefix-dev/pixi/releases/tag/v0.68.1)
- check if installation was successful and check for updates:

```cmd
pixi --version
pixi self-update
```

### Install Python Environment

```cmd
pixi install
```

### Additional Remarks

> Important: If one wants to test the labeling & training directly on [arivis Cloud] or create a module it is required to have an account.
>
> To use [Colab] one needs to have a Google account.

## Python Package: pylibCZIrw

A simple and easy-to-use Python wrapper for [libCZI](https://github.com/ZEISS/libczi) - a cross-platform C++ library intended for providing read and write access to CZI documents


## Deep Learning Topics

### Train a Deep-Learning Model for Semantic Segmentation on arivis Cloud

The general idea is to learn how to label a dataset on [arivis Cloud].

Dataset Name: **Smart_Microscopy_Workshop_2025_Nucleus_Semantic**

![Annotated Dataset](./images/apeer_dataset_nuc.png)

- label some nuclei "precisely"
- label background areas and edges
- embrace the idea of partial labeling

![Partial Annotations](./images/APEER_annotation_auto_background.gif)

- start a training to get a trained model as a *.czann file

Remark: The the modelfile: **cyto2022_nuc2.czann** can be found inside the repository.

For more detailed information please visit: [Docs - Partial Annotations](https://docs.apeer.com/machine-learning/annotation-guidelines)

### Use the model in your python code

Once the model is trained it can be downloaded directly to your hard disk and used to segment images in ZEN or arivis Pro or your own python code.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/ZEN_Python_CZI_Smart_Microscopy_Workshop/blob/main/workshop/notebooks/run_prediction_from_czann.ipynb)

### Train your own model and package (as *.czann) using the [czmodel] package

The package provides simple-to-use conversion tools to generate a CZANN file from a [PyTorch] or [ONNX] model that resides in memory or on disk to be usable in the ZEN, arivis Cloud, arivisPro software platforms and also in your own code.

For details and more information examples please go to: [czmodel]

### Train a simple model for semantic segmentation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/ZEN_Python_CZI_Smart_Microscopy_Workshop/blob/main/workshop/notebooks/SingleClassSemanticSegmentation_PyTorch.ipynb)

### Train a simple model for regression

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/ZEN_Python_CZI_Smart_Microscopy_Workshop/blob/main/workshop/notebooks/Regresssion_PyTorch.ipynb)

### Use the model inside Napari (experimental)

This plugin is purely experimental. The authors undertakes no warranty concerning its use.

In order to use such a model one needs a running python environment with [Napari] and the [napari-czann-segment] plugin installed.

It can install it via [pip]:

```cmd
pip install napari-czann-segment
```

For more detailed information about the plugin please go to: [Napari Hub - napari-czann-segment](https://www.napari-hub.org/plugins/napari-czann-segment)

![Train on arivis Cloud and use model in Napari](https://github.com/sebi06/napari-czann-segment/raw/main/readme_images/Train_APEER_run_Napari_CZANN_no_highlights_small.gif)

## Using the [czitools] package (experimental)

This python package is purely experimental. The authors undertakes no warranty concerning its use.

For details please visit: [czitools]

### Read CZI metadata

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/czitools/blob/main/demo/notebooks/read_czi_metadata.ipynb)

### Read CZI pixeldata

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/czitools/blob/main/demo/notebooks/read_czi_pixeldata_simple.ipynb)

### Write OME-ZARR from 5D CZI image data

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/czitools/blob/main/demo/notebooks/omezarr_from_czi_5d.ipynb)

### Write CZI using ZSTD compression

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/czitools/blob/main/demo/notebooks/save_with_ZSTD_compression.ipynb)

### Show planetable of a CZI image as surface

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/czitools/blob/main/demo/notebooks/show_czi_surface.ipynb)

### Read a CZI and segment using Voroni-Otsu provided by PyClesperanto GPU processing

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sebi06/czitools/blob/main/demo/notebooks/read_czi_segment_voroni_otsu.ipynb)

## CZICheck - Check CZI for internal errors

[CZICheck] is a command-line application developed using libCZI, enabling users to assess the integrity and structural correctness of a CZI document.

Checking the validity of a CZI becomes more complex the closer one is to the application domain (e.g. application-specific metadata).
So this console application is more of a utility to help users who are directly using [libCZI], or its python wrapper [pylibCZIrw] & [pylibCZIrw_github], than it is an official validation tool for any ZEISS-produced CZIs.

CZICheck runs a collection of *checkers* which evaluate a well defined rule.
Each *checker* reports back findings of type Fatal, Warn, or Info.

Please check the tool's internal help by running `CZICheck.exe --help` and check additional documentation on the repository.

![CZIChecker in Action](./images/czichecker1.png)

## napari-czitools (experimental)

This plugin is purely experimental. The authors undertakes no warranty concerning its use.

In order to use such a model one needs a running python environment with [Napari] and the [napari-czitools] plugin installed.

It can install it via [pip]:

```cmd
pip install napari-czitools
```

For more detailed information about the plugin please go to: [Napari Hub - napari-czitools](https://napari-hub.org/plugins/napari-czitools.html)

## CZI and OME-ZARR (experimental)

All OME-ZARR related scripts here are purely experimental. The authors undertakes no warranty concerning the use of those scripts.

**By using any of those examples you agree to this disclaimer.**

### Convert CZI to OME-ZARR using [ome-zarr]

See: [write_omezarr_adv.py](./workshop/czi_omezarr/write_omezarr_adv.py)

### Convert CZI to OME-ZARR using [ngff-zarr]

See: [write_omezarr_adv.py](./workshop/czi_omezarr/write_omezarr_ngff.py)

### Convert CZI to OME-ZARR HCS Plate using [ome-zarr]

See: [write_omezarr_adv.py](./workshop/czi_omezarr/write_hcs_omezarr.py)

### Convert CZI to OME-ZARR HCS Plate using [ngff-zarr]

See: [write_omezarr_adv.py](./workshop/czi_omezarr/write_hcs_ngffzarr.py)

## Useful Links

---

| Name/Description                                      | Link                                                                                    | Name/Description                                      | Link                                                |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------- |
| Napari - Python-based image viewer                    | [GitHub](https://github.com/napari/napari)                                              | pip - Python Package Installer                        | [PyPI](https://pypi.org/project/pip/)               |
| PyPi - Python Package Index                           | [PyPI](https://pypi.org/)                                                               | pylibCZIrw - Python Package to read & write CZI files | [PyPI](https://pypi.org/project/pylibCZIrw)         |
| pylibCZIrw - GitHub Repository for CZI files (Python) | [GitHub](https://github.com/ZEISS/pylibczirw)                                           | czmodel - Package for Pytorch & ONNX models           | [PyPI](https://pypi.org/project/czmodel)            |
| cztile - Python Package for tiling arrays             | [PyPI](https://pypi.org/project/cztile)                                                 | arivis Cloud - DL Training Platform                   | [arivis Cloud](https://www.arivis.cloud)            |
| napari-czann-segment - Napari Plugin for DL models    | [GitHub](https://github.com/sebi06/napari_czann_segment)                                | napari-czitools - Plugin for CZI files                | [GitHub](https://github.com/sebi06/napari-czitools) |
| CZI - Carl Zeiss Image Format                         | [ZEISS](https://www.zeiss.com/microscopy/int/products/microscope-software/zen/czi.html) | PyTorch                                               | [PyTorch](https://pytorch.org)                      |
| ONNX                                                  | [ONNX](https://onnx.ai)                                                                 | libCZI - GitHub Repository for CZI files (C++)        | [GitHub](https://github.com/ZEISS/libczi)           |
| czitools - Tools for CZI files                        | [PyPI](https://pypi.org/project/czitools)                                               | Colab                                                 | [Colab](https://colab.research.google.com)          |
| Docker Desktop                                        | [Docker Desktop](https://www.docker.com/products/docker-desktop)                        | CZICompress - Shrink CZI files                        | [GitHub](https://github.com/ZEISS/czicompress)      |
| CZIChecker - Check Integrity of CZI files             | [GitHub](https://github.com/ZEISS/czicheck)                                             | ome-zarr - Python Implementation of NGFF Specs        | [GitHub](https://github.com/ome/ome-zarr-py)        |
| NGFF - Next-generation File Formats                   | [NGFF](https://ngff.openmicroscopy.org/)                                                | ngff-zarr - Python Implementation of NGFF Specs       | [GitHub](https://github.com/fideus-labs/ngff-zarr)  |

---

[Napari]: https://github.com/napari/napari
[pip]: https://pypi.org/project/pip/
[pylibCZIrw]: https://pypi.org/project/pylibCZIrw
[pylibCZIrw_github]: https://github.com/ZEISS/pylibczirw
[czmodel]: https://pypi.org/project/czmodel
[arivis Cloud]: https://www.arivis.cloud
[napari-czann-segment]: https://github.com/sebi06/napari_czann_segment
[napari-czitools]: https://github.com/sebi06/napari-czitools
[PyTorch]: https://pytorch.org
[ONNX]: https://onnx.ai
[libCZI]: https://github.com/ZEISS/libczi
[czitools]: https://pypi.org/project/czitools
[Colab]: https://colab.research.google.com
[Docker Desktop]: https://www.docker.com/products/docker-desktop
[CZICompress]: https://github.com/ZEISS/czicompress
[ome-zarr]: https://github.com/ome/ome-zarr-py
[ngff-zarr]: https://github.com/fideus-labs/ngff-zarr