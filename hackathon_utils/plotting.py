import matplotlib.pyplot as plt
import seaborn as sns


def plot_project_scores(df_normalized_wide):
    """Plot projects ranked by reviewer scores."""
    plt.figure(figsize=(12, 8))
    sns.boxplot(
        x="Normalized_mean", y="Project name", data=df_normalized_wide, orient="h"
    )
    plt.title("Projects Ranked by Reviewer Scores (Conditioned on Reviewer Bias)")
    plt.xlabel("Normalized Mean Score")
    plt.ylabel("Project Name")
    plt.tight_layout()
    plt.show()
