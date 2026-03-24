# Big Data Engineering: Spark, Dask & AWS
## End-to-End Course with Real-World Projects

**Author:** Firman Hadi, Ph.D.
**Duration:** 12 Weeks (Full Semester)
**Format:** Interactive HTML (theory) + Jupyter Notebooks (hands-on labs)
**Approach:** Local-first, cloud-optional

---

## Course Philosophy

Every module uses **real open datasets** from different domains. Students build progressively toward a **capstone project** that integrates all three technologies into a complete data pipeline. The course follows a "learn by building" approach — no toy examples.

---

## Datasets Used

| Dataset | Domain | Format | Size | Source |
|---------|--------|--------|------|--------|
| NYC Yellow Taxi Trips | Transportation | Parquet/CSV | ~2-3 GB/year | NYC TLC |
| CHIRPS Rainfall | Climate | NetCDF/GeoTIFF | ~1-6 GB | CHC UCSB |
| NYC PLUTO Property | Housing | CSV/Shapefile | ~200 MB | NYC Planning |
| WHO Global Health Observatory | Epidemiology | CSV/JSON (API) | Variable | WHO |
| EPA Air Quality (AQS) | Environment | CSV | ~1-5 GB | US EPA |
| US Census / ACS | Demographics | CSV/API | ~500 MB | Census Bureau |
| OpenStreetMap Extracts | Geospatial | PBF/Shapefile | 1-10 GB | Geofabrik |
| ERA5 Climate Reanalysis | Climate | NetCDF/GRIB | Variable | Copernicus CDS |

All datasets are freely available without authentication (ERA5 requires a free account).

---

## Repository Structure

```
spark-dask-aws-course/
├── README.md                        # Course overview & setup
├── COURSE_PLAN.md                   # This document
├── index.html                       # Interactive HTML site (theory)
├── environment.yml                  # Conda environment
├── requirements.txt                 # pip requirements
├── setup/
│   ├── check_environment.py         # Verify setup
│   ├── download_datasets.py         # Automated dataset downloader
│   └── localstack_setup.sh          # Optional: LocalStack for AWS sim
│
├── data/
│   ├── README.md                    # Data dictionary & download instructions
│   ├── sample/                      # Small samples for quick testing (<50 MB)
│   └── .gitkeep                     # Full data downloaded by script
│
├── notebooks/
│   ├── week-01-foundations/
│   ├── week-02-spark-core/
│   ├── week-03-spark-advanced/
│   ├── week-04-dask-core/
│   ├── week-05-dask-advanced/
│   ├── week-06-aws-essentials/
│   ├── week-07-data-pipelines/
│   ├── week-08-optimization/
│   ├── week-09-streaming-realtime/
│   ├── week-10-integration/
│   ├── week-11-capstone-build/
│   └── week-12-capstone-present/
│
├── src/                             # Reusable pipeline code
│   ├── __init__.py
│   ├── ingestion/
│   ├── transformation/
│   ├── quality/
│   └── utils/
│
├── pipelines/                       # Complete pipeline scripts
│   ├── taxi_analytics/
│   ├── climate_monitoring/
│   ├── property_assessment/
│   └── capstone/
│
├── tests/                           # Unit & integration tests
│   ├── test_ingestion.py
│   ├── test_transformations.py
│   └── test_quality.py
│
├── infrastructure/                  # AWS templates (optional)
│   ├── cloudformation/
│   ├── terraform/
│   └── emr_configs/
│
└── docs/                            # Additional references
    ├── cheatsheets/
    ├── architecture_diagrams/
    └── troubleshooting.md
```

---

## Week-by-Week Curriculum

### PHASE 1: FOUNDATIONS (Weeks 1-3)

---

### Week 1 — Environment Setup & Big Data Concepts
**Dataset:** NYC Yellow Taxi (sample: 100K rows)

**Theory (HTML):**
- What makes data "big" — when pandas breaks
- The distributed computing mental model: driver, executors, partitions
- Lazy vs eager evaluation across frameworks
- Course roadmap and project overview

**Lab Notebooks:**
1. `01a_environment_setup.ipynb` — Install PySpark, Dask, boto3; verify environment
2. `01b_pandas_limits.ipynb` — Load progressively larger taxi CSVs until pandas fails; measure memory/time
3. `01c_first_spark_session.ipynb` — Same taxi data in Spark; observe lazy DAG; compare speed
4. `01d_first_dask_pipeline.ipynb` — Same taxi data in Dask; compare API similarity to pandas

**Learning Outcomes:**
- Articulate when distributed computing is necessary
- Set up a working local environment for Spark and Dask
- Load and inspect data in both frameworks

---

### Week 2 — Spark Core: DataFrames, SQL & Transformations
**Dataset:** NYC Yellow Taxi (full year: ~60M rows)

**Theory (HTML):**
- SparkSession architecture: driver, executors, cluster manager
- DataFrame API: select, filter, withColumn, groupBy, agg
- Spark SQL: temp views, window functions, CTEs
- Catalyst optimizer: logical plan → physical plan → code generation
- Partitioning strategies and their impact

**Lab Notebooks:**
1. `02a_taxi_exploration.ipynb` — Schema inspection, null handling, type casting on full taxi dataset
2. `02b_transformations.ipynb` — Feature engineering: trip duration, speed, fare per mile, time buckets
3. `02c_aggregations_sql.ipynb` — Revenue by zone, hourly demand patterns, top routes via SQL
4. `02d_spark_ui.ipynb` — Reading the Spark UI: stages, tasks, shuffle, DAG visualization

**Learning Outcomes:**
- Perform complex transformations on millions of rows
- Write equivalent logic in DataFrame API and Spark SQL
- Use the Spark UI to understand execution plans

---

### Week 3 — Spark Advanced: Joins, UDFs & I/O Formats
**Datasets:** NYC Taxi + NYC PLUTO Property + US Census/ACS

**Theory (HTML):**
- Join strategies: broadcast, sort-merge, shuffle hash
- When to use UDFs vs built-in functions (and the performance cost)
- File formats deep-dive: CSV vs Parquet vs Delta vs ORC
- Partitioned writes and predicate pushdown
- Data skew detection and mitigation

**Lab Notebooks:**
1. `03a_spatial_join.ipynb` — Join taxi pickups to PLUTO zones; enrich with property values
2. `03b_demographic_join.ipynb` — Join census demographics to taxi zones; analyze equity patterns
3. `03c_file_formats.ipynb` — Write same data as CSV, Parquet, Delta; compare size, read speed, schema evolution
4. `03d_optimization.ipynb` — Detect and fix data skew; broadcast joins; partition tuning

**Learning Outcomes:**
- Choose the right join strategy based on data characteristics
- Select appropriate file formats for different use cases
- Diagnose and resolve common Spark performance issues

---

### PHASE 2: DASK & SCIENTIFIC DATA (Weeks 4-5)

---

### Week 4 — Dask Core: DataFrames, Delayed & Distributed
**Dataset:** EPA Air Quality (multi-year hourly readings)

**Theory (HTML):**
- Dask architecture: scheduler, workers, task graph
- Dask DataFrame vs pandas: what works, what doesn't
- dask.delayed for custom parallel workflows
- Distributed scheduler vs synchronous vs threaded
- The Dask Dashboard: progress, profile, memory

**Lab Notebooks:**
1. `04a_air_quality_load.ipynb` — Load multi-year EPA CSVs with glob; lazy operations; .compute()
2. `04b_timeseries_analysis.ipynb` — Resample hourly to daily/monthly; rolling averages; seasonal decomposition
3. `04c_delayed_custom.ipynb` — Custom ETL with dask.delayed: download → clean → validate → write
4. `04d_distributed_dashboard.ipynb` — Launch LocalCluster; profile tasks; identify bottlenecks

**Learning Outcomes:**
- Process larger-than-memory tabular data with Dask
- Build custom parallel workflows with dask.delayed
- Monitor and debug distributed computations

---

### Week 5 — Dask Advanced: Xarray, Geospatial & Multi-Dimensional Data
**Datasets:** CHIRPS Rainfall + ERA5 Climate Reanalysis

**Theory (HTML):**
- Multi-dimensional data: why DataFrames aren't enough
- Xarray data model: DataArray, Dataset, coordinates, dimensions
- Chunking strategies: time vs space; optimal chunk sizes (100-500 MB)
- Dask + Xarray integration: lazy loading NetCDF/Zarr
- Cloud-Optimized formats: Zarr, COG, kerchunk

**Lab Notebooks:**
1. `05a_xarray_intro.ipynb` — Open CHIRPS NetCDF; explore dimensions, coords, attributes
2. `05b_climate_analysis.ipynb` — Spatial subsetting (.sel); temporal resampling; anomaly detection
3. `05c_era5_multidim.ipynb` — Open ERA5 multi-variable dataset; pressure level analysis; wind patterns
4. `05d_dask_xarray.ipynb` — Chunk optimization; parallel computation on global grids; write to Zarr

**Learning Outcomes:**
- Work with multi-dimensional scientific datasets
- Choose optimal chunking strategies for different access patterns
- Build a drought/flood detection pipeline from raw climate data

---

### PHASE 3: CLOUD & PIPELINES (Weeks 6-8)

---

### Week 6 — AWS Essentials: S3, IAM & Data Lake Foundations
**Dataset:** Any previously used dataset → upload to S3

**Theory (HTML):**
- AWS Free Tier: what's included, cost guardrails
- S3 deep-dive: buckets, prefixes, storage classes, lifecycle policies
- IAM fundamentals: users, roles, policies (least privilege)
- Data Lake architecture: raw → curated → analytics zones
- Cloud-Optimized formats: Parquet on S3, COG, Zarr stores

**Lab Notebooks:**
1. `06a_s3_basics.ipynb` — Create bucket; upload/download with boto3; list objects; presigned URLs
2. `06b_data_lake_zones.ipynb` — Organize data into raw/curated/analytics prefixes; lifecycle policies
3. `06c_spark_on_s3.ipynb` — Read/write Parquet from S3 with PySpark (local mode + s3a://)
4. `06d_cost_estimation.ipynb` — Estimate storage and transfer costs for your datasets

**Note:** All labs can run locally with [LocalStack](https://localstack.cloud/) for S3 simulation. Instructions for both real AWS and LocalStack provided.

**Learning Outcomes:**
- Set up a well-organized data lake on S3
- Read/write data from Spark and Dask to cloud storage
- Estimate and control cloud costs

---

### Week 7 — Building Data Pipelines: ETL, Quality & Orchestration
**Dataset:** WHO Global Health + EPA Air Quality (multi-source integration)

**Theory (HTML):**
- ETL vs ELT: when and why
- Data quality dimensions: completeness, accuracy, consistency, timeliness
- Schema evolution and backward compatibility
- Pipeline orchestration patterns: sequential, fan-out, conditional
- Idempotency and exactly-once processing

**Lab Notebooks:**
1. `07a_ingestion_patterns.ipynb` — API ingestion (WHO GHO), file ingestion (EPA CSV), schema validation
2. `07b_data_quality.ipynb` — Build quality checks: null rates, range validation, cross-source consistency
3. `07c_transformation_pipeline.ipynb` — Multi-stage pipeline: ingest → validate → clean → enrich → write
4. `07d_testing_pipelines.ipynb` — Unit testing Spark transformations with pytest; test fixtures; CI patterns

**Learning Outcomes:**
- Design robust ETL/ELT pipelines with quality gates
- Implement data quality checks programmatically
- Write testable, maintainable pipeline code

---

### Week 8 — Performance Optimization & Resource Management
**Dataset:** NYC Taxi (full multi-year) + PLUTO (stress testing at scale)

**Theory (HTML):**
- Spark tuning: executor memory, cores, parallelism, shuffle partitions
- Dask tuning: worker memory, nthreads, chunk sizes
- Caching strategies: when to persist vs recompute
- Predicate pushdown, column pruning, partition pruning
- Profiling tools: Spark UI, Dask Dashboard, py-spy

**Lab Notebooks:**
1. `08a_spark_tuning.ipynb` — Experiment with configurations; measure impact on taxi aggregations
2. `08b_dask_tuning.ipynb` — Worker scaling; memory management; adaptive scaling
3. `08c_caching_strategies.ipynb` — .cache() vs .persist() vs recompute; memory vs disk tradeoffs
4. `08d_benchmarking.ipynb` — Build a benchmarking harness; compare Spark vs Dask vs pandas at different scales

**Learning Outcomes:**
- Tune Spark and Dask for specific workloads
- Make informed decisions about caching and resource allocation
- Benchmark and compare framework performance

---

### PHASE 4: ADVANCED TOPICS & INTEGRATION (Weeks 9-10)

---

### Week 9 — Streaming, Real-Time & Event-Driven Architectures
**Dataset:** Simulated real-time taxi feed + EPA hourly sensor data

**Theory (HTML):**
- Batch vs streaming vs micro-batch
- Spark Structured Streaming: triggers, watermarks, output modes
- Event-driven pipelines: AWS Lambda + S3 events
- Exactly-once semantics and checkpointing
- When streaming is overkill (and batch is fine)

**Lab Notebooks:**
1. `09a_structured_streaming.ipynb` — Simulate taxi stream from files; sliding window aggregations
2. `09b_stream_processing.ipynb` — Real-time anomaly detection on sensor data; trigger alerts
3. `09c_lambda_events.ipynb` — S3 event → Lambda → process → write (optional: real AWS or LocalStack)
4. `09d_stream_vs_batch.ipynb` — Same analytics as batch vs stream; compare complexity, latency, cost

**Learning Outcomes:**
- Build streaming pipelines with Spark Structured Streaming
- Design event-driven architectures with Lambda
- Choose between batch and streaming for a given use case

---

### Week 10 — Full Integration: Multi-Framework Pipelines
**Datasets:** All datasets combined

**Theory (HTML):**
- Choosing the right tool: decision framework (Spark vs Dask vs pandas)
- Hybrid architectures: Dask for science, Spark for ETL, pandas for reporting
- AWS Glue, Athena, EMR: managed services overview
- Data catalog and metadata management
- Architecture patterns: Lambda, Kappa, medallion

**Lab Notebooks:**
1. `10a_decision_framework.ipynb` — Decision tree: given data size, format, team skills → choose framework
2. `10b_hybrid_pipeline.ipynb` — Ingest (Spark) → Transform (Spark) → Analyze (Dask+Xarray) → Report (pandas)
3. `10c_athena_queries.ipynb` — Query Parquet on S3 with Athena (or DuckDB locally); compare with Spark SQL
4. `10d_architecture_design.ipynb` — Design doc: architect a pipeline for a given scenario (group exercise)

**Learning Outcomes:**
- Select the right framework for each pipeline stage
- Build pipelines that leverage multiple frameworks
- Design and document data architectures

---

### PHASE 5: CAPSTONE PROJECT (Weeks 11-12)

---

### Week 11 — Capstone: Build
**Dataset:** Student's choice (from course datasets or approved alternative)

**Project Requirements:**
1. **Multi-source ingestion** — At least 2 different data sources/formats
2. **Distributed processing** — Use Spark AND/OR Dask (not just pandas)
3. **Data quality** — Implement validation checks with clear pass/fail criteria
4. **Pipeline code** — Modular, tested, documented Python package
5. **Output** — Analytics-ready dataset + at least 3 derived insights
6. **Cloud-ready** — Code that works locally and can be deployed to AWS (even if not actually deployed)

**Suggested Capstone Projects:**

| Project | Datasets | Key Skills |
|---------|----------|------------|
| Urban Mobility & Equity | Taxi + Census + PLUTO | Spark joins, demographic analysis |
| Climate Risk Assessment | CHIRPS + ERA5 + OSM | Dask+Xarray, spatial overlay |
| Air Quality & Health | EPA AQS + WHO + Census | Multi-source ETL, time series |
| Property Value Predictor | PLUTO + Census + OSM + Taxi | Feature engineering, pipeline design |

**Lab Notebooks:**
1. `11a_project_scaffold.ipynb` — Set up project structure, data access, and pipeline skeleton
2. `11b_ingestion_build.ipynb` — Implement data ingestion and quality checks
3. `11c_transformation_build.ipynb` — Core transformations and feature engineering
4. `11d_analysis_build.ipynb` — Generate insights and output datasets

---

### Week 12 — Capstone: Polish, Test & Present

**Lab Notebooks:**
1. `12a_testing.ipynb` — Write and run tests; validate outputs; edge case handling
2. `12b_documentation.ipynb` — Write README, architecture diagram, data dictionary
3. `12c_optimization.ipynb` — Profile and optimize; document performance characteristics
4. `12d_presentation.ipynb` — Create a notebook-based presentation of findings

**Deliverables:**
- Working pipeline code (src/ + pipelines/)
- Test suite with >80% pass rate
- Architecture diagram (Mermaid or draw.io)
- 10-minute presentation notebook
- Reflection: what worked, what you'd change, next steps

---

## Assessment & Progress Tracking

| Component | Weight | Description |
|-----------|--------|-------------|
| Weekly Labs | 40% | 4 notebooks per week, auto-graded where possible |
| Quizzes | 10% | One quiz per theory module (in HTML site) |
| Midterm Pipeline | 20% | Week 7-8: complete working pipeline from ingestion to output |
| Capstone Project | 30% | Weeks 11-12: end-to-end project |

---

## Prerequisites

- Python proficiency (functions, classes, list comprehensions)
- Basic pandas (read_csv, groupby, merge)
- Command line basics (cd, ls, pip install)
- Optional: SQL fundamentals (SELECT, JOIN, GROUP BY)

---

## Environment Setup

```bash
# Option 1: Conda (recommended)
conda env create -f environment.yml
conda activate bigdata-course

# Option 2: pip
python -m venv bigdata-env
source bigdata-env/bin/activate  # Windows: bigdata-env\Scripts\activate
pip install -r requirements.txt

# Verify
python setup/check_environment.py
```

### Core Dependencies
- Python 3.10+
- PySpark 3.5+
- Dask[complete] 2024.1+
- Xarray + netCDF4
- boto3 + s3fs
- JupyterLab
- pytest
- DuckDB (Athena alternative for local)

### Optional (Cloud)
- AWS CLI v2
- LocalStack (for S3 simulation)
- Terraform (for infrastructure-as-code)

---

## How to Use This Course

### Self-Paced Learners
Follow the weeks sequentially. Each week has ~4 hours of content (1h theory + 3h labs). Budget 12 weeks at 4-6 hours/week.

### Instructors
The HTML site serves as lecture material. Notebooks are homework/lab assignments. Midterm and capstone provide structured assessments.

### Working Professionals
Cherry-pick by phase. If you know Spark, skip to Phase 2 (Dask). If you know both, jump to Phase 3 (Cloud & Pipelines).

---

## License

Course materials: CC BY-SA 4.0
Code: MIT License
Datasets: See individual dataset licenses in data/README.md
