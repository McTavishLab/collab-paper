
# Lucia's collab paper notebook

## February 23, 2022

List of things that we did today:

- We started the lab notebooks using markdown
- We solved Randy's aligment issue
- Kiana, Lucia and Luna got the same error with the blast database, investigate! 

### Updating **Primates** `phylogeny`

I am working on on updating a phylogeny of the order **Primates**
I ran the following command
```
physcraper_run.py --study_id pg_2407 --tree_id tree5076 --search_taxon ott:913935 --alignment /branchinecta/jbazanwilliamson/M585.nex --aln_schema nexus -
-bootstrap_reps 100 -db /branchinecta/shared/local_blast_db --output /branchinecta/shared/collab-paper/linked_dir/LUCIABW-PRIMATES-2022-02-23
```
