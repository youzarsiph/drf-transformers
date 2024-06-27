# drf-transformers

[![Ruff Lint](https://github.com/youzarsiph/drf-transformers/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/drf-transformers/actions/workflows/ruff.yml)
[![Black Format](https://github.com/youzarsiph/drf-transformers/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/drf-transformers/actions/workflows/black.yml)
[![Django CI](https://github.com/youzarsiph/drf-transformers/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/drf-transformers/actions/workflows/django.yml)
[![Docker](https://github.com/youzarsiph/drf-transformers/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/youzarsiph/drf-transformers/actions/workflows/docker-publish.yml)
[![Docker Image CI](https://github.com/youzarsiph/drf-transformers/actions/workflows/docker-image.yml/badge.svg)](https://github.com/youzarsiph/drf-transformers/actions/workflows/docker-image.yml)

Django REST Framework AI microservice using Phi 3 from HuggingFace Hub

## Get started

Clone the repo:

```console
git clone https://github.com/youzarsiph/drf-transformers
```

Install `poetry`, a Python tool for building and publishing packages:

```console
python -m pip install poetry
```

Install dependencies:

```console
python -m poetry install
```

Activate virtual environment

```console
python -m poetry env use python
```

Create a new Django project:

```console
python -m django startproject mysite
```

Copy `drf_transformers` to `mysite`:

```console
cp -r drf_transformers mysite/drf_transformers
```

Configure project settings, open `mysite/settings.py`:

```python
...

# Application definition
INSTALLED_APPS = [
    # Add the following lines
    "drf_transformers",
    "drf_redesign",
    "rest_framework",
    ...
]

...
```

Then open `mysite/urls.py`:

```python
...
from django.urls import include, path

urlpatterns = [
    ...
    # Add the following lines
    path("", include("drf_transformers.urls")),
    path("", include("rest_framework.urls")),
]

```

Run `check`:

```console
python manage.py check
```

Create a `.env` file that contains your HuggingFace access token, you may need to create an account on [HuggingFace](https://huggingface.co/):

```bash
# Your HF access token
HF_TOKEN=hf_**********************************

```

Or you can export `HF_TOKEN` env variable.

Now you are ready to go.
