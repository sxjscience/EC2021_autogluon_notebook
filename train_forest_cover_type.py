import pandas as pd
from autogluon.tabular import TabularPredictor

train_df = pd.read_csv('forest-cover-type-prediction/train.csv.zip')
train_df = train_df.drop('Id', 1)
predictor = TabularPredictor(label='Cover_Type',
                             path='forest_cover_ensemble').fit(train_df, presets='best_quality')

# Inference
test_df = pd.read_csv('forest-cover-type-prediction/test.csv.zip')
test_predictions = predictor.predict(test_df)
submission_df = pd.read_csv('forest-cover-type-prediction/sampleSubmission.csv.zip')
submission_df.to_csv("stack_ensemble_submission.csv", index=False)
