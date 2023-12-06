# 04 designing many to many
# exercise

As a coach
So I can get to know all students
I want to keep a list of students' names.

As a coach
So I can get to know all students
I want to assign tags to students (for example, "happy", "excited", etc).

As a coach
So I can get to know all students
I want to be able to assign the same tag to many different students.

As a coach
So I can get to know all students
I want to be able to assign many different tags to a student.

students, students names, students tags, 

| Record                | Properties          |
| --------------------- | ------------------  |
| students              | name
| tags                  | title

students
id: SERIAL
name: text

tags
id: SERIAL
title: text

students_tags
student_id int
tag_id int

# challenge

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of movies with their title and release date.

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of my cinemas with their city name (e.g 'London' or 'Manchester').

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which cinemas are showing a specific movie.

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which movies are being shown a specific cinema.

movies, movie title, movie release date, cinema, cinema location, 

| Record                | Properties          |
| --------------------- | ------------------  |
| movies                | title, release_date
| cinemas               | city


movies
id: SERIAL
title: text
release_date: DATE

cinemas
id: SERIAL
city: text

movies_cinemas
movie_id
cinema_id