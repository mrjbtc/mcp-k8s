FROM python:3.11-slim

ARG USER="acrux"

RUN apt-get update -y
RUN apt-get install -y wget
RUN wget https://dl.k8s.io/v1.31.2/bin/linux/amd64/kubectl
RUN chmod +x kubectl
RUN mv kubectl /usr/local/bin/

RUN useradd -m ${USER}
USER ${USER}
RUN mkdir /home/${USER}/mcp

ENV PATH="/home/${USER}/.local/bin:$PATH"
ENV PYTHONPATH=/home/${USER}/mcp

COPY --chown=${USER}:${USER} requirements.txt /home/${USER}/mcp/requirements.txt

RUN python -m ensurepip --default-pip && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /home/${USER}/mcp/requirements.txt

COPY --chown=${USER}:${USER} ./mcp/ /home/${USER}/mcp/
COPY --chown=${USER}:${USER} kube-config /home/${USER}/.kube/config

WORKDIR /home/${USER}

CMD ["/bin/bash"]
