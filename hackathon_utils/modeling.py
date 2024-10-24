import pandas as pd
import statsmodels.formula.api as smf


def fit_mixed_effects_model(df_long):
    """Fit a linear mixed-effects model to estimate reviewer bias."""
    model = smf.mixedlm("Rating ~ 1", df_long, groups=df_long["first"])
    result = model.fit()
    return result


def calculate_reviewer_effects(result):
    """Extract reviewer effects from the model result."""
    reviewer_effects = result.random_effects
    reviewer_effects_df = pd.DataFrame.from_dict(
        reviewer_effects, orient="index"
    ).reset_index()
    reviewer_effects_df.columns = ["first", "reviewer_effect"]
    return reviewer_effects_df


def adjust_ratings(df_long, reviewer_effects_df):
    """Adjust ratings by subtracting reviewer effects."""
    df_normalized = df_long.merge(reviewer_effects_df, on="first", how="left")
    df_normalized["Normalized_Rating"] = (
        df_normalized["Rating"] - df_normalized["reviewer_effect"]
    )
    return df_normalized


def compute_normalized_scores(df_normalized):
    """Compute mean normalized scores and rank projects."""
    # Pivot back to wide format
    df_normalized_wide = df_normalized.pivot_table(
        index=["Project name", "first"], columns="Criterion", values="Normalized_Rating"
    ).reset_index()
    # Calculate mean normalized score
    df_normalized_wide["Normalized_mean"] = df_normalized_wide[
        ["Criteria 1", "Criteria 2", "Criteria 3"]
    ].mean(axis=1)
    # Compute overall mean per project
    df_normalized_wide["normal_mean_overall"] = df_normalized_wide.groupby(
        "Project name"
    )["Normalized_mean"].transform("mean")
    # Order 'Project name' by 'normal_mean_overall'
    df_normalized_wide["Project name"] = pd.Categorical(
        df_normalized_wide["Project name"],
        categories=df_normalized_wide.sort_values(
            "normal_mean_overall", ascending=False
        )["Project name"].unique(),
        ordered=True,
    )
    return df_normalized_wide
