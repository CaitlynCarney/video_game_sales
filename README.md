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
- There are many things that may influence how much a game might sell. And throughout the years there have been many kinds of games on many different platforms that have been released. But what is driving game sales through the years? What determines a games success level? That is what I aim to find out here.

### Goals
- Determine drivers a game success level.
- Create a prediction model to predict the level of success with as much accuracy as possible.

### Where did you get the data?
- Acquire the data from [kaggle data set](https://www.kaggle.com/gregorut/videogamesales?select=vgsales.csv)
    - Generated by a scrape of vgchartz.com.
        - The script to scrape the data is available at GregorUT/vgchartzScrape.
        - It is based on BeautifulSoup using Python.
    - There are 16,598 records. 2 records were dropped due to incomplete information.

</details>
    
    
## <a name="planning"></a>
![plan](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/project_planning.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Projet Outline:
    
- Acquisiton of data
- Prepare and clean data with python - Jupyter Labs
    - Drop
    - Rename
    - Create
    - Dummies
    - Etc.
- Explore data:
    - What are the features?
    - Null values:
        - Are the fixable or should they just be deleted.
    - Categorical or continuous values.
    - Make graphs that show:
        - At least 2.
- Run statistical analysis:
    - At least 2.
- Modeling:
    - Make multiple models.
    - Pick best model.
    - Test Data.
    - Conclude results.
        
### Hypothesis
- The year the game came out in affects the success rates. There may have been economic crashes one year causing less game to be sold, there may have been an increase of games sold in 1980 than there was in 1990 because video games were new and magic, etc.
- Game sales are effected by the platform it is being sold on. For example Game A may have more sales because it is being sold on a Playstation platfrom, but game B didn't sell as high because it was being sold on Sega.
- Lastly the games primary genre effects game sales because some genres are more popular than others.

### Target variable
- `level_of_success`
    - This was a created feature where the `Global_Sales` feature was binned together.
        - Moderate Success:
            - Only sold 100,000 copies.
        - Fairly Successful:
            - Sold between 100,000 and 500,000.
        - Very Successful:
            - Sold between 500,000 and 900,000.
        - Extremely Successful:
            - Sold over a million copies.

</details>

    
## <a name="findings"></a>
![find](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/key_findings.png?raw=true)

[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Explore:
- I learned:
    - Strongest correlations to sales are:
        - Year of realease with a correlation of -0.08
        - Nintendo Platform with a correlation of -0.07
    - Approximatly 72% of all extremely successful games were made between 1985 and 1990.
    - Moderatly Successful games were at an all time lowbetween 1980 and 1985
        - The amount of moderatly successful games grow more and more through the years.
    - The years between 1980 to 1985 made up 42% of all fairly successful games and 21% of all very successful games.
    - 3,549 games were made between 2005 and 2010
        - With 39.7% being of Moderate Success
        - 38.8% being Fairly succcessful
    - 72% of all the games made in 1985 were extremely successful
    - About 15.8% of Moderate Success comes from Nintendo games.
    - Playstation's has a fairly goo distribution of success.
        - Their moderate succes makes up abotu 39% of all moderatly successful games.
        - Their Fairly successful games make up about 40% of all fairly successful games.
        - Very success makes up for about 33% of all of the very successful games.
        - Finaly their extremely successful games make up for about 32% of all extremely successful games.
    - Xbox tends to put out more Very Successful games thatn any other sucess rate.
        - Makes up for about 2% of all Very Successful games
            - This is not very much compared to the others but is their highest output in success level.
    - Computer Platforms have a pretty steady amount of copies sold in all amounts.
        - Their moderate succes makes up abotu 32% of all moderate successful games
        - Their Fairly successful games make up about 34% of all fairly successful games.
        - Very success makes up for about 42% of all very successful games.
        - Extremely successful games make up for about 43% of all extremely successful games
    - Nintendo puts out more games of moderate success
    - Playstation pits out an even amount of moderate and fairly successful games
    - Xbox games usually range between fairly successful and very successful
    - Computer games are pretty even distributed accross all 4 success levels
    - Sega games tend to be of Moderate or Fair success
    - All other game platforms are usually of moderate success or fairly successfu
    - Action Adventure Games have the highest percentage of game success across all success levels
        - Ranging from ~24% to ~32%
    - Sport games and RPG's both tend to be on the low end of success percents, but both have a spike when selling over 1 million copies.
    - The Biggest sellers when it comes to genre are Action Adventure, Strategy, and Shooters.
    - There are far many Action Adventure games made than any other.
        - Total of 2,545 individual titles.
    - Strategy is the second highest with 2,304 games which is 19.27% of games.
    - The lowest produced game type that sold a minimum of 100 thousand copies is Sports with only 876 game titles.
    
    

### Stats
- Stat Test 1: 
    - Chi Square
        - Rejected the null hypothesis that : A games genre and its level of success are independent from each other.
            
- Stats test 2:
    - Chi Square
        - Failed to reject the null hypothesis that : A games publisher and its level of success are independent from each other.
    
- Stats test 3:
    - Chi Square
        - Rejected the null hypothesis that : A games release year and its level of success are independent from each other.
    
- Stats test 4:
    - Chi Square
        - Rejected the null hypothesis that : A games platform and its level of success are independent from each other.

### Modeling:
- Baseline:
    - 0.3938
- Models Made:
    - Logit 1, 2, and individuals for each feature.
        - Accuracy of Logit 1 Model on Train: 
             - 0.4266
    - KNN
        - Accuracy of KNN Model on Train: 
             - 0.4696
    - Decision Tree
        - Accuracy of Decision Tree Model on Train: 
             - 0.4339
    - Random Forest
        - Accuracy of Random Forest Classifier on Train: 
             - 0.4486
- Best Model:
    - Decision Tree Model
- Model testing:
    - Accuracy of Decision Tree Model on Validate: 
         - 0.4269
- Performance:
    - Accuracy of Decision Tree Model on Test: 
         - 0.4339

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
| Action_Adventure  |  Action Adventure game or not | uint8 |        
| Computer  |  Computer platform or not | uint8 |    
| Extremely_Successful  |  If the game was extremely successful or not | uint8 | | Fairly_Successful  |  If the game was fairly successful or not | uint8 |    
| Genre  |  Genre of the game | object |      
| Global_Sales  |  Total worldwide sales. | float64 |     
| level_of_success  |  Levels of success based on Global Sales | category |   
| Misc  |  Miscellaneous game or not | uint8 |    
| Moderate_Success  | If the game had moderate success or not | uint8 |  
| Nintendo  |   Nintendo platform or not | uint8 |
| Other  |  Other platform or not | uint8 |   
| Platform  |   Platform of the games release (i.e. PC,PS4, etc.) | object |     
| Playstation  | Playstation platform or not | uint8 |       
| Publisher  |  Publisher of the game | object |      
| Role_Playing  |  RPG or not | uint8 |  
| Sega  |  Sega platform or not | uint8 |  
| Shooter  |  Shooter game or not | uint8 | 
| Simulation  |   Simulation game or not | uint8 | 
| Sports  | Sports game or not | uint8 |   
| Strategy  |  Strategy game or not | uint8 | 
| Very_Successful  |  If the game was very successful or not | uint8 |  
| Xbox  |Xbox platfrom or not | uint8 |        
| Year  | Year of the game's release | int64 |   
| years_binned  |  Year of the games realse binned in 5's | category |     
  
    
\*  Indicates the target feature in this Zillow data.

***
</details>

## <a name="acquire_and_prep"></a>
![acquire_prep](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/acquire_prep.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Acquire Data:
- Acquire the data from [kaggle data set](https://www.kaggle.com/gregorut/videogamesales?select=vgsales.csv)
    
### Prepare Data
- To clean the data I had to:
    - Move column names from row 1 to the column names.
    - Drop the row with the column names.
    - Drop columns from `Year` column where variable is 'N/A'.
    - Changes Year and Sales to int/float
    - Drop columns that feed right into target variable.
    - Bin the year column
    - Make new feature `level_of_success` which is binned global sales.
        - This is the target.
    - Push together varaibles from platform and genre to minimize dummies.
    - Create dummies.
    - Concats dummys to df
- From here I :
    - Split the data into train, validate, and test
    - Split train, validate, and test into X and y

***

</details>



## <a name="explore"></a>
![dict](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/data_explore.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>
    
- wrangle.py 

### Findings:
- I learned:
    - Approximatly 72% of all extremely successful games were made between 1985 and 1990.
    - Moderatly Successful games were at an all time lowbetween 1980 and 1985
        - The amount of moderatly successful games grow more and more through the years.
    - The years between 1980 to 1985 made up 42% of all fairly successful games and 21% of all very successful games.
    - 3,549 games were made between 2005 and 2010
        - With 39.7% being of Moderate Success
        - 38.8% being Fairly succcessful
    - 72% of all the games made in 1985 were extremely successful
    - About 15.8% of Moderate Success comes from Nintendo games.
    - Playstation's has a fairly goo distribution of success.
        - Their moderate succes makes up abotu 39% of all moderatly successful games.
        - Their Fairly successful games make up about 40% of all fairly successful games.
        - Very success makes up for about 33% of all of the very successful games.
        - Finaly their extremely successful games make up for about 32% of all extremely successful games.
    - Xbox tends to put out more Very Successful games thatn any other sucess rate.
        - Makes up for about 2% of all Very Successful games
            - This is not very much compared to the others but is their highest output in success level.
    - Computer Platforms have a pretty steady amount of copies sold in all amounts.
        - Their moderate succes makes up abotu 32% of all moderate successful games
        - Their Fairly successful games make up about 34% of all fairly successful games.
        - Very success makes up for about 42% of all very successful games.
        - Extremely successful games make up for about 43% of all extremely successful games
    - Nintendo puts out more games of moderate success
    - Playstation pits out an even amount of moderate and fairly successful games
    - Xbox games usually range between fairly successful and very successful
    - Computer games are pretty even distributed accross all 4 success levels
    - Sega games tend to be of Moderate or Fair success
    - All other game platforms are usually of moderate success or fairly successfu
    - Action Adventure Games have the highest percentage of game success across all success levels
        - Ranging from ~24% to ~32%
    - Sport games and RPG's both tend to be on the low end of success percents, but both have a spike when selling over 1 million copies.
    - The Biggest sellers when it comes to genre are Action Adventure, Strategy, and Shooters.
    - There are far many Action Adventure games made than any other.
        - Total of 2,545 individual titles.
    - Strategy is the second highest with 2,304 games which is 19.27% of games.
    - The lowest produced game type that sold a minimum of 100 thousand copies is Sports with only 876 game titles.

***

</details>    

## <a name="stats"></a>
![stats](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/stats.png?raw=true)
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>


### Stats Test 1:
- What is the test?
    - Chi Sqare
- Why use this test?
    - Find if the 2 variables are dependent or not
- What is being compared?
    - Genre and Success Level

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is...
    - "A games genre and its level of success are independent from each other"
- The alternate hypothesis (H<sub>1</sub>) is ...
    - "The genre of a game and its success are dependent on one another."


#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- Reject the null
- move forward with Alternative Hypothesis 

- Summary:
    - F score of:
        - 0.023
    - P vlaue of:
        - 0.05

### Stats Test 2: 
- What is the test?
    - Chi Sqare
- Why use this test?
    - Find if the 2 variables are dependent or not
- What is being compared?
    - Publisher and Success Level

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is...
    - "A games publisher and its level of success are independent from each other"
- The alternate hypothesis (H<sub>1</sub>) is ...
    - "The publisher of a game and its success are dependent on one another."


#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- Fail to reject the null.
- Do not move forward with publisher.

- Summary:
    - F score of:
        - 1.0
    - P vlaue of:
        - 0.5

### Stats Test 3:
- What is the test?
    - Chi Sqare
- Why use this test?
    - Find if the 2 variables are dependent or not
- What is being compared?
    - Tears Binned and Success Level

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is...
    - "A games release year and its level of success are independent from each other"
- The alternate hypothesis (H<sub>1</sub>) is ...
    - "The release year of a game and its success are dependent on one another."


#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- Reject the null
- Move forward with Alternative Hypothesis 

- Summary:
    - F score of:
        - 6.712021410509012e-123
    - P vlaue of:
        - 0.05    
    
### Stats Test 4:
- What is the test?
    - Chi Sqare
- Why use this test?
    - Find if the 2 variables are dependent or not
- What is being compared?
    - Platform and Success Level

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is...
    - "A games platform and its level of success are independent from each other"
- The alternate hypothesis (H<sub>1</sub>) is ...
    - "The platform of a game and its success are dependent on one another."


#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- Reject the null
- Move forward with Alternative Hypothesis 

- Summary:
    - F score of:
        - 7.614105483906174e-144
    - P vlaue of:
        - 0.05        
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
    - Linear Regression
        - Logit 1
        - Logit 2
        - One for each individual feature.
    - KNN
    - Decision Tree
    - Random Forest
    - Ridge Classifier
- Other indicators of model performance
    - Baseline

### Baseline Accuracy  
- 0.394
    
### Logit 1 Model
Model Accuracy:  0.4266
    
### Logit 2 Model
Model Accuracy:  0.32

### Individual Logits'
Model Accuracy:  0.39 - 0.43
    
### KNN Model
Model Accuracy:  0.4696
    
### Decision Tree Model
Model Accuracy:  0.4339
    
### Random Forest Model
Model Accuracy:  0.4486
    
### Ridge Classifier
Model Accuracy: 0.4546
    

## Selecting the Best Model:

- Ridge Classifier
    - The Baseline Accuracy is: 0.3938
    - Accuracy of Ridge Classifier Model on Train: 0.4546
    - Accuracy of Ridge Classifier Model on Validate: 0.445
    - Accuracy of Ridge Classifier Model on Test: 0.4546

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Accuracy with Train | Accuracy with Validate | Accuracy with Test|
| ---- | ----| ---- | ---- |
| Logit 1 |  0.4266  | 0.4271 | 0.4235 |
| Decision Tree |  0.4339  | 0.4269 | 0.4339 |
| KNN |  0.4696  | 0.4167 | 0.4133 |
| Random Forest |  0.4486  | 0.4412 | 0.432 |
| Ridge Cclassifier |  0.4546  | 0.445 | 0.4546 |

- Why did I choose this model?
    - I originally went with the KNN model because of its performance in the train data however it under performed compared to all other in the test data.
        - Form here I ran the others as well and fount that the Ridge Classifier model was the one that performed well in all 3 tests.

## Testing the Model

- Model Testing Results
     - 0.4546


***

</details>  

## <a name="conclusion"></a>
![conclusion](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/conclusion.png?raw=true)
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Initial Findings:
    
I found that there is a different distribution of games success levels based on the year they were released. With 1985 to 1990 putting out 72% of all extremely succesful games, 1980 to 1995 making up for 42% of all fairly successful games and 21% of all very successful games.
    
I also found that a games platform had diffrent amounts of success. Nintendo platform for example put out more modetatly successful games, making up for 15.8% of all of this success level. Playstation platforms tend to have higher numbers of titles across all leveles of success, as well as computer platforms. Xbox puts out more very successful game than any other of the success levels and finally Sega tends to be of moderate or fairly successful games.
    
Lastly I found that genres each have different amounts of success. Action adventure being the most through all levels (probably because it is the most made genre). Sports and RPG's tend to be on the lower end of the success rates.
    
The biggest sellers when it comes to genre are action adventure, strategy, and shooters. There are far more action adventure games made than any other, with a total of 2,545 individual titles which is 30.2% of all games. Strategy is the second highest with 2,304 games which is 19.27% of all games. The lowest produced game type that sold a minimum of 100 thousand copies is Sports with only 876 game titles.

In the end:
    
I found that genre, year, and platform have an effect on the level of success a game would have. Although, it is not perfect, it does give us insight to how much success a game may have.

With further time I would like to see about getting further data maybe including critic scores, developer, if the game is online or not, multiplayer or solo, and possibly the amount of time the game was in development.

I recommend utalizing the Ridge Classifier model to help give insight to a games possible level of success within the industry.


</details>  

![Folder Contents](https://github.com/CaitlynCarney/Video_Game_Sales/blob/master/Workbooks/photos/file_pathing.png?raw=true)


>>>>>>>>>>>>>>>
.

