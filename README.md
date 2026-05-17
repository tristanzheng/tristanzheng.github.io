This repository is used for the development, maintenance, and deployment of my personal blog. Please visit [Tristan Zheng](https://tristanzheng.github.io/) if you are interested.

## Python Scripts

The helper scripts in `_scripts/` use a local Python virtual environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the image optimizer with:

```sh
python _scripts/optimize_images.py
```
