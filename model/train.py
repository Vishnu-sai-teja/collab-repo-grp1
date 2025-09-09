import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import NearestNeighbors


def train(df, payload):
    X = df.drop(columns=["id", "name"])
    ids = df[["id", "name"]]

    # Define categorical and numerical features
    categorical = ["skillset", "organisation", "exp_type", "sex"]
    numerical = ["age", "experience"]

    # Preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
        ]
    )

    # Build pipeline
    knn_model = Pipeline([
        ("preprocessor", preprocessor),
        ("nn", NearestNeighbors(n_neighbors=3, metric="manhattan"))
    ])

    knn_model.fit(X)

    query_df = pd.DataFrame([payload])
    distances, indices = knn_model.named_steps["nn"].kneighbors(
        knn_model.named_steps["preprocessor"].transform(query_df)
    )

    recommendations = df.iloc[indices[0]] 

    mentors_list = recommendations.to_dict(orient="records")
    return mentors_list
    