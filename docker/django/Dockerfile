FROM python:3.11.4
RUN apt-get update && apt-get -y install libpq-dev gcc python3-distutils
RUN apt-get install -y \
    wget gettext \
    build-essential \
    && apt-get clean \
    && apt-get autoremove -y

# Install dockerize to avoid startup problems (waiting for DB to start)
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
         -O - | tar -C /usr/local/bin -xzv

ARG PROJECT_NAME
ARG PROJECT_EXTERNAL_PATH=backend/src/

RUN mkdir ${PROJECT_NAME}
WORKDIR ${PROJECT_NAME}

RUN mkdir -p /static
RUN mkdir -p /media

# ----------------------------------------------------------------------------------------------------------------------
# Install python project dependencies
# ----------------------------------------------------------------------------------------------------------------------
# django requirements (python)
COPY ${PROJECT_EXTERNAL_PATH}/requirements.txt /${PROJECT_NAME}/
RUN pip install --upgrade pip && pip install -r requirements.txt

# ----------------------------------------------------------------------------------------------------------------------
# Load source code & executors
# ----------------------------------------------------------------------------------------------------------------------
COPY ${PROJECT_EXTERNAL_PATH}/ /${PROJECT_NAME}/

COPY docker/django/run_django.sh /${PROJECT_NAME}/

COPY docker/django/ipython_config.py /root/.ipython/profile_default/

