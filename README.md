# Welcome to the first McTavish Lab collab paper repo!

**Goal of the paper:**

_Develop a Python module to generate informative visualizations of the Physcraper results._

**Name of the module:** TBD

**Resources:**

1. [Physcraper GitHub repo](https://github.com/McTavishLab/physcraper)
1. [Jupyter notebook examples in the Physcraper GitHub repo](https://github.com/McTavishLab/physcraper/tree/main/docs/examples)
1. [Physcraper documentation](https://physcraper.readthedocs.io/en/main/index.html)
1. [Physcraper paper](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-021-04274-6)


## Project log

### March 2, 2022

- Cluster Ticket: git pull permissions for Randy and Kiana, and the rest of us
  - https://stackoverflow.com/questions/6448242/git-push-error-insufficient-permission-for-adding-an-object-to-repository-datab 
- EJM: error reading a DNA file from the database with Kiana’s run
- Md syntax: 
  - create dropdown stuff
  - add emojis
- The Physcraper results structure
- How we visualize the results now
- Starting a Python module
- Writing an ms with backwards design
- Think of good names for the package

### Feb 23, 2022

- Q: Is there a way to increase the run time in the cluster while the job is still running?? - unfortunately, no: 
"this ability is reserved for system admins only. 
If you attempt to update the time limit of a running job, you will receive this error:
`Access/permission denied for job <job id>`.
You can update the time limit of a pending job only:
`scontrol update JobId=<job id> TimeLimit=<dd-hh:mm:ss>`."

- Creating personal workflow files as jupyter notebooks or markdown files. 
  - Markdown files - Success!
  - Jupyter notebook - will work on these later if needed for the Python module.



### Feb 16, 2022

- Overview of cluster errors:
  - Not finding muscle (Lucia) - solved: do not use conda
  - Error accessing collab-paper (Randy) - solved: give full path of genbank database
- Everybody starts a run on the cluster - success!
  - Lucia - Primates
  - Randy - Mantis
  - Kiana - Podarcis
  - Luna - Felis

### Feb 9, 2022

- Summary of Physcraper
- EJM helped figure out errors and we tried running Physcraper again!
- ssh authentication locally
- Git cloning the collab-paper project repository



### Feb 2, 2022

- Overview of Physcraper
- Choose a paper subject - Success!
  - Python module to generate figures
- Running the Physcraper examples and a taxon of your interest on the cluster - People got some errors again



### Dec meeting:

- Running Physcraper on the Merced cluster with conda
- Run Lucia’s example:
  - Download alignment
  - Work on the jupyter notebook: Explain how to modify the alignment to run on Physcraper
- Run this on a physcraper docker locally:
```
time physcraper_run.py 
--study_id pg_2407 
--tree_id tree5076 
-db local_blast_db_OLD 
--search_taxon ott:913935 
--alignment /project/linked_dir/alignments/M585.nex --aln_schema nexus 
--bootstrap_reps 2 
--output /project/linked_dir/luna_lucia_primates
```
Figure out why it is not running on the cluster - office hours?


How to run Physcraper with a local BLAST database
The -db argument
See Kiana’s and other’s research questions
Work on the collab-paper repo
Linking the alignment data folder to physcraper docker
Jasper reaching out to Haemosporida experts

Done:
run docker on the UC server -> we do not need the physcraper docker, EJM is making the install with venv and conda so we can all run it


