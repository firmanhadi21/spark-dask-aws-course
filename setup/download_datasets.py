"""
Automated dataset downloader for the Big Data Engineering course.

Downloads sample and full datasets from open data sources.
Run: python setup/download_datasets.py --mode sample  (for quick start, ~200 MB)
Run: python setup/download_datasets.py --mode full     (for complete course, ~10 GB)

All datasets are freely available. ERA5 requires a free Copernicus CDS account.
"""

import os
import sys
import argparse
import hashlib
from pathlib import Path
from urllib.request import urlretrieve
from tqdm import tqdm

DATA_DIR = Path(__file__).parent.parent / "data"
SAMPLE_DIR = DATA_DIR / "sample"

DATASETS = {
    "taxi": {
        "description": "NYC Yellow Taxi Trip Records (TLC)",
        "sample_urls": [
            "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet",
        ],
        "full_urls": [
            f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-{m:02d}.parquet"
            for m in range(1, 13)
        ],
        "subdir": "taxi",
    },
    "pluto": {
        "description": "NYC PLUTO Property Assessment",
        "sample_urls": [
            "https://data.cityofnewyork.us/api/views/64uk-42ks/rows.csv?accessType=DOWNLOAD",
        ],
        "full_urls": [
            "https://data.cityofnewyork.us/api/views/64uk-42ks/rows.csv?accessType=DOWNLOAD",
        ],
        "subdir": "pluto",
        "rename": {"rows.csv?accessType=DOWNLOAD": "pluto.csv"},
    },
    "epa_aqs": {
        "description": "EPA Air Quality System - Daily PM2.5",
        "sample_urls": [
            "https://aqs.epa.gov/aqsweb/airdata/daily_88101_2023.zip",
        ],
        "full_urls": [
            f"https://aqs.epa.gov/aqsweb/airdata/daily_88101_{y}.zip"
            for y in range(2019, 2024)
        ],
        "subdir": "epa_aqs",
    },
    "chirps": {
        "description": "CHIRPS Rainfall (monthly, global)",
        "sample_urls": [
            "https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/chirps-v2.0.2023.01.nc",
        ],
        "full_urls": [
            f"https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/chirps-v2.0.2023.{m:02d}.nc"
            for m in range(1, 13)
        ],
        "subdir": "chirps",
    },
}


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_file(url, dest_path):
    """Download a file with progress bar."""
    dest_path = Path(dest_path)
    if dest_path.exists():
        print(f"  [skip] Already exists: {dest_path.name}")
        return

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  Downloading: {dest_path.name}")

    with DownloadProgressBar(unit="B", unit_scale=True, miniters=1, desc=dest_path.name) as t:
        urlretrieve(url, dest_path, reporthook=t.update_to)


def download_dataset(name, config, mode="sample"):
    """Download a single dataset."""
    urls = config["sample_urls"] if mode == "sample" else config["full_urls"]
    base_dir = SAMPLE_DIR if mode == "sample" else DATA_DIR
    subdir = base_dir / config["subdir"]

    print(f"\n{'='*60}")
    print(f"Dataset: {config['description']}")
    print(f"Files: {len(urls)}")
    print(f"Target: {subdir}")
    print(f"{'='*60}")

    for url in urls:
        filename = url.split("/")[-1].split("?")[0]
        if "rename" in config and filename in config.get("rename", {}):
            filename = config["rename"][filename]
        download_file(url, subdir / filename)


def main():
    parser = argparse.ArgumentParser(description="Download course datasets")
    parser.add_argument(
        "--mode",
        choices=["sample", "full"],
        default="sample",
        help="Download sample (~200MB) or full (~10GB) datasets",
    )
    parser.add_argument(
        "--datasets",
        nargs="+",
        choices=list(DATASETS.keys()) + ["all"],
        default=["all"],
        help="Which datasets to download",
    )
    args = parser.parse_args()

    datasets_to_download = DATASETS if "all" in args.datasets else {k: DATASETS[k] for k in args.datasets}

    print(f"Mode: {args.mode}")
    print(f"Datasets: {', '.join(datasets_to_download.keys())}")
    print(f"Data directory: {DATA_DIR}")

    for name, config in datasets_to_download.items():
        try:
            download_dataset(name, config, args.mode)
        except Exception as e:
            print(f"\n  [ERROR] Failed to download {name}: {e}")
            print("  Continuing with next dataset...")

    print(f"\n{'='*60}")
    print("Download complete!")
    print(f"Data location: {DATA_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
