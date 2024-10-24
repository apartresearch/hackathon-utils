import pandas as pd


def load_data(filepath):
    """Load CSV data into a DataFrame."""
    df = pd.read_csv(filepath)
    # Convert 'Created On' to datetime if present
    if "Created On" in df.columns:
        df["Created On"] = pd.to_datetime(
            df["Created On"], format="%a %b %d %Y %H:%M:%S", utc=True
        )
    return df


def preprocess_data(df):
    """Preprocess the DataFrame by filtering and calculating totals."""
    # Filter out rows where 'Criteria 1' is NaN
    df = df[df["Criteria 1"].notna()]
    # Calculate total score
    df["total"] = df[["Criteria 1", "Criteria 2", "Criteria 3"]].mean(axis=1)
    # Create a short project name with count
    df["Project name"] = df.groupby("Project name").transform(
        lambda x: f"[{len(x)}] {x.name[:20]}..."
    )
    # Calculate mean total score per project
    df["max_total"] = df.groupby("Project name")["total"].transform("mean")
    # Set 'Project name' as a categorical variable ordered by 'max_total'
    df["Project name"] = pd.Categorical(
        df["Project name"],
        categories=df.sort_values("max_total", ascending=False)[
            "Project name"
        ].unique(),
        ordered=True,
    )
    return df


def reshape_data(df):
    """Reshape the DataFrame to long format for modeling."""
    # Extract first name from 'Name'
    df["first"] = df["Name"].str.extract(r"([a-zA-Z]+)")
    # Reshape to long format
    df_long = df.melt(
        id_vars=["Project name", "first"],
        value_vars=["Criteria 1", "Criteria 2", "Criteria 3"],
        var_name="Criterion",
        value_name="Rating",
    )
    return df_long
