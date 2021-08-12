#!/usr/bin/env bash

set -e

if ! type swagger-codegen > /dev/null 2>&1; then
  echo 'You need to install the sdk generator, run `brew install swagger-codegen`'
  exit 1
fi

swagger-codegen generate \
  --input-spec https://api-uat.codat.io/swagger/v1/swagger.json \
  --lang python \
  --git-user-id procurify \
  --git-repo-id codat-python-sdk
