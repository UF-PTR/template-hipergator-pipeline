# PIPELINE-NAME

> One sentence: what goes in, what comes out.

**Status:** 🚧 in development · ✅ ready (someone who didn't write it has run the example without asking)
**Lab:** Lastname Lab, UF Pharmacotherapy and Translational Research
**Maintainer:** Your Name (you@ufl.edu)
**Paper:** (DOI once available)

> [!CAUTION]
> **🚫 NO PHI OR IDENTIFIABLE DATA.** This repo holds code only. Real data stays in UF-approved storage; `data/` is for a small de-identified example at most. See the [UF-PTR data policy](https://github.com/UF-PTR#-no-phi-or-identifiable-data--ever).

## I want to run it

No terminal needed. Open [HiPerGator OnDemand](https://ondemand.rc.ufl.edu), start a Jupyter session, open `notebooks/run_me.ipynb`, fill in the three lines in the first cell, **Run All**. You'll get an email when it finishes.

Full walkthrough with screenshots: [`docs/RUN_ON_HIPERGATOR.md`](docs/RUN_ON_HIPERGATOR.md).

**Inputs:** (describe: file format, where they usually live)
**Outputs:** (describe: what lands in the output folder)
**Runtime:** about N hours on the example data.

## I want to change it

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version: the notebook is the user interface and never changes; the science lives in `scripts/run_pipeline.py`; `slurm/run.slurm` is the glue. Keep that split and nothing you change will break a user.

```
notebooks/run_me.ipynb      the only thing users touch
docs/RUN_ON_HIPERGATOR.md   no-terminal walkthrough
scripts/run_pipeline.py     the actual pipeline
slurm/run.slurm             job script the notebook submits
config.example.yml          every tunable, with defaults
environment.yml             conda environment
example/                    a small input and its expected output
```

## Citing

See `CITATION.cff` or click *Cite this repository*.
