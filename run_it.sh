#!/usr/bin/bash
docker build --tag tic-tac-toe . && \
docker run --rm -it tic-tac-toe