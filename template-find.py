#! /bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10G
#
#SBATCH --partition mctavish.q
#SBATCH --time=0-02:1000:00     # 2 days 1000 minutes
#
  #SBATCH --output=USERNAME-TAXONNAME-YEAR-MONTH-DAY.stdout
#SBATCH --error=USERNAME-TAXONNAME-YEAR-MONTH-DAY.stderr
#

#SBATCH --export=ALL

pwd
## Add dependcies to PATH
export PATH=/branchinecta/shared/bin:$PATH
## Activate virtual env
source /branchinecta/shared/venv-physcraper/bin/activate
## Move to folder containing inputs (or where you want to save outputs)
cd /branchinecta/shared/
pwd
echo "Starting Physcraper TAXONNAME find studies"

find_trees.py -t TAXONNAME -tb -o TAXONNAME.txt
