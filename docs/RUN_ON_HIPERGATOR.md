# Running PIPELINE-NAME on HiPerGator (no terminal)

Time: about 10 minutes the first time, 2 minutes after that.

## Before you start

- A HiPerGator account in your lab's allocation. If you don't have one, your PI requests it at [rc.ufl.edu](https://www.rc.ufl.edu/get-started/).
- Your input files somewhere under `/blue/<your-group>/`. Ask your PI if you're unsure where.

## 1. Get the code (first time only)

1. Open [ondemand.rc.ufl.edu](https://ondemand.rc.ufl.edu) and sign in with your GatorLink.
2. Top menu → **Clusters → HiPerGator Shell Access**. A black terminal opens in the browser. This is the only time you'll see one.
3. Paste this, replacing `GROUP` and `USER`, and press Enter:
   ```
   cd /blue/GROUP/USER && git clone https://github.com/UF-PTR/PIPELINE-NAME.git
   ```
4. Close the terminal tab.

_[screenshot: OnDemand top menu with Clusters highlighted]_

## 2. Open a Jupyter session

1. OnDemand top menu → **Interactive Apps → Jupyter Notebook**.
2. Fill in: **Account** = your group, **QOS** = your group, **Cores** = 1, **Memory** = 4 GB, **Time** = 1 hour. (This is just for the notebook; the real job requests its own resources.)
3. **Launch**. Wait for the card to say *Running*, then **Connect to Jupyter**.

_[screenshot: the Jupyter launch form with the fields filled in]_

## 3. Run it

1. In the Jupyter file browser, go to `blue/GROUP/USER/PIPELINE-NAME/notebooks/` and open **`run_me.ipynb`**.
2. In the first cell, change the three lines: where your inputs are, where you want results, your email.
3. Menu → **Run → Run All Cells**.
4. The last cell prints `Submitted batch job 12345678`. You can close everything now.
5. You'll get an email when it finishes. Results are in the folder you chose.

_[screenshot: the first cell with the three lines highlighted]_

## If something goes wrong

| What you see | What to do |
|---|---|
| `INPUT_DIR not found` | The path has a typo, or the folder is on your laptop rather than HiPerGator. Paths must start with `/blue/`. |
| `sbatch failed ... Invalid account` | The `--account`/`--qos` in `slurm/run.slurm` don't match your group. Ask the maintainer to fix, or edit the two lines yourself. |
| `sbatch failed ... command not found` | You're not on HiPerGator (e.g. running the notebook locally). |
| Email says **FAILED** | Open `logs/PIPELINE-NAME_<jobid>.err` in Jupyter and send it to the maintainer. |
| Job stuck in `PD` for hours | Normal under heavy load. Burst QOS (`GROUP-b`) is often faster: edit `--qos` in `slurm/run.slurm`. |
| Kernel not found when opening the notebook | Pick **Python 3** when asked. If it still fails, see `docs/KERNEL_SETUP.md`. |

Maintainer: **MAINTAINER-NAME (maintainer@ufl.edu)**
