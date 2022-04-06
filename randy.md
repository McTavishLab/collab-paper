# Randy's Collab Paper Lab Notebook

## February 23, 2022

- Today we fixed an error with my git permissions, I was not able to git pull. We added the full paths onto my SBATCH script.
- We were also able to fix my error with my alignment file by deleting the ending of the file using nano (CHARSET) and using the GitHub tutorial to do this that luna shared.
- We also started a lab notebook in markdown and set up for the next meeting where we will analyze the job submission results and subsequently use BLAST.

## Updating the _`Mantis`_ phylogeny

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
time physcraper_run.py --study_id pg_1988 --tree_id tree4074 --alignment /home/rposada3/branchinecta/shared/collab-paper/M11113-modified.nex --aln_schema nexus -db /branchinecta/shared/local_blast_db/ --search_taxon ott:641494 -o /branchinecta/shared/collab-paper/linked_dir/randy-mantis-2022-02-23
```
### Job ID

- awaiting submission results
```
Submitted batch job 2419116
```

## Updating the _`Mantodea`_ phylogeny
# This will be re-ran for the order Mantodea

```
cd mctavishlab.github.io/
cd /branchinecta
cd shared/
export PATH=/branchinecta/shared/bin:$PATH
source /branchinecta/shared/venv-physcraper/bin/activate
cd /branchinecta/shared/
find_trees.py -t mantodea -tb -o mantodea.txt
```
## OTT id 656293

```
Members of mantodea present in the following studies in the OpenTree Phylesystem
Only returning studies with TreeBase links

Study pg_1988 tree(s) tree4074
OpenTreeUrl: https://tree.opentreeoflife.org/curator/study/view/pg_1988
Reference: Svenson, G.J., & Whiting M. 2009. Reconstructing the origins of praying mantises (Dictyoptera, Mantodea): the roles of Gondwanan vicariance and morphological convergence. Cladistics 25 (5): 468-514.
Data Deposit URL: http://purl.org/phylo/treebase/phylows/study/TB2:S12224

Study pg_2446 tree(s) tree5216, tree5219, tree5218, tree5217, tree5220
OpenTreeUrl: https://tree.opentreeoflife.org/curator/study/view/pg_2446
Reference: Whiting M., Carpenter J., Wheeler Q., & Wheeler W. 1997. The strepsiptera problem: phylogeny of the holometabolous insect orders inferred from 18S and 28S ribosomal DNA sequences and morphology. Systematic Biology, 46(1): 1-68.
Data Deposit URL: http://purl.org/phylo/treebase/phylows/study/TB2:S382

Study pg_1562 tree(s) tree3124
OpenTreeUrl: https://tree.opentreeoflife.org/curator/study/view/pg_1562
Reference: Damgaard J., Klass K., Picker M.D., & Buder G. 2008. Phylogeny of the Heelwalkers (Insecta: Mantophasmatodea) based on mtDNA sequences, with evidence for additional taxa in South Africa. Molecular Phylogenetics and Evolution, 47: 443-462.
Data Deposit URL: http://purl.org/phylo/treebase/phylows/study/TB2:S12943
```
