from fastapi import FastAPI
from schema import MentorRecommendationRequest, MentorsResponse
from schema import Mentor
import sqlite3
import pandas as pd
from model.train import train

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

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

@app.post("/recommend_mentors", response_model=MentorsResponse)
async def recommend_mentors(filters: MentorRecommendationRequest):
    conn = sqlite3.connect('mentoring_platform.db')
    cur = conn.cursor()

    query = """
        SELECT id, name, age, experience, skillset, organisation, exp_type, sex
        FROM Person
        WHERE role = 'mentor'
    """

    df = pd.read_sql_query(query, conn)
    print(filters)
    mentors_list = train(df, filters.dict())

    mentors = [
        Mentor(
            id=row["id"],
            name=row["name"],
            age=row["age"],
            experience=row["experience"],
            skillset=row["skillset"],
            organisation=row["organisation"],
            exp_type=row["exp_type"],
            sex=row["sex"]
        )
        for row in mentors_list
    ]
    
    conn.close()
    return {"mentors": mentors}
