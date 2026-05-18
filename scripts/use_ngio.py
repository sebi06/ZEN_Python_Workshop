import ngio
from ngio import open_ome_zarr_plate
from czi_omezarr_utils.validation import validate_ome_zarr
from pathlib import Path

# define path to local OME-ZARR file — resolved relative to this script's location
# so it works regardless of the working directory from which the script is invoked
REPO_ROOT = Path(__file__).parent.parent
omezarr_path = REPO_ROOT / "czi_data" / "WP96_4Pos_B4-10_DAPI_ngff_plate.ome.zarr"

# validate the OME-ZARR file
is_valid = validate_ome_zarr(omezarr_path)
if not is_valid:
    print(f"❌ Invalid OME-ZARR file: {omezarr_path}")

# define path to a field image group inside the plate (s0 is a raw array level, not an image)
image_path = omezarr_path / "B" / "04" / "0"

# validate image path
is_valid = validate_ome_zarr(image_path)
if not is_valid:
    print(f"❌ Invalid Image path inside OME-ZARR file: {image_path}")


plate = ngio.open_ome_zarr_plate(omezarr_path)
hcs_zarr = open_ome_zarr_plate(omezarr_path)
print(hcs_zarr)
print(f"Rows: {hcs_zarr.rows}, Columns: {hcs_zarr.columns}")

ome_zarr_container = ngio.open_ome_zarr_container(image_path)
image = ome_zarr_container.get_image()

print(f"Image shape: {image.shape}, dtype: {image.dtype}")
