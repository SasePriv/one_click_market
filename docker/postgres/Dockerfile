FROM postgres:16.1
COPY postgres.conf /etc/postgres.conf

RUN mkdir -p /db_dumps/data
COPY dumper.sh /db_dumps
RUN chmod +x /db_dumps/dumper.sh

RUN echo -e '#!bin/sh \ncreatedb -O postgres ${PROJECT_NAME}\n echo "Created DB ${PROJECT_NAME}"' > /docker-entrypoint-initdb.d/99_create_db.sh \
    && chmod 755 /docker-entrypoint-initdb.d/99_create_db.sh
