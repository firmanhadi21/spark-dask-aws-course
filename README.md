# Big Data Engineering: Spark, Dask & AWS

A 12-week end-to-end course using real-world open datasets across transportation, climate, housing, health, and environmental domains.

**Live theory site →** https://firmanhadi21.github.io/spark-dask-aws-course

## Quick Start

```bash
# 1. Create environment
conda env create -f environment.yml
conda activate bigdata-course

# 2. Verify setup
python setup/check_environment.py

# 3. Download sample data (~200 MB)
python setup/download_datasets.py --mode sample

# 4. Launch Jupyter
jupyter lab notebooks/
```

## Course Structure

| Phase | Weeks | Focus | Datasets |
|-------|-------|-------|----------|
| **Foundations** | 1-3 | Spark core, joins, file formats | NYC Taxi, PLUTO, Census |
| **Dask & Science** | 4-5 | Dask, Xarray, multi-dimensional data | EPA Air Quality, CHIRPS, ERA5 |
| **Cloud & Pipelines** | 6-8 | AWS, ETL, optimization | Multi-source integration |
| **Advanced** | 9-10 | Streaming, multi-framework pipelines | Simulated streams, all datasets |
| **Capstone** | 11-12 | End-to-end project | Student's choice |

Each week includes theory (interactive HTML site) and 4 hands-on Jupyter notebooks.

## Approach

- **Local-first**: Everything runs on your laptop. AWS modules are optional with clear cost warnings.
- **Real data**: No toy examples. Every lab uses open datasets you'd encounter professionally.
- **Progressive complexity**: Start with single-file pandas, end with multi-source distributed pipelines.

See [COURSE_PLAN.md](COURSE_PLAN.md) for the detailed curriculum.

## Repository Layout

```
notebooks/          # 48 Jupyter notebooks (4 per week × 12 weeks)
src/                # Reusable pipeline modules
pipelines/          # Complete pipeline scripts
data/               # Dataset storage (downloaded via script)
setup/              # Environment & data setup utilities
infrastructure/     # AWS templates (optional)
docs/               # Cheatsheets & architecture diagrams
index.html          # Interactive theory site
```

## Author

**Firman Hadi, Ph.D.**
Lecturer, Dept. of Geodetic Engineering, Universitas Diponegoro
https://firmanhadi21.github.io

## License

Course materials: CC BY-SA 4.0 | Code: MIT
