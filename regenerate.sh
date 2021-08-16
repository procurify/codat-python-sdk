#!/usr/bin/env bash

set -e

spec_location=https://api.codat.io/swagger/v1/swagger.json

if ! type openapi-generator > /dev/null 2>&1; then
  echo 'You need to install the sdk generator, run `brew install openapi-generator`'
  exit 1
fi

cp README.md custom_README.md

openapi-generator generate \
  --skip-validate-spec \
  --input-spec $spec_location \
  --generator-name python \
  --git-user-id procurify \
  --git-repo-id codat-python-sdk \
  --package-name codat_python_sdk

mv README.md generated_info.md

mv custom_README.md README.md
