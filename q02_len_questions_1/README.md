# How can visualise the character count in questions


## Write a function `q02_len_questions_1` that :
- Makes use of previously created object named as `q01_load_data_questions`	
- Combines the column named as 'question1' and 'question2' into one column, converts it into string type and stores it in a new variable.
- Extracts the total length of each observation from previous variable and plots a histogram.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path to the file csv |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable | pandas.Series | Combined column of 'question1' and 'question2' which is converted into string type|
