ARG PYTHON_VER=3.11.9
FROM python:$PYTHON_VER-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install wget ca-certificates gnupg -y
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN echo "deb http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN apt-get update -y
RUN apt-get install -y libcairo2-dev gcc libpq-dev postgresql-client-common postgresql-common postgresql-16 postgresql-client-16 postgresql-contrib-16 vim
RUN rm -rf /var/lib/apt/lists/* &&  apt clean

WORKDIR /app/

ARG CTR_USER="python"
ARG CTR_UID="10000"
ARG CTR_GID="10000"

RUN <<EOF
groupadd --gid $CTR_GID $CTR_USER
useradd --uid $CTR_UID --gid $CTR_GID -m $CTR_USER
chown $CTR_UID:$CTR_GID -R /app/
EOF

USER $CTR_USER

RUN python3 -m venv .venv

ENV PATH="/app/.venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt

# Install django-storages
RUN pip install 'django-storages[s3]' pytest
# Install webserver

RUN pip install 'granian'

COPY --chown=$CTR_UID:$CTR_GID . .

RUN chmod +x /app/production/prepare_server.sh /app/production/wait_pg_ready.sh

# Move settings file
RUN cp /app/production/production_settings.py /app/horilla/production_settings.py

ENTRYPOINT ["/bin/bash", "-c"]
