# PostgreSQL psql Navigation Commands:
This file documents essential PostgreSQL and psql navigation commands. 
It focuses on accessing PostgreSQL, navigating databases, inspecting metadata, and managing sessions. 
No SQL querying is performed here.

## 1. Accessing PostgreSQL:
- Command: sudo -i -u postgres
- Explanation: Switches to the PostgreSQL system user.

- Command: psql
- Explanation: Opens the PostgreSQL interactive terminal.

- Command: psql -d database_name
- Explanation: Opens psql and connects to the specified database.

- Command: \q
- Explanation: Exits the psql terminal.
---------------------------------------

## 2. Database Navigation:
- Command: \l
- Explanation: Lists all databases on the PostgreSQL server.

- Command: \c database_name
- Explanation: Connects the current session to a different database.

- Command: \conninfo
- Explanation: Displays connection information for the current session.
-----------------------------------------------------------------------

## 3. Schema and Table Inspection:
- Command: \dt
- Explanation: Lists tables in the current schema.

- Command: \dt * . * (ignore spaces between asterisk and 'dot').
- Explanation: Lists tables across all schemas.

- Command: \d table_name
- Explanation: Displays the structure of a table.

- Command: \dn
- Explanation: Lists all schemas in the current database.
---------------------------------------------------------

## 4. Help and Discovery:
- Command: \?
- Explanation: Displays all available psql meta-commands.

- Command: \h
- Explanation: Shows general help for SQL commands (reference only).

- Command: \h command_name
- Explanation: Shows help for a specific SQL command.
-----------------------------------------------------

## 5. Session Utilities:
- Command: \x
- Explanation: Toggles expanded output mode.

- Command: \s
- Explanation: Displays the command history for the current session.

- Command: ctrl + C
- Explanation: Cancels the current running command.
---------------------------------------------------

## 6. Emvironment Awareness:
- Command: whoami
- Explanation: Displays the current Linux user.
-----------------------------------------------

## 7. Backup and Restore:
- Command: pg_dump database-name > file.sql
- Explanation: Creates a backup of a PostgreSQL database.

- Command: psql database_name < file.sql
- Explanation: Restores a database from a backup file.
