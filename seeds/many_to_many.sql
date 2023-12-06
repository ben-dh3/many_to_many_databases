DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name text
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    title text
);

CREATE TABLE students_tags (
    student_id int,
    tag_id int,
    constraint fk_student foreign key(student_id) references students(id) on delete cascade,
    constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
    PRIMARY KEY (student_id, tag_id)
);