# XG Boost


## Write a function `q07_XGBoost` that :
- Makes use of previously created object named as `q06_TF_IDF` with path consisting of train file.
- Split the data in train and test set (80:20 split) with usage of function called in the above step with random state as 42.
- Defines the hyperparmeter as following -
	- params = {}
	- params['objective'] = 'binary:logistic'
    - params['eval_metric'] = 'logloss'
    - params['eta'] = 0.02
    - params['max_depth'] = 4
- Converts the X_train, X_test to matrix and and integrates into one.
- Fits the model on train set with input as above combined matrix and parameters as follows 
	- also set params as mentioned above
	- training set matrix
	- num_boost_round=400
	- Combined matrix of X_test and X_train
	- early_stopping_rounds=50
- Makes use of previously created object named as `q06_TF_IDF` with path consisting of test file and predict while making use of test data to compare it and return roc scores.



### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path to the file csv |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable1 | Float | Score between predicted and actual values|



