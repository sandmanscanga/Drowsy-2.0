# Notes

This branch is going to focus on preparing the database.

The database is a MySQL docker container.

---

## Root Info

+ host -> db
+ user -> root
+ passwd -> topsecret

---

## Root Steps

1. Drop the database if the database exists.
2. Drop the user if the user exists.
3. Create the database.
4. Create the user.
5. Grant the user privileges.

---

## User Info

+ host -> db
+ user -> vuln_user
+ passwd -> insecure
+ db -> vuln_db

---

## User Steps

1. Create the users table schema.
2. Insert data into the users table.

---

Might be a good idea to start this function with a hook that will be used to wait for the service to finish being brought up.

---

## Functions

1. wait_for_service
2. wipe_vuln_db
3. wipe_vuln_user
4. create_vuln_db
5. create_vuln_user
6. grant_vuln_user
7. create_table_schema
8. insert_table_data
