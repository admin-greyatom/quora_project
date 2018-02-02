# TF-IDF


## Write a function `q06_TF_IDF` that :
- Makes use of previously created object named as `q01_load_data_questions`	
- Makes use of `TfidfVectorizer` function on concatnated column consisting features 'question1' and 'question2'.
- Applies the fitted model and transforms features 'question1' and 'question2' to string type.
- Calculates the absolute difference between above transformed features and store in new variable.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path to the file csv |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable1 | scipy.sparse.csr.csr_matrix | Absolute difference of transformed features 'question1' and 'question2'|
| variable1 | pandas.core.series.Series | Column consisting values of feature named as 'is_duplicate'|


Note :-
Use the following parameters while using `TfidfVectorizer` - (analyzer='word', stop_words='english', lowercase=True, max_features=300, norm='l1').
