# SQL - Introduction
As our programming journey goes on, we now find ourselves facing a sphinx: the mythical Structured Query Language, _SQL_.<br/>
What it requires from us is understanding, adaptability, and decent Google searching skills.<br/>
If you're curious as to the questions this sphinx asked us, go right ahead to the [tasks overview](#overview) section.<br/>
If you'd like to know how we approached it, just keep reading, for the [requirements](#Requirements) section is near.<br/>

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be executed on Ubuntu 22.04 LTS using MySQL 8.0 (version 8.0.25)
* All files should start with a description of the task and end with a new line
* All SQL queries should have a comment
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of all files will be tested using wc

## Tasks
### General information
__Number of tasks:__ 17<br/>
__Completed:__ 17<br/>
__Passed:__ 17<br/>
### Overview
#### 0. List databases
Lists all databases of our MySQL server.<br/>
See file [`0-list_databases.sql`](./0-list_databases.sql)
#### 1. Create a database
Without using the `SELECT` or `SHOW` statements and ensuring the script does not fail should the database exist, creates the database `hbtn_0c_0` in our MySQL server.<br/>
See file [`1-create_database_if_missing.sql`](./1-create_database_if_missing.sql)
#### 2. Delete a database
Without using the `SELECT` or `SHOW` statements and ensuring the script does not fail should the database __not__ exist, deletes the database `hbtn_0c_0` in our MySQL server.<br/>
See file [`2-remove_database.sql`](./2-remove_database.sql)
#### 3. List tables
Lists all the tables of a database in the MySQL server.<br/>
See file [`3-list_tables.sql`](./3-list_tables.sql)
#### 4. First table
Creates a table called first_table in the current database in the MySQL server.<br/>
See file [`4-first_table.sql`](./4-first_table.sql)
#### 5. Full description
Without using the `DESCRIBE` or `EXPLAIN` statements, prints full description of the table created in task 4.<br/>
See file [`5-full_table.sql`](./5-full_table.sql)
#### 6. List all in table
Lists all rows of the table created in task 4.<br/>
See file [`6-list_values.sql`](./6-list_values.sql)
#### 7. First add
Inserts a new row in the table `first_table`, using values `id = 89` and `name = Best School`.<br/>
See file [`7-insert_value.sql`](./7-insert_value.sql)
#### 8. Count 89
Displays the number of records with `id = 89` in `first_table`.<br/>
See file [`8-count_89.sql`](./8-count_89.sql)
#### 9. Full creation
Creates `second_table` in the database and adds four rows with `id`, `name`, and `score` values.<br/>
See file [`9-full_creation.sql`](./9-full_creation.sql)
#### 10. List by best
Lists all records from `second_table`, score first, then name, in descending score order.<br/>
See file [`10-top_score.sql`](./10-top_score.sql)
#### 11. Select the best
Lists all records from `second_table` where `score` >= 10, score then name, top score first.<br/>
See file [`11-best_score.sql`](./11-best_score.sql)
#### 12. Cheating is bad
Updates Bob's score to 10 in `second_table`, _without_ using his id value.<br/>
See file [`12-no_cheating.sql`](./12-no_cheating.sql)
#### 13. Score too low
Removes all records with a score <= 5 in `second_table`.<br/>
See file [`13-change_class.sql`](./13-change_class.sql)
#### 14. Average
Computes the score average of all records in `second_table`.<br/>
See file [`14-average.sql`](./14-average.sql)
#### 15. Number by score
Lists the number of records with the same score in `second_table`.<br/>
The displays should be the `score` column, then a new column named `number` with the number of records for that score.<br/>
See file [`15-groups.sql`](./15-groups.sql)
#### 16. Say my name
Displays score and name by descending score, only for rows where `name` column contains a value.<br/>
See file [`16-no_link.sql`](./16-no_link.sql)
