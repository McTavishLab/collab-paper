# Randy's Collab Paper Lab Notebook

##February 23, 2022

- Today we fixed an error with my git permissions, I was not able to git pull. and we added the full paths onto my sbatch script.
- We were able to fix my error with my alignment file by deleting the ending of the file using nano (CHARSET) and using the GitHub tutorial to do this that luna shared.
- We also started a lab notebook in markdown and set up for the next meeting where we will analyze the job submission results and use BLAST.≈

## I am working on updating a phylogeny of the genus _mantis_

```
cd mctavishlab.github.io/
cd /branchinecta
cd shared/
export PATH=/branchinecta/shared/bin:$PATH
source /branchinecta/shared/venv-physcraper/bin/activate
cd /branchinecta/shared/
find_trees.py -t mantis -tb -o mantis.txt
```
### OTT id 641494

### Study pg_1988 tree(s) tree4074

```
OpenTreeUrl: https://tree.opentreeoflife.org/curator/study/view/pg_1988
Reference: Svenson, G.J., & Whiting M. 2009. Reconstructing the origins of praying mantises (Dictyoptera, Mantodea): the roles of Gondwanan vicariance and morphological convergence. Cladistics 25 (5): 468-514.
Data Deposit URL: http://purl.org/phylo/treebase/phylows/study/TB2:S12224
``` 
### Using the above tree that I found, I then used the following physcraper command

```
time physcraper_run.py --study_id pg_1988 --tree_id tree4074 --alignment linked_dir/alignments/ALIGNMENT.nex --aln_schema nexus -db ../local_blast_db_OLD/ --search_taxon ott:641494 -o /collab-paper/linked_dir/randy-mantis-2022-02-02
```
### Submission Script

```
#! /bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=10G
#
#SBATCH --partition mctavish.q
#SBATCH --time=0-02:1000:00     # 2 days 1000 minutes
#
  #SBATCH --output=rposada3-mantis-2022-02-23.stdout
#SBATCH --error=rposada3-mantis-2022-02-23.stderr
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
echo "Starting Physcraper Mantis run"
time physcraper_run.py --study_id pg_1988 --tree_id tree4074 --alignment /home/rposada3/branchinecta/shared/collab-paper/M11113-modified.nex --aln_schema nexus -db /branchinecta/shared/local_blast_db_OLD/ --search_taxon ott:641494 -o /branchinecta/shared/collab-paper/linked_dir/randy-mantis-2022-02-23
```
### Job ID

- awaiting submission results
```
Submitted batch job 2419116
```
