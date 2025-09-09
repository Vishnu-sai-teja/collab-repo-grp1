from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/mentors")
async def get_mentors():
    # Connect to DB
    conn = sqlite3.connect('mentoring_platform.db')
    cur = conn.cursor()

    # Query only mentors
    cur.execute("""
        SELECT id, name, age, experience, skillset, organisation, exp_type, sex
        FROM Person
        WHERE role = 'mentor'
    """)

    # Fetch and map results
    mentors = [
        {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "experience": row[3],
            "skillset": row[4],
            "organisation": row[5],
            "exp_type": row[6],
            "sex": row[7]
        }
        for row in cur.fetchall()
    ]

    # Close connection
    conn.close()

    # Return JSON response
    return {"mentors": mentors}



