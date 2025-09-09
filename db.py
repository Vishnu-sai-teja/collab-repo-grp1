# mentors_mentees_single_table_with_ref_sqlite.py

import sqlite3

conn = sqlite3.connect('mentoring_platform.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT CHECK(role IN ('mentor', 'mentee')) NOT NULL,
    age INTEGER NOT NULL,
    experience INTEGER,  -- NULL for mentees
    skillset TEXT NOT NULL,  -- Comma-separated values
    organisation TEXT CHECK(organisation IN ('Startup', 'MNC', 'Big4')) NOT NULL,
    exp_type TEXT CHECK(exp_type IN ('service', 'prod')),  -- NULL for mentees
    sex TEXT CHECK(sex IN ('m', 'f')) NOT NULL
)
''')

cur.execute("""
INSERT INTO Person (name, role, age, experience, skillset, organisation, exp_type, sex) VALUES
('Ravi Kumar', 'mentor', 42, 18, 'Python', 'MNC', 'service', 'm'),
('Anita Sharma', 'mentor', 38, 14, 'Java', 'Startup', 'prod', 'f'),
('Vikram Singh', 'mentor', 45, 20, 'Python', 'Big4', 'service', 'm'),
('Pooja Reddy', 'mentor', 34, 12, 'Java', 'MNC', 'service', 'f'),
('Arjun Mehta', 'mentor', 40, 16, 'Python', 'Startup', 'prod', 'm'),
('Neha Verma', 'mentor', 36, 13, 'Java', 'MNC', 'service', 'f'),
('Rahul Nair', 'mentor', 48, 22, 'Python', 'Big4', 'service', 'm'),
('Meena Joshi', 'mentor', 41, 17, 'Java', 'MNC', 'prod', 'f'),
('Sanjay Gupta', 'mentor', 39, 15, 'Python', 'Startup', 'prod', 'm'),
('Kavita Rao', 'mentor', 37, 14, 'Java', 'MNC', 'service', 'f'),
('Amit Patel', 'mentor', 44, 19, 'Python', 'Big4', 'service', 'm'),
('Priya Menon', 'mentor', 33, 11, 'Java', 'MNC', 'prod', 'f'),
('Suresh Das', 'mentor', 46, 21, 'Python', 'Startup', 'service', 'm'),
('Divya Kapoor', 'mentor', 35, 12, 'Java', 'MNC', 'prod', 'f'),
('Harish Iyer', 'mentor', 43, 18, 'Python', 'Big4', 'service', 'm'),
('Shalini Mishra', 'mentor', 39, 15, 'Java', 'Startup', 'prod', 'f'),
('Manoj Rathi', 'mentor', 50, 25, 'Python', 'MNC', 'service', 'm'),
('Deepa Kulkarni', 'mentor', 37, 13, 'Java', 'Big4', 'prod', 'f'),
('Rohit Sen', 'mentor', 41, 17, 'Python', 'MNC', 'prod', 'm'),
('Anjali Deshmukh', 'mentor', 36, 12, 'Java', 'Startup', 'service', 'f')
""")

# -- 20 Mentees
cur.execute("""
INSERT INTO Person (name, role, age, experience, skillset, organisation, exp_type, sex) VALUES
('Aditya Jain', 'mentee', 24, NULL, 'Python', 'MNC', NULL, 'm'),
('Sneha Pillai', 'mentee', 22, NULL, 'Java', 'Startup', NULL, 'f'),
('Karthik R', 'mentee', 25, NULL, 'Python', 'Big4', NULL, 'm'),
('Ishita Agarwal', 'mentee', 23, NULL, 'Java', 'MNC', NULL, 'f'),
('Rohan Das', 'mentee', 21, NULL, 'Python', 'Startup', NULL, 'm'),
('Nidhi Sharma', 'mentee', 24, NULL, 'Java', 'MNC', NULL, 'f'),
('Arvind Menon', 'mentee', 22, NULL, 'Python', 'Big4', NULL, 'm'),
('Pallavi Rao', 'mentee', 23, NULL, 'Java', 'MNC', NULL, 'f'),
('Varun Kapoor', 'mentee', 25, NULL, 'Python', 'Startup', NULL, 'm'),
('Shreya Nair', 'mentee', 21, NULL, 'Java', 'MNC', NULL, 'f'),
('Siddharth Gupta', 'mentee', 22, NULL, 'Python', 'Big4', NULL, 'm'),
('Anusha Reddy', 'mentee', 23, NULL, 'Java', 'Startup', NULL, 'f'),
('Abhinav Singh', 'mentee', 24, NULL, 'Python', 'MNC', NULL, 'm'),
('Megha Jain', 'mentee', 21, NULL, 'Java', 'Big4', NULL, 'f'),
('Pranav Iyer', 'mentee', 25, NULL, 'Python', 'MNC', NULL, 'm'),
('Komal Sharma', 'mentee', 23, NULL, 'Java', 'Startup', NULL, 'f'),
('Naveen Kumar', 'mentee', 22, NULL, 'Python', 'MNC', NULL, 'm'),
('Tanvi Mehta', 'mentee', 21, NULL, 'Java', 'Big4', NULL, 'f'),
('Arjun Malhotra', 'mentee', 24, NULL, 'Python', 'MNC', NULL, 'm'),
('Ritika Sen', 'mentee', 23, NULL, 'Java', 'Startup', NULL, 'f')
""")


conn.commit()
conn.close()
