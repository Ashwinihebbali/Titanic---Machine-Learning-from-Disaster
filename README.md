# Titanic Dataset Model

Machine learning project predicting passenger survival on the Titanic using a trained classification model.

## Project Overview

This project implements a machine learning model to predict whether passengers survived the Titanic disaster. The model is trained on historical passenger data and makes binary predictions (0 = did not survive, 1 = survived).

## Files

- **Titanic-Dataset.csv** - Complete training/test dataset with passenger information
- **Titanic dataset model.ipynb** - Jupyter notebook with model development, training, and evaluation
- **submission.csv** - Final predictions (418 rows) formatted for Kaggle submission

## Dataset

**Features include:**
- PassengerId: Unique passenger identifier
- Survived: Binary outcome (0/1)
- Pclass: Ticket class (1st, 2nd, 3rd)
- Name: Passenger name
- Sex: Gender
- Age: Age in years
- SibSp: Number of siblings/spouses aboard
- Parch: Number of parents/children aboard
- Ticket: Ticket number
- Fare: Ticket price
- Cabin: Cabin number
- Embarked: Port of embarkation

**Total rows:** 891 passengers (training data) + 418 (test predictions)

## Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
```

## Installation

```bash
git clone <repository-url>
cd Titanic
pip install -r requirements.txt
```

## Usage

1. **View the notebook:**
   ```bash
   jupyter notebook "Titanic dataset model.ipynb"
   ```

2. **Run the model:**
   - Open the notebook and execute cells sequentially
   - Model trains on Titanic dataset and generates predictions

3. **Check submissions:**
   - `submission.csv` contains final predictions (418 rows + 1 header)
   - Format: PassengerId, Survived (0 or 1)

## Model Performance

- **Format:** Binary classification
- **Evaluation:** Cross-validation metrics in notebook
- **Submission:** Kaggle Titanic competition format

## Kaggle Submission

The `submission.csv` file meets Kaggle submission requirements:
- ✓ 418 data rows + 1 header
- ✓ Columns: PassengerId, Survived
- ✓ Values: 0 or 1 (binary)
- ✓ Ready to upload

To submit:
1. Go to [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
2. Click "Make a submission"
3. Upload `submission.csv`
4. View leaderboard score.

## Key Results

- Total predictions: 418
- Survived (1): 156 passengers
- Did not survive (0): 262 passengers

## Notes

- Model trained on historical Titanic passenger data
- Predictions based on passenger features (class, age, gender, etc.)
- Binary classification approach (survived/not survived)

## Author

Created as a Kaggle competition project

## License

MIT License
