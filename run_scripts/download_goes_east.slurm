#!/bin/bash
#SBATCH --job-name=goes_east         # Job name
#SBATCH --partition=normal               # Partition (queue) name
#SBATCH --nodes=1                       # Number of nodes
#SBATCH --ntasks=10                     # Number of tasks (processes)
#SBATCH --time=01:00:00                 # Time limit hrs:min:sec
#SBATCH --output=goes_download_%j.log   # Standard output and error log

module load Anaconda3                    # Load Anaconda module if required
MAIN_DIR="/home/jmframe/goes/"
source activate "${MAIN_DIR}jmframe/.conda/envs/py_goes"

# Run the download script
python3 -u "${MAIN_DIR}src/downloadgoes.py" "${MAIN_DIR}configs/config_east.yml"