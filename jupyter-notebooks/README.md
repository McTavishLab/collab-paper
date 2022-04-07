# Creating a jupyter notebook

## Launching Jupyter

First things first, decide whether you want to work on the repo from the cluster or from your own computer.

Then, make sure you are in the directory you want to work with:

```
cd path/to/your/repo
```

### If you chose to work from your own computer

Once you changed directory to the appropriate folder, you can start jupyter with the command

```
jupyter notebook
```

And... you are done!

### If you chose to work from the cluster

This option is a bit more involved, but very doable. Many thanks to @LuciaBazanW for this tip!

Once you have `ssh`-ed into the cluster and changed to the appropriate repo, go ahead and start anaconda, which has jupyter:

```
module load anaconda3
```

Export anaconda's path so the cluster knows where to find it:

```
export PATH=$HOME/anaconda3/bin:$PATH
```

Launch jupyter without an interface:

```
jupyter notebook --no-browser --port=8080
```

Open another terminal window, and ssh into the cluster again with:

```
ssh -L 8080:localhost:8080  REPLACE-WITH-YOUR-USER-NAME@merced.ucmerced.edu
```

Open a window from the web browser that you prefer (for example, Safari, Chrome, etc.)
Go to `http://localhost:8080/` or any of the URLs provided when you launched jupyter with no interface.

Provide a token if needed.

The jupyter notebook interface should start in your own browser now 🎉 🚀


