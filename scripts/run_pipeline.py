#!/usr/bin/env python3
"""
PIPELINE-NAME — the actual pipeline.

Interface (keep this fixed so the notebook never has to change):
    python run_pipeline.py --config CONFIG.yml

CONFIG.yml must contain at least:
    input_dir:  path to inputs
    output_dir: path where results are written
Everything else is optional and documented in config.example.yml.
"""
import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML missing — activate the conda environment (see environment.yml)")


def load_config(path: Path) -> dict:
    with open(path) as f:
        cfg = yaml.safe_load(f) or {}
    for key in ("input_dir", "output_dir"):
        if key not in cfg:
            sys.exit(f"config is missing required key: {key}")
    cfg["input_dir"] = Path(cfg["input_dir"]).expanduser().resolve()
    cfg["output_dir"] = Path(cfg["output_dir"]).expanduser().resolve()
    if not cfg["input_dir"].is_dir():
        sys.exit(f"input_dir does not exist: {cfg['input_dir']}")
    cfg["output_dir"].mkdir(parents=True, exist_ok=True)
    return cfg


def run(cfg: dict) -> None:
    """Replace the body of this function with the real pipeline."""
    inputs = sorted(p for p in cfg["input_dir"].iterdir() if p.is_file())
    print(f"found {len(inputs)} input file(s) in {cfg['input_dir']}")

    # --- example step: count lines in each input, write a summary ---
    summary = cfg["output_dir"] / "summary.tsv"
    with open(summary, "w") as out:
        out.write("file\tlines\n")
        for p in inputs:
            with open(p, errors="ignore") as f:
                n = sum(1 for _ in f)
            out.write(f"{p.name}\t{n}\n")
    print(f"wrote {summary}")
    # ----------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, type=Path)
    args = ap.parse_args()
    cfg = load_config(args.config)
    run(cfg)
    print("done")


if __name__ == "__main__":
    main()
