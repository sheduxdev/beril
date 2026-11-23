# Beril runtime image.
#
#   docker build -t beril .
#   docker run --rm -v "$PWD:/work" beril scan --target /work --profile engineer
#
# The image makes no outbound request unless the command does. Build with
# --build-arg WITH_BROWSER=1 to include the Camoufox browser for --render.
ARG PYTHON_IMAGE=python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b

FROM ${PYTHON_IMAGE} AS build

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /build
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH
COPY pyproject.toml README.md LICENSE CHANGELOG.md ./
COPY scripts ./scripts
COPY data ./data
COPY references ./references
COPY docs ./docs
COPY agents ./agents
COPY benchmarks ./benchmarks
COPY labs/detection/incidents ./labs/detection/incidents
RUN pip install --no-cache-dir .

FROM ${PYTHON_IMAGE}

ARG WITH_BROWSER=0
ENV PATH=/opt/venv/bin:$PATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates git \
    && rm -rf /var/lib/apt/lists/*
COPY --from=build /opt/venv /opt/venv
RUN useradd --uid 10001 --create-home --shell /usr/sbin/nologin beril \
    && chown -R 10001:10001 /opt/venv/share/beril \
    && if [ "$WITH_BROWSER" = "1" ]; then \
         pip install --no-cache-dir camoufox \
         && su beril -c "python -m camoufox fetch"; \
       fi
USER 10001
WORKDIR /work
LABEL org.opencontainers.image.title="Beril" \
      org.opencontainers.image.source="https://github.com/sheduxdev/beril" \
      org.opencontainers.image.licenses="MIT"
ENTRYPOINT ["beril"]
CMD ["help"]
