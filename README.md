# H-hat Jupyter Kernel

This is a H-hat spec to be used on jupyter notebook kernel.

## Configuration

You first need to have `ipython` and `jupyter` installed. Recommended through `pip`. And recommended to use `conda` or have a separated virtual environment with `venv`, `virtualenv`, `poetry` or any other method of your choice.

You need to clone [H-hat quantum programming language repo](https://github.com/hhat-lang/hhat_lang) and, on the root folder, run the command on terminal (or powershell):
```bash
python3 -m pip install -e .
```

After that, clone this very repository, go to its root folder and run:
```bash
python3 -m pip install -e .
```

and you run:
```bash
jupyter kernelspec install --user {path to this repo}/hhat_jupyter_kernel/
```

You should see `hhat_jupyter_kernel` when doing:
```bash
jupyter kernelspec list
```

If everything works fine, time to test the H-hat kernel on jupyter. Run:
```bash
jupyter
```

and choose `H-hat` at the language options for the new notebook. Try runing the following in a single cell:

```
main ( int{} a = (:3, :print("a =")) print("hoi quantum!") )
```

This should print:
```
a = 3
hoi quantum!
```


