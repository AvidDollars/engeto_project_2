#!/usr/bin/bash

### TO BE USED AS PRE-COMMIT HOOK ###
#
# USAGE:
#   in .git/hooks/pre-commit.sample:
#       1) remove old code (only shebang to be left)
#       2) add a line: $PATH_TO_PROJECT/pre-commit-hook.sh
#       3) rename the hook: "pre-commit.sample" -> "pre-commit"

isort --profile black . && \
black . --verbose && \
ruff . && \
mypy --strict . && \
pytest --cov .
