FROM registry.access.redhat.com/ubi9/python-311:1-62.1716478620

ARG GIT_TAG=stable

ARG XTERM_PORT=8501

ENV XTERM_PORT=${XTERM_PORT}

RUN git clone --depth 1 --branch ${GIT_TAG} https://github.com/instructlab/instructlab.git instructlab

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY terminal.py /app/terminal.py

COPY termpage.html /app/termpage.html

ENTRYPOINT ["python3", "/app/terminal.py"]
