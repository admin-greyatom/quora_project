# How does your data look like ?

Hello budding Data scientist lets have a look at our data in a structred format.


## Write a function `q01_load_data_questions` that :
- Load the data into a dataframe of csv format.
- Calculates the length of the data frame , also calculate the mean value of column 'is_duplicate' rounded of to two places.	
- Combines the column named as 'qid1' and 'qid2' into one column.
- Calculates the questions that appear multiple times on the basis of above combined column.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path to the file csv |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| length | Dataframe for Data; CSV acceptable by sklearn | X_train |
| variable1  |Float | Rounded mean value of 'is_duplicate' |
| variable2 | integer | total count of duplicate questions |
| variable3 | pandas.Dataframe | dataset loaded from the given path |
