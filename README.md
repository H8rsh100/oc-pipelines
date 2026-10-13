# oc-pipelines

**Project name:** oc-pipelines

A sample application used to demonstrate a complete CI/CD pipeline built with
**GitHub Actions**, **Tekton** and **OpenShift Pipelines**.

## Project details

| Field | Value |
| --- | --- |
| Project name | oc-pipelines |
| Application | News aggregation sample app (`app/news.py`) |
| Language | Python 3 |
| Linter | flake8 |
| Unit test runner | nose |
| CI | GitHub Actions (`.github/workflows/workflow.yml`) |
| Task runner | Tekton (`.tekton/tasks.yml`) |
| CD | OpenShift Pipelines (`oc-pipelines-oc-final`, `oc-pipelines-oc-green`) |
| Storage | OpenShift PersistentVolumeClaim |

## Pipeline stages

1. **Lint with flake8** – static analysis of the Python sources.
2. **Run unit tests with nose** – executes the unit tests under `tests/`.
3. **Cleanup task** – Tekton task that removes build leftovers before a run.
4. **Build and deploy** – OpenShift Pipeline `oc-pipelines-oc-final`.

## Repository layout

```
oc-pipelines/
├── README.md
├── .github/
│   └── workflows/
│       └── workflow.yml      # GitHub Actions: flake8 lint + nose tests
├── .tekton/
│   └── tasks.yml             # Tekton tasks: cleanup + nose
├── app/
│   └── news.py               # sample application source
├── tests/
│   └── test_news.py          # nose unit tests
├── requirements.txt
└── setup.cfg                 # flake8 configuration
```

## Running locally

```bash
pip install -r requirements.txt
flake8 app tests
nosetests tests
```
