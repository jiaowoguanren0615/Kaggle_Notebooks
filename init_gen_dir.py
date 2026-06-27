from pathlib import Path
import json


# Root folder
ROOT_DIR = Path(".")


def create_empty_notebook(path: Path):
    """
    Create a minimal empty Jupyter Notebook file.
    """
    notebook_content = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.x"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    path.write_text(
        json.dumps(notebook_content, indent=2),
        encoding="utf-8"
    )


def create_file(path: Path):
    """
    Create different types of files based on suffix.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        print(f"Skipped existing file: {path}")
        return

    if path.suffix == ".ipynb":
        create_empty_notebook(path)

    elif path.suffix == ".md":
        title = path.stem.replace("_", " ").replace("-", " ").title()
        path.write_text(f"# {title}\n\n", encoding="utf-8")

    elif path.suffix == ".csv":
        path.write_text("", encoding="utf-8")

    elif path.suffix == ".py":
        path.write_text(
            f'"""\n{path.name}\nUtility functions for Kaggle projects.\n"""\n\n',
            encoding="utf-8"
        )

    else:
        path.write_text("", encoding="utf-8")

    print(f"Created file: {path}")


def main():
    files = [
        # competitions/titanic
        "competitions/titanic/notebook.ipynb",
        "competitions/titanic/submission.csv",
        "competitions/titanic/README.md",

        # competitions other folders
        "competitions/house-prices/.gitkeep",
        "competitions/playground-series/.gitkeep",

        # eda
        "eda/titanic_eda.ipynb",
        "eda/house_prices_eda.ipynb",
        "eda/general_visualization.ipynb",

        # feature engineering
        "feature-engineering/missing_values.ipynb",
        "feature-engineering/encoding_methods.ipynb",
        "feature-engineering/scaling_normalization.ipynb",
        "feature-engineering/feature_selection.ipynb",

        # experiments
        "experiments/xgboost_test.ipynb",
        "experiments/lgb_baseline.ipynb",
        "experiments/ensemble_try.ipynb",

        # templates
        "templates/kaggle_tabular_template.ipynb",
        "templates/cv_validation_template.ipynb",
        "templates/submission_template.ipynb",

        # notes
        "notes/kaggle_tips.md",
        "notes/feature_engineering.md",
        "notes/model_selection.md",
        "notes/mistakes_log.md",

        # utils
        "utils/data_utils.py",
        "utils/model_utils.py",
        "utils/visualization_utils.py",
    ]

    folders = [
        "competitions/titanic/data",
        "competitions/house-prices",
        "competitions/playground-series",
        "eda",
        "feature-engineering",
        "experiments",
        "templates",
        "notes",
        "utils",
    ]

    # Create folders
    for folder in folders:
        folder_path = ROOT_DIR / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")

    # Create files
    for file in files:
        create_file(ROOT_DIR / file)

    print("\nKaggle folder structure created successfully.")


if __name__ == "__main__":
    main()
