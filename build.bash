#!/bin/bash
set -euo pipefail

mkdir -p public
uv run mkslides \
    build \
    --config-file 'mkslides_config.yml' \
    --site-dir 'public' \
    --strict \
    'slides/slides.md'

#xdg-open "file://$(pwd)/public/index.html"
