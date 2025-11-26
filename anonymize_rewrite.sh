#!/bin/sh
# Reescribe el historial para anonimizar autores y committers distintos a Eddy18-hub
# Reemplaza nombre/email por: Removed Contributor <removed@example.com>

RENAME_NAME="Removed Contributor"
RENAME_EMAIL="removed@example.com"
KEEP_NAME="Eddy18-hub"
KEEP_EMAIL="espinosaeduardo1805@gmail.com"

git filter-branch --force --env-filter '
    if [ "${GIT_AUTHOR_NAME}" != "'"${KEEP_NAME}"'" ] || [ "${GIT_AUTHOR_EMAIL}" != "'"${KEEP_EMAIL}"'" ]; then
        export GIT_AUTHOR_NAME="'"${RENAME_NAME}"'"
        export GIT_AUTHOR_EMAIL="'"${RENAME_EMAIL}"'"
    fi
    if [ "${GIT_COMMITTER_NAME}" != "'"${KEEP_NAME}"'" ] || [ "${GIT_COMMITTER_EMAIL}" != "'"${KEEP_EMAIL}"'" ]; then
        export GIT_COMMITTER_NAME="'"${RENAME_NAME}"'"
        export GIT_COMMITTER_EMAIL="'"${RENAME_EMAIL}"'"
    fi
' -- --all

# Limpieza de refs temporales creados por filter-branch
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

exit 0
