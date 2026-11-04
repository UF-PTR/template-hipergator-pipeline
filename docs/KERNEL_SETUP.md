# Making the environment visible in Jupyter

The notebook itself only needs plain Python 3 — the standard OnDemand kernel is fine for submitting the job. The conda environment is what the *job* uses, via `slurm/run.slurm`.

## Build the environment (maintainer, once)

From a HiPerGator shell:

```bash
module load conda
conda env create -f environment.yml          # creates PIPELINE-NAME-env
```

By default this lands in your own `~/.conda/envs`, which only you can use. For a lab-shared environment, create it under `/blue`:

```bash
conda env create -f environment.yml -p /blue/GROUP/share/envs/PIPELINE-NAME-env
```

and change `conda activate PIPELINE-NAME-env` in `slurm/run.slurm` to that full path.

## If someone wants the environment as a Jupyter kernel too

Only needed if a contributor wants to develop interactively in the same environment:

```bash
module load conda
conda activate PIPELINE-NAME-env
python -m ipykernel install --user --name PIPELINE-NAME-env --display-name "PIPELINE-NAME"
```

That registers it for the person who ran the command. Making a kernel visible to everyone in the group is an RC-side setup; see [UF Research Computing's Jupyter docs](https://docs.rc.ufl.edu/) or open a support ticket.
