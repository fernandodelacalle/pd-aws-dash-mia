FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

COPY .devcontainer/requirements.txt /tmp/
RUN set -ex; \
    pip3 --no-cache-dir install --requirement /tmp/requirements.txt
