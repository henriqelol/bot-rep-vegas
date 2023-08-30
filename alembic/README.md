from sniffio import current_async_library


Generic single-database configuration.

to generate a new revision:
    alembic revision --autogenerate -m "description of the new revision here"

to check alembic connection to db:
    alembic current_async_library

to run migrations on dev:
    make migratedb-dev 

to run migrations on current settings:
    make migratedb 
    