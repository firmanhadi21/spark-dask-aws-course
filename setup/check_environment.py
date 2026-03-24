"""
Environment checker for the Big Data Engineering course.
Run: python setup/check_environment.py
"""

import sys
import importlib
import shutil

REQUIRED = {
    "pyspark": "PySpark (distributed processing)",
    "dask": "Dask (parallel computing)",
    "distributed": "Dask Distributed (scheduler)",
    "xarray": "Xarray (multi-dimensional arrays)",
    "pandas": "Pandas (data manipulation)",
    "numpy": "NumPy (numerical computing)",
    "pyarrow": "PyArrow (columnar data / Parquet)",
    "boto3": "Boto3 (AWS SDK)",
    "geopandas": "GeoPandas (geospatial DataFrames)",
    "matplotlib": "Matplotlib (visualization)",
    "duckdb": "DuckDB (embedded analytics)",
    "pytest": "Pytest (testing)",
}

OPTIONAL = {
    "rioxarray": "RioXarray (raster I/O)",
    "netCDF4": "netCDF4 (climate data format)",
    "folium": "Folium (interactive maps)",
    "great_expectations": "Great Expectations (data quality)",
    "delta": "Delta Lake (table format)",
}


def check_packages(packages, required=True):
    results = []
    for pkg, desc in packages.items():
        try:
            mod = importlib.import_module(pkg)
            version = getattr(mod, "__version__", "unknown")
            results.append((pkg, desc, version, True))
        except ImportError:
            results.append((pkg, desc, None, False))
    return results


def main():
    print("Big Data Engineering Course — Environment Check")
    print("=" * 60)
    print(f"Python: {sys.version}")
    print(f"Java:   ", end="")
    java = shutil.which("java")
    print(f"{'Found at ' + java if java else 'NOT FOUND (required for Spark)'}")
    print()

    print("Required Packages:")
    print("-" * 60)
    required_results = check_packages(REQUIRED)
    all_ok = True
    for pkg, desc, version, ok in required_results:
        status = f"v{version}" if ok else "MISSING"
        icon = "OK" if ok else "!!"
        print(f"  [{icon}] {desc:<40} {status}")
        if not ok:
            all_ok = False

    print()
    print("Optional Packages:")
    print("-" * 60)
    optional_results = check_packages(OPTIONAL, required=False)
    for pkg, desc, version, ok in optional_results:
        status = f"v{version}" if ok else "not installed"
        icon = "OK" if ok else "--"
        print(f"  [{icon}] {desc:<40} {status}")

    print()
    print("=" * 60)
    if all_ok:
        print("All required packages are installed. You're ready to go!")
    else:
        missing = [pkg for pkg, _, _, ok in required_results if not ok]
        print(f"Missing required packages: {', '.join(missing)}")
        print("Run: conda env create -f environment.yml")
        print(" or: pip install -r requirements.txt")
    print("=" * 60)

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
