FROM registry.access.redhat.com/ubi9/python-311:1-62.1716478620
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY src/sample-app.py .
ENV GRADIO_SERVER_NAME="0.0.0.0"
EXPOSE 8501
USER root
ENTRYPOINT [ "python", "sample-app.py" ]