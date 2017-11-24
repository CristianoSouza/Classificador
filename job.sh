#!/bin/bash
#SBATCH -p 7d
#SBATCH -t 7-00:00:00
#SBATCH --job-name=Exehybrid_tcp
#SBATCH -o hybrid_tcp_attribute.out
#SBATCH -n 1	 
export PATH="/home/wzalewski/anaconda3/bin:$PATH"
source activate py27tensorflow
srun python main.py
