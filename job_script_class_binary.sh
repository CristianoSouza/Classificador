#!/bin/bash
#SBATCH -p 7d
#SBATCH -t 7-00:00:00
#SBATCH --job-name=pre_binary
#SBATCH -o pre_script_binary_class.out
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=cristianoantonio.souza10@gmail.com
#SBATCH -n 1	 
export PATH="/home/wzalewski/anaconda3/bin:$PATH"
source activate py27tensorflow
srun python script_binary_class.py
