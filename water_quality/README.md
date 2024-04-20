# Machine Learning for Safe Drinking Water Assessment 

## Project Background
Access to clean drinking water is a fundamental human right, yet millions globally lack this essential resource. This project explores the potential of machine learning to assess water potability. We propose a machine learning model that can analyze various water quality parameters to predict the presence of contaminants and classify water as safe or unsafe for consumption.

## Project Objectives
1. This project will explore how ML can leverage a vast array of water quality data to classify water sources as safe or unsafe for drinking. 
2. We will compare machine learning algorithms to identify the most effective approach for accurately classifying water potability. 
3. By pinpointing the most critical water quality indicators, we will gain insights to develop target monitoring strategies, maximising efficiency, and effectiveness. 
4. This project bridges the gap between traditional methods and cutting-edge AI, paving the way for faster, more efficient water safety assessments.

## Dataset Overview
This data obtained from Kaggle contains 21 different measurements for 8,000 water samples, allowing us to build powerful models to assess water safety. 

<img width="250" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/53c42798-48f1-451f-a218-e56c1aa85a79">  

- Metals: Aluminum, Arsenic, Barium, Cadmium, Chromium, Copper, Lead, Mercury, Silver, Uranium, Selenium, and Radium - These can be harmful at high levels.
- Chemicals: Ammonia, Chloramine, Fluoride, Nitrates, Nitrites, Perchlorate - These can indicate pollution or treatment processes.
- Biological: Bacteria, Viruses - These directly impact water safety.

## Exploratory Data Analysis
EDA provides insights into the dataset's characteristics and relationships. 
<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/35f39ac5-9fcb-400a-873f-db8d1c5c84e3">
<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/5379f0c8-7e0a-410d-9f1f-a63e78fc2b6b">

## Data Splitting
Data splitting aids in training and evaluating models effectively, allowing for robust validation and testing procedures. In this case, we split the data into 80% training and 20% testing. 

<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/b293f238-7b5d-486c-a2d5-0eda8d6fff88">

## Data Normalization 
Standard scaling, a preprocessing technique in machine learning, is applied to features to ensure they have a mean of zero and a standard deviation of one. This normalisation process is crucial for many machine learning algorithms, especially those that involve distance calculations or gradient descent optimisation. By standardising the features, the algorithm treats all features equally in terms of their influence on the model, preventing any particular feature from dominating the others due to its scale. This not only helps algorithms converge faster but also enhances their performance by making them less sensitive to the scale of input features, leading to more stable and reliable models overall.

<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/5164f678-0a5c-4a08-bf5d-509864072e58">

After applying StandardScaler():
![image](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/a8171930-82b0-406d-8f35-33b4672f7eef)

## Baseline Selection - Machine Learning Algorithms
<img width="265" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/a992a714-1641-4392-8372-5cb93f8f3919">
<img width="265" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/62caeedb-b403-4867-b80a-d7eeae5e2ec9">
<img width="265" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/ae2335dd-a390-4168-abed-5f00fed8e1b1">
<img width="265" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/a5714085-0a84-4e9a-afc4-0eca199d3a67">
<img width="265" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/55e9d452-8991-4ad0-905a-36fefb7d7f6b">

- Tree-based models demonstrate superior performance in accuracy and F1 scores compared to linear models. For instance, Decision Trees (DT) achieved an accuracy of 0.96 and an F1 score of 0.90, while Random Forest (RF) attained a similar accuracy and F1 score. 
- Notably, tree-based models exhibit lower overfitting on imbalanced data because they require less data for training, making even a few samples from the minority class sufficient. 
- Conversely, linear models like Logistic Regression (LR) and Support Vector Machines (SVM) also exhibit good accuracy scores, achieving the same scores of 0.91, respectively. 
- However, their F1 scores were lower, each registering a 0.71 and 0.70, respectively. This disparity stems from linear models' need for larger datasets to train effectively, leading to a good fit for majority-class data but an underfit for minority-class data.
- In general, the models exhibited overfitting on the majority class data, resulting in poor performance on minority class samples. 
- This overfitting caused the accuracy score to be considerably higher than the F1 score. 
- Notably, the models performed notably well in predicting the 'not safe' (0) class, with similar precision, recall, and F1 scores across all models. 
- However, for the 'safe' class (1), the models showed inadequate performance due to underfitting. 
This was because they did not receive sufficient training samples for the 'safe' class, leading to poor performance on minority class predictions.

## Hyperparameters Tuning on Decision Tree Classifier using GridSearchCV
<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/dfe83c55-efa9-469b-9429-1ce5d769b5ce">
<img width="1630" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/03047788-0913-4088-88a2-412689d45d71">

## Evaluation on Optimized Hyperparameters Decision Tree Classifier 
The classification results indicate a high level of performance overall. 

<img width="837" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/5d6faf49-2c84-494e-aa30-234d59cd905e">

- For the "Not Safe" class, precision, recall, and F1-score are all high, at 0.98, suggesting that the model effectively identifies instances belonging to this class with few false positives and negatives. 
- Similarly, for the "Safe" class, precision, recall, and F1-score are slightly lower but still respectable, at 0.84, indicating that while the model identifies instances of this class with good accuracy, there are some false positives and negatives. The accuracy of 0.96 reflects the overall proportion of correctly classified instances in the dataset. The macro and weighted averages of precision, recall, and F1-score are both high, indicating a balanced performance across classes. 
- Overall, the model demonstrates strong predictive capabilities with a weighted average F1-score of 0.96, suggesting its suitability for classification tasks.














