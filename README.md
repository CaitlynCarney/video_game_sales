<a name="top"></a>
![Video Games](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/custom_header.png?raw=true)

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


## <a name="project_description"></a>
![desc](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/project_desc.png?raw=true)
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
    
    
## <a name="planning"></a>
![plan](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/project_planning.png?raw=true)
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

    
## <a name="findings"></a>
![find](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/key_findings.png?raw=true)

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

## <a name="dictionary"></a>
![dict](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/data_dict.png?raw=true)

[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Data Used
    
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| Rank  |  Ranking of overall sales | astype |     
| Name  |  The games name | astype |     
| Platform  |   Platform of the games release (i.e. PC,PS4, etc.) | astype | 
| Year  | Year of the game's release | astype |   
| Genre  |  Genre of the game | astype |   
| Publisher  |  Publisher of the game | astype |  
| NA_Sales  |  Sales in North America (in millions) | astype |  
| EU_Sales  |  Sales in Europe (in millions) | astype |  
| JP_Sales  |  Sales in Japan (in millions) | astype |  
| Other_Sales  |  Sales in the rest of the world (in millions) | astype |  
| Global_Sales  |  Total worldwide sales. | astype | 
    
\*  Indicates the target feature in this Zillow data.

***
</details>

## <a name="acquire_and_prep"></a>
![acquire_prep](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/acquire_prep.png?raw=true)
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



## <a name="explore"></a>
![dict](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/data_explore.png?raw=true)
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

## <a name="stats"></a>
![stats](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/stats.png?raw=true)
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

## <a name="model"></a>
![model](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/model.png?raw=true)
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Summary of modeling choices...

### Baseline
        
### Models and R<sup>2</sup> Values:
- Will run the following models:
    - ???

- Other indicators of model performance
    - R<sup>2</sup> Baseline Value
        - ?
    - R<sup>2</sup> OLS Value 
        - ?



### RMSE using Mean
    
Train/In-Sample:  ?
    
Validate/Out-of-Sample: ? 
    

### RMSE using Median
Train/In-Sample:  ?
Validate/Out-of-Sample:  ?

### Model
    
Training/In-Sample:  ?
    
Validation/Out-of-Sample:  ?
    

### Model
    
Training/In-Sample:  0.012348907010552293 
    
Validation/Out-of-Sample:  0.011532822479710627
    

### Eetc:

## Selecting the Best Model:

- ??? 

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Training/In Sample RMSE | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- | ---- |
| Baseline Mean | in sample  | out sample | r square |
| Baseline Median | in sample  | out sample | r square |
| model |  in sample  | out sample | r square |
| model |  in sample  | out sample | r square |
| model |  in sample  | out sample | r square |
| model |  in sample  | out sample | r square |
| model |  in sample  | out sample | r square |

- Why did I choose this model?
    - ???

## Testing the Model

- Model Testing Results
     - ???


***

</details>  

## <a name="conclusion"></a>
![conclusion](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/conclusion.png?raw=true)
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Initial Findings:

In the end:

We found that:

With further time: 

Recommend:


</details>  

![Folder Contents](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/file_pathing.png?raw=true)


>>>>>>>>>>>>>>>
.

