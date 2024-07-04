FROM registry.access.redhat.com/ubi9/python-311:1-62.1716478620

ARG GIT_TAG=stable

RUN git clone --depth 1 --branch ${GIT_TAG} https://github.com/instructlab/instructlab.git instructlab

WORKDIR /instructlab

COPY requirements.txt /instructlab/requirements.txt

RUN pip install instructlab --extra-index-url=https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir --upgrade -r /instructlab/requirements.txt

RUN ilab init --non-interactive && ilab model download

ENTRYPOINT ["ilab", "model", "chat"]
