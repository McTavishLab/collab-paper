# Creating a jupyter notebook

## Launching Jupyter

### From the cluster

Many thanks to @LuciaBazanW for this tip!

Start anaconda, which has jupyter:

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

Open a web browser window that you prefer (for example, Safari, Chrome, etc.)
Go to `http://localhost:8080/` or any of the URLs provided when you launched jupyter with no interface.

Provide a token if needed.

The jupyter notebook interface should start in your own browser now 🎉 🚀


