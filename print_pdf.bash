#!/bin/bash
set -euo pipefail

podman run --rm -t \
    --userns=keep-id \
    -v `pwd`/public:/public:ro \
    -v `pwd`/archive/public:/dest:rw \
    docker.io/astefanutti/decktape \
    --screenshots-size 1920x1080 \
    /public/index.html \
    /dest/slides.pdf
