# hackathon-utils

Utilities for processing and analyzing hackathon project reviews, including functions for data loading, preprocessing, modeling, and plotting. This package helps in calculating reviewer bias, standardizing criteria reviews, computing averages, ranking projects, and generating visualizations.

## Table of Contents

- [hackathon-utils](#hackathon-utils)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Clone the Repository](#clone-the-repository)
    - [Install the Package](#install-the-package)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [Example](#example)
  - [Extensibility](#extensibility)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Data Loading**: Read CSV files into pandas DataFrames.
- **Data Preprocessing**: Filter and transform data for analysis.
- **Reviewer Bias Calculation**: Use linear mixed-effects models to estimate and adjust for reviewer bias.
- **Standardization**: Normalize criteria reviews by accounting for individual reviewer effects.
- **Scoring and Ranking**: Calculate average scores and rank projects accordingly.
- **Visualization**: Generate plots to visualize project rankings and score distributions.
- **Extensible Design**: Modular structure allows for easy addition of new features and functions.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/hackathon-utils.git
cd hackathon-utils
```

### Install the Package

You can install the package in editable mode using pip:

```
pip install -e .
```

Alternatively, you can install it directly from the repository:

```
pip install git+https://github.com/yourusername/hackathon-utils.git
```

## Dependencies

The package relies on the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- statsmodels

Install the dependencies using:

```
pip install -r requirements.txt
```

(A requirements.txt file should list all the dependencies.)

## Usage

Import the required functions from the package:

```
from hackathon_utils import (
    load_data,
    preprocess_data,
    reshape_data,
    fit_mixed_effects_model,
    calculate_reviewer_effects,
    adjust_ratings,
    compute_normalized_scores,
    plot_project_scores
)
```

## Example

Here's a step-by-step example of how to use the package:

```
# Step 1: Load Data
df = load_data('data/project_reviews_2024-09-04.csv')

# Step 2: Preprocess Data
df_processed = preprocess_data(df)

# Step 3: Reshape Data for Modeling
df_long = reshape_data(df_processed)

# Step 4: Fit Mixed-Effects Model
model_result = fit_mixed_effects_model(df_long)

# Step 5: Calculate Reviewer Effects
reviewer_effects_df = calculate_reviewer_effects(model_result)

# Step 6: Adjust Ratings Based on Reviewer Bias
df_normalized = adjust_ratings(df_long, reviewer_effects_df)

# Step 7: Compute Normalized Scores and Rankings
df_normalized_wide = compute_normalized_scores(df_normalized)

# Step 8: Plot the Results
plot_project_scores(df_normalized_wide)

# Step 9: Save Normalized Scores to CSV
df_normalized_wide.to_csv('data/demo_calculated_scores.csv', index=False)
```

## Extensibility

The package is designed to be modular and extensible:

Add New Data Processing Functions: - Place them in data_processing.py.

- Implement Additional Models or - Analyses: Add them to modeling.py.
  Create More Visualization Tools: Include them in plotting.py.
- Utility Functions: General helper functions can go into utils.py.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Repository: Click the "Fork" button at the top right of the repository page.
2. Clone Your Fork: `git clone https://github.com/yourusername/hackathon-utils.git`
3. Create a New Branch: `git checkout -b feature/your-feature-name`
4. Make Your Changes: Add your new features or bug fixes.
5. Commit and Push:

```
git add .
git commit -m "Add your commit message here"
git push origin feature/your-feature-name
```

6. Submit a Pull Request: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or suggestions, please contact:

- Esben Kran and Jaime Raldua
- sprints@apartresearch.com
