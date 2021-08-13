#!/usr/bin/env bash

set -e

spec_location=https://api.codat.io/swagger/v1/swagger.json

if ! type swagger-codegen > /dev/null 2>&1; then
  echo 'You need to install the sdk generator, run `brew install swagger-codegen`'
  exit 1
fi

cp README.md custom_README.md

swagger-codegen generate \
  --input-spec $spec_location \
  --lang python \
  --git-user-id procurify \
  --git-repo-id codat-python-sdk \
  -DpackageName=codat_python_sdk

mv README.md generated_info.md

mv custom_README.md README.md
