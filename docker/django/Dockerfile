FROM python:3.11.4
RUN apt-get update && apt-get -y install libpq-dev gcc python3-distutils
RUN apt-get install -y \
    wget gettext \
    build-essential \
    && apt-get clean \
    && apt-get autoremove -y

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
