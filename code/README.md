# Running a job on the cluster

## 1. If you are outside the UC Merced network, turn your VPN on!

You can only ssh into the cluster from within UC Merced's network

## 2. ssh into the cluster

```
ssh USER-NAME@merced.ucmerced.edu
```

## 3. Create a job submission file.

There is a [template](https://github.com/McTavishLab/collab-paper/blob/main/code/template-find.sub) in this repository.
A submission script for this project looks like this:

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
```
You can create an empty file with:

```
touch my_run.sub
```

And then add all the necessary commands in there by opening it with a text editor, such as nano"

```
nano my_job.sub
```

Alternatively, you can copy the template and then edit the copy file:

```
cp code/template-find.sub my_job.sub
nano myjob.sub
```

## Submit the job

```
sbatch my_job.sub
```

## Check your queue

```
squeue -u username
```

## Check the state of the cluster real time

Use the tool called ganglia! Find it at https://merced.ucmerced.edu/ganglia/

## Find results of your job

```
cat USERNAME-TAXONNAME-YEAR-MONTH-DAY.stdout
```

## Check if anything failed

```
cat USERNAME-TAXONNAME-YEAR-MONTH-DAY.stderr
```


## Use screen to leave work on the background

```
screen
screen -aD
```


## copy a file form your computer into the server

```
scp local/file/address USER-NAME@merced.ucmerced.edu:/destinationfolder/
```

## Copy a file from the server back to your computer

From your own computer, do:

```
rsync username@merced.ucmerced.edu:path/to/file/on/cluster/name .
```

## To finish the cluster connection press Ctrl + d



