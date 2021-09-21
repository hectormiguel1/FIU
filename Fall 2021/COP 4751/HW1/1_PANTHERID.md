# Question 1 
Write the SQL queries for the following items, considering the SQL Query Optimization Techniques studied in class.

A. Retrive the name, original language, and year of the movies.

 ```sql
    SELECT mov_name, mov_lang, mov_year 
    FROM movie
```

B. Retrive title and language of all USA release country movies which were released between Jan/01/2019 and December/31/2020

```sql
    SELECT mov_title, mov_lang 
    FROM movie
    WHERE mov_rel_country = "USA" 
    AND mov_year >= 2019 
    AND mov_year <= 2020
```

C. Retrive a list of first names of all the actors who were cast in the movie "The Godfather" and the roles they played in the production.

```sql
    SELECT act_fname, act_lname, role 
    FROM actor, movie, movie_cast, 
    WHERE movie_cast.act_id = actor.act_id 
    AND movie_cast.mov_id = movie.mod_id 
    AND movie.mov_title = "The Godfather"
```











=============== Originality Declaration =====================

Name: Hector Ramirez

Panther-ID: _______

Course: COP-4751

Assignment#: 1

Due: 

I hereby certify that this work is my own and none of it is the work of any other person.

Signature: Hector Ramirez

=========================================================