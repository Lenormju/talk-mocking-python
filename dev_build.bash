#!/bin/bash
set -euo pipefail

mkdir -p public
uv run mkslides \
    serve \
    --config-file 'mkslides_config.yml' \
    --strict \
    --open \
    'slides/slides.md'

#xdg-open "file://$(pwd)/public/index.html"
