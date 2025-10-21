# SQL - More queries

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be executed on Ubuntu 22.04 LTS using MySQL 8.0 (version 8.0.25)
* All files should start with a description of the task and end with a new line
* All SQL queries should have a comment
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of all files will be tested using wc

### General information
__Number of tasks:__ 17<br/>
__Completed:__ 11<br/>
__Passed:__ 7<br/>

#### 0. My privileges!
Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`.<br/>
See file [`0-privileges.sql`](./0-privileges.sql)
#### 1. Root user
Creates the new user `user_0d_1` and gives them all privileges.<br/>
See file [`1-create_user.sql`](./1-create_user.sql)
#### 2. Read user
Creates user `user_0d_2` and grants them `SELECT` privileges in the `hbtn_0d_2` database.<br/>
Does not fail if database or user already exists.<br/>
See file [`2-create_read_user.sql`](./2-create_read_user.sql)
#### 3. Always a name
Creates the table `force_name` on our mysql server.<br/>
`force_name` has an INT `id` and a VARCHAR(256) `name` that can't be null.<br/>
See file [`3-force_name.sql`](./3-force_name.sql)
#### 4. ID can't be null
Creates the table `id_not_null` where, you guessed it, `id` can't be null.<br/>
See file [`4-never_empty.sql`](./4-never_empty.sql)
#### 5. Unique ID
Creates the table `unique_id` where `id` defaults to 1, but is unique.<br/>
See file [`5-unique_id.sql`](./5-unique_id.sql)
#### 6. States table
Creates the database `hbtn_0d_usa` and the table `states`.<br/>
`states` has a primary key `id` and a `name` that cannot be null.<br/>
See file [`6-states.sql`](./6-states.sql)
#### 7. Cities table
Now creating the `cities` table, similar to `states`.<br/>
Has a `state_id` column that holds a foreign key referencing the id in the `states` table.<br/>
See file [`7-cities.sql`](./7-cities.sql)
#### 8. Cities of California
Sorting in ascending order by `cities_id`, lists all the cities of California that can be found in the database `hbtn_0d_usa`.<br/>
Cannot use `JOIN`.<br/>
See file [`8-cities_of_california_subquery.sql`](./8-cities_of_california_subquery.sql)
#### 9. Cities by States
Lists all cities contained in the database, sorted in ascending order by `cities.id`.<br/>
Columns must follow the format `cities.id` -` cities.name` - `states.name`.<br/>
See file [`9-cities_by_state_join.sql`](./9-cities_by_state_join.sql)
#### 10. Genre ID by show
Lists the name of a tv show as many times as it has associates genres, _and_ the id of said genres.<br/>
See file [`10-genre_id_by_show.sql`](./10-genre_id_by_show.sql)
#### 11. Genre ID for all shows
See file [`5-unique_id.sql`](./5-unique_id.sql)
#### 12. No genre
See file [`5-unique_id.sql`](./5-unique_id.sql)
#### 13. Number of shows by genre
See file [`5-unique_id.sql`](./5-unique_id.sql)
#### 14. My genres
See file [`5-unique_id.sql`](./5-unique_id.sql)
#### 15. Only Comedy
See file [`5-unique_id.sql`](./5-unique_id.sql)
#### 16. List shows and genres
See file [`5-unique_id.sql`](./5-unique_id.sql)
