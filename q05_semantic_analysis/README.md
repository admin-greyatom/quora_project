# How can we measure usage of different punctuation in questions ?


## Write a function `q05_semantic_analysis` that :
- Makes use of previously created object named as `q02_len_questions_1`	
- Makes use of lamda function to extract the following specified characters from questions and store it in different variables.
      - '?'
      - '[math]'
      - '.'
      - Capitalised first letters
      - Capital letters
      - Numbers
	

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path to the file csv |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable1 | Float | Count of '?' characters in the questions |
| variable2 | Float | Count of '[math]' characters in the questions|
| variable3 | Float | Count of '.' characters in the questions|
| variable4 | Float | Count of Capitalised first letters characters in the questions|
| variable5 | Float | Count of Capital letters characters in the questions|
| variable6 | Float | Count of number characters in the questions|

