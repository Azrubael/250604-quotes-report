The project with scripts to automatically generate cryptocurrency quote graphs and so on.


**The suggested order of virtual environment preparation.**

[1] - Install Python 3.10 (or later), pip и python3.10-venv
* https://docs.python.org/3/using/windows.html#launcher
* https://pip.pypa.io/en/stable/installing/
```bash
    apt install python3.10-venv
```


[2] - Create isolated invironment
* For Linux
```bash
    $ python3 -m venv crypto_env
    $ source crypto_env/bin/activate
```
* For Windows
```bash
    $ py -m venv crypto_wenv
    $ .\crypto_wenv\Scripts\activate
```


[3] - Activate virtual environment:

```bash
    $ source crypto_env/bin/activate
```


[4] - Restore dependencies:
```bash
(crypto_env)$ pip install -r dependencies.txt
```


[5] - Start local dev server:
```bash
(crypto_env)$ python ./mysite/manage.py runserver
```


[6] - Create list of dependencies
```bash
(crypto_env)$ pip freeze > dependencies.txt
```


[7] - To deactivate isolated environment
```bash
(crypto_env)$ deactivate
```