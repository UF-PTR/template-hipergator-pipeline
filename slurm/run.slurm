#!/bin/bash
#SBATCH --job-name=PIPELINE-NAME
#SBATCH --account=GROUP
#SBATCH --qos=GROUP
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16gb
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --mail-type=END,FAIL
# --mail-user and --export=CONFIG are supplied by the notebook at submit time.

set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
mkdir -p logs

echo "job $SLURM_JOB_ID on $(hostname) at $(date)"
echo "config: ${CONFIG:?CONFIG not set — submit via the notebook or: sbatch --export=CONFIG=path slurm/run.slurm}"

module purge
module load conda
conda activate PIPELINE-NAME-env

python scripts/run_pipeline.py --config "$CONFIG"

echo "finished at $(date)"
