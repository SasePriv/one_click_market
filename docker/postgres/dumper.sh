#!/bin/bash
if [ $1 == "-d" ]
then
  echo "Dumping DB..."
  PGPASSWORD=$POSTGRES_PASSWORD && pg_dump -U postgres -Fc -Z 9 turing > /db_dumps/data/turing.dump
  echo "DB dumped!"
elif [ $1 == "-r" ]
then
 echo "Dropping and restoring DB..."
  dropdb -U postgres turing && /usr/bin/pg_restore -U postgres -C -d postgres -Fc --username=postgres /db_dumps/data/turing.dump
  echo "DB restored!"
else
  echo "Invalid parameter. Use -d to dump or -r to restore"
fi