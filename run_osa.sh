#!/bin/bash
#SBATCH -p defq
#SBATCH --job-name=OSA_JOB
#SBATCH --mem=30G
#SBATCH -o OSA.o
#SBATCH -e OSA.e
#SBATCH --time=1-48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
source /home/${USER}/.bashrc
source activate streamline
srun python run_osa.py
