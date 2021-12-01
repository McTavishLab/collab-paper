# Running physcraper on the Merced cluster

## Add dependencies to PATH

  export PATH=/branchinecta/shared/bin:$PATH

##Activate virtual env

  source /branchinecta/shared/venv-physcraper/bin/activate

## Move to `brachinecta/shared`
  cd /branchinecta/shared

## Do a Physcraper run

  physcraper_run.py -tf tests/data/tiny_test_example/test.tre -tfs newick -a tests/data/tiny_test_example/test.fas --taxon_info tests/data/tiny_test_example/main.json -as fasta -db /branchinecta/shared/local_blast_db_OLD/ -o owndata
