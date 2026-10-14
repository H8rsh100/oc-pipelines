# cicd-final-project

**Project name:** ci-cd-final-project

A sample application used to demonstrate a complete CI/CD pipeline built with
**GitHub Actions**, **Tekton** and **OpenShift Pipelines**.

## Project details

| Field | Value |
| --- | --- |
| Project name | ci-cd-final-project |
| Repository name | cicd-final-project |
| Application | News aggregation sample app (`app/news.py`) |
| Language | Python 3 |
| Linter | flake8 |
| Unit test runner | nose |
| CI | GitHub Actions (`.github/workflows/workflow.yml`) |
| Task runner | Tekton (`.tekton/tasks.yml`) |
| Pipeline | OpenShift Pipeline `oc-pipelines-oc-final` |
| Storage | OpenShift PersistentVolumeClaim |

## Pipeline stages

1. **Initialize containers** – the job runs inside a container image.
2. **Setup Node.js** – toolchain used by the pipeline tooling.
3. **Lint with flake8** – static analysis of the Python sources.
4. **Run unit tests with nose** – executes the unit tests under `tests/`.
5. **Cleanup task** – Tekton task that removes build leftovers before a run.
6. **Build and deploy** – buildah + openshift-client deploy step.

## Repository layout

```
cicd-final-project/
├── README.md
├── .github/
│   └── workflows/
│       └── workflow.yml      # GitHub Actions: flake8 lint + nose tests
├── .tekton/
│   ├── tasks.yml             # Tekton tasks: cleanup + nose
│   └── pipeline.yml          # OpenShift Pipeline oc-pipelines-oc-final
├── app/
│   ├── news.py               # sample application source
│   └── server.py             # service entry point, port 8000
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
