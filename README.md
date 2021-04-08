README.md Outline

# Predicting Heart Failure

# <a name="top"></a>Finding Log Error for Zillow - README.md
![Zillow Logo](https://github.com/Zillow-Project/zillow_project_2021/blob/main/Caitlyn/photos/Screen%20Shot%202021-04-01%20at%205.57.59%20PM.png?raw=true)
​
***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Acquire & Prep](#acquire_and_prep)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___
​
​
## <a name="project_description"></a>Project Description:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Description
- ???

### Goals
- ???

### Where did you get the data?
- ???

</details>
    
    
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

### Projet Outline:
    
- Acquisiton of data ....
- Prepare and clean data with python - Jupyter Labs
- Explore data
    - What are the features?
    - Null values
        - Are the fixable or should they just be deleted
    - Categorical or continuous values
    - Make graphs that show 
        - At least 2
- Run statistical analysis
    - At least 2
- Modeling
    - Make multiple models
    - Pick best model
    - Test Data
    - Conclude results
        
### Hypothesis
- ???

### Target variable
- ???

</details>

    
## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Explore:
- I learned:
    - ???

### Stats
- Stat Test: 
    - which test:
        - reject of accept null
- Stats test:
    - which test:
        - reject of accept null
- Stats test:
    - which test:
        - reject of accept null

### Modeling:
- Baseline:
- Models Made:
- Best Model:
- Model testing:
- Performance:

***

    
</details>

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Data Used
    
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| feature  |  description | astype |     
| feature  |  description | astype |     
| feature  |  description | astype | 
| feature  |  description | astype |   
| feature  |  description | astype |   
    
\*  Indicates the target feature in this Zillow data.

***
</details>

## <a name="acquire_and_prep"></a>Acquire & Prep:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Acquire Data:
- ???

### Prepare Data
- To clean the data I had to:
    - ?
- From here I :
    - Split the data into train, validate, and test
    - Split train, validate, and test into X and y
    - Scaled the data

***
​
</details>



## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>
    
- wrangle.py 

### Findings:
- ???
​
### Function1 used:
- Outcome of the use of the function 
​
### Function2 used:
- Outcome of the use of the function 
​
***
​
</details>    

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>


### Stats Test 1:
- What is the test?
    - ???
- Why use this test?
    - ???
- What is being compared?
    - ???

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is...
    - "___"
- The alternate hypothesis (H<sub>1</sub>) is ...
    - "___"


#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- Reject the null
- move forward with Alternative Hypothesis 

- Summary:
    - F score of:
        - ???
    - P vlaue of:
        - ???

### Stats Test 2: 
- What is the test?
    - ???
- Why use this test?
    - ???
- What is being compared?
    - ???

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is...
    - "___"
- The alternate hypothesis (H<sub>1</sub>) is ...
    - "___"


#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- Reject the null
- move forward with Alternative Hypothesis 

- Summary:
    - F score of:
        - ???
    - P vlaue of:
        - ???

***
​
    
</details>    

## <a name="model"></a>Modeling:
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Summary of modeling choices...

### Baseline

- Baseline Results: 
    - Median In sample = 0.16
    - Median Out of sample = 0.15
        
### Models and R<sup>2</sup> Values:
- Will run the following models:
    - Linear regression OLS Model
    - Lasso Lars
    - Tweedie Regressor
    - Polynomail Degree 2
    - Ploynomial Degree 3

- Other indicators of model performance
    - R<sup>2</sup> Baseline Value
        - -0.004585
    - R<sup>2</sup> OLS Value 
        - 0.00005159



### RMSE using Mean
    
Train/In-Sample:  0.16 
    
Validate/Out-of-Sample:  0.15
    

### RMSE using Median
Train/In-Sample:  0.16 
Validate/Out-of-Sample:  0.15

### RMSE for OLS using LinearRegression
    
Training/In-Sample:  0.15698193096987265 
    
Validation/Out-of-Sample:  0.1518694361646674
    

### RMSE for Lasso + Lars
    
Training/In-Sample:  0.012348907010552293 
    
Validation/Out-of-Sample:  0.011532822479710627
    

    
### RMSE for GLM using Tweedie, power=0 and alpha=0
    
Training/In-Sample:  0.01234045919349956 
    
Validation/Out-of-Sample:  0.011536767590909373
    

    
### RMSE for Polynomial Model, degrees=2
    
Training/In-Sample:  0.012288891953326782 
    
Validation/Out-of-Sample:  0.011543443686491118
    

    
### RMSE for Polynomial Model, degrees=3
    
Training/In-Sample:  0.012288891953326782 
    
Validation/Out-of-Sample:  0.011543443686491118


### Eetc:

## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Training/In Sample RMSE | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- | ---- |
| Baseline | 0.16  | 0.15 | -0.004585 |
| Linear Regression |  0.15698193096987265  | 0.1518694361646674 | 0.00005159 |
| Tweedie Regressor (GLM) | 0.01234045919349956  | 0.011536767590909373 | n/a |
| Lasso Lars | 0.012348907010552293  | 0.011532822479710627 | n/a |
| Polynomial Regression D2| 0.012288891953326782  | 0.011543443686491118 | n/a |
| Polynomial Regression D3| 0.012288891953326782  | 0.011543443686491118 | n/a |

- Why did you choose this model?
    - It was closer to 0 than our baseline.

## Testing the Model

- Model Testing Results
     - Out-of-Sample Performance:  0.1518694361646674


***

</details>  

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

We found that only about 9.36% of log error was inaccurate. Meaning that it was below -0.15 or above 0.15 rendering it inaccurate.

This gave us a small amount to work with. But in the end we were able to create a model to find certain drivers of the inaccurate log error.
Our model performed better than the baseline by a decent amount. With a R baseline of ~-0.0046 and our model performing at ~0.000052. Meaning we were able to get closer to 0 than our baseline.

We found that Ventura, north downtown LA, tax values, home quality, and a homes age affect loerror within their resepective cluster.

With further time we would like to look further into geographical location and tax values to see if there is a more specific reason for log error.

We recommend using our OLS model to be used within the field, in order to establish a closer zestimate score to what the selling price may be, in order to service our custoemrs even better.


    

</details>  

![Folder Contents](https://github.com/Zillow-Project/zillow_project_2021/blob/main/Caitlyn/photos/ScreenShot2021-04-06at12.52.26PM.png?raw=true)


>>>>>>>>>>>>>>>
.

