# Turning a working pipeline into a Ready one

The 🚧 → ✅ checklist. "Ready" means someone who didn't write it ran the example without asking you anything.

1. **Find-and-replace the placeholders.** `PIPELINE-NAME`, `GROUP`, `YOUR_USERNAME`, `MAINTAINER-NAME`, `maintainer@ufl.edu`. They appear in the README, notebook, slurm script, and docs.
2. **Put the science in `scripts/run_pipeline.py`.** Keep the interface: it takes `--config file.yml`, reads `input_dir` and `output_dir`, writes into `output_dir`. Add other knobs to the config, never to the command line — the notebook only knows how to pass a config.
3. **Pin the environment.** `environment.yml` lists every package with a version. Build it fresh from the file and confirm the pipeline runs in it (`docs/KERNEL_SETUP.md`).
4. **Set real resources** in `slurm/run.slurm`: cores, memory, time, account, qos. Over-ask slightly; a job that dies at 95% wastes more than a job that holds spare memory.
5. **Make the example real but small.** `example/input/` should run in under 10 minutes. Put what it should produce in `example/expected_output/` so a user can compare.
6. **Fill in `docs/RUN_ON_HIPERGATOR.md`** — the inputs/outputs sections and the screenshots marked `_[screenshot: ...]_`. Take them from a fresh OnDemand session.
7. **Hand it to someone who hasn't seen it.** A labmate, not you. They follow the doc. Every question they ask is a line missing from the doc; add it.
8. **Tag and publish.** When it's used in a paper: make the repo public, create a release (`v1.0.0`), update `CITATION.cff`, and cite the release URL in the paper's code-availability statement. Flip the README status to ✅.

## Keeping it Ready

- Change the science? Re-run the example and update `expected_output/`.
- Change the config keys? Update `config.example.yml` and the docs table.
- Never change the notebook's first cell. That's the contract with users.
