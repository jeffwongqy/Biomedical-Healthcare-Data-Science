# Machine Learning for Safe Drinking Water Assessment 
![water_quality](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/9b9dea7a-fd55-4588-b047-115de1265939)

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
### Classification Report:

<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/5d6faf49-2c84-494e-aa30-234d59cd905e">

- The classification results indicate a high level of performance overall. 
- For the "Not Safe" class, precision, recall, and F1-score are all high, at 0.98, suggesting that the model effectively identifies instances belonging to this class with few false positives and negatives. 
- Similarly, for the "Safe" class, precision, recall, and F1-score are slightly lower but still respectable, at 0.84, indicating that while the model identifies instances of this class with good accuracy, there are some false positives and negatives. The accuracy of 0.96 reflects the overall proportion of correctly classified instances in the dataset. The macro and weighted averages of precision, recall, and F1-score are both high, indicating a balanced performance across classes. 
- Overall, the model demonstrates strong predictive capabilities with a weighted average F1-score of 0.96, suggesting its suitability for classification tasks.

### Confusion Matrix:
<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/f1c7ef50-d5a3-4baa-a411-e2edcba55c0b">

- The top-left cell (1385) indicates the number of instances that were correctly classified as belonging to the "Not Safe" class (True Negatives).
- The top-right cell (33) indicates the number of instances that were incorrectly classified as "Safe" when they actually belonged to the "Not Safe" class (False Positives).
- The bottom-left cell (35) indicates the number of instances that were incorrectly classified as "Not Safe" when they actually belonged to the "Safe" class (False Negatives).
- The bottom-right cell (147) indicates the number of instances that were correctly classified as belonging to the "Safe" class (True Positives).
- From this confusion matrix, we can see that the model performs well overall, with a high number of true positives and true negatives. 
However, there are some misclassifications, as indicated by the false positives and false negatives. Overall, the model appears to have a higher accuracy in predicting the "Not Safe" class compared to the "Safe" class, as there are fewer false positives and more true negatives.

### ROC-AUC Curve:
<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/6f7e3cf2-6e9f-4e22-a04a-d73456267dcb">

- A higher AUC value (closer to 1) suggests better discrimination between the positive and negative classes, indicating that the model can effectively distinguish between them.

## Feature Importances on Optimized Hyperparameters of Decision Tree Classifier
<img width="500" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/11c29117-1ffe-40a8-987f-62c3749902e0">

- Based on the information provided above, it seems that cadmium, aluminium, chloramine, uranium, and silver have the highest average SHAP values in a model predicting water quality. This suggests that these features are influential in determining whether the water is classified as safe or not safe. 
- Cadmium, and Uranium: These elements are known to be highly toxic and can cause severe health problems even at low levels. Their high SHAP values suggest they strongly influence the model's prediction of unsafe water.
- Aluminium: While aluminium can be harmful at high concentrations, it's often present in treated water at regulated levels. The model might be sensitive to aluminium levels, but further analysis is needed to determine its impact on the "safe" classification.
- Chloramine: This disinfectant is commonly used in water treatment. Its SHAP value could indicate that the model considers chloramine presence as a positive factor for water safety, but it's essential to ensure proper levels are maintained to avoid harmful byproducts.
- Silver: Colloidal silver is sometimes used for water purification, but its effectiveness and safety are debated. A high SHAP value for silver might require further investigation into the model's training data and assumptions.
- SHAP values are for feature importance, not absolute safety. Just because a feature has a high SHAP value does not mean it is the sole determinant of safety. Other factors and interactions might also play a role. 

## Further Discussions
This isn't just about our research; it's about making clean water a reality!  Our models show promise for real-time water quality monitoring, which could be a major breakthrough in safeguarding drinking water. Imagine being able to instantly identify risky water sources! This could revolutionise public health, especially in areas with unpredictable water quality. By using these machine learning tools, authorities can effectively monitor water, identify problems quickly, and take action to protect people's health.

## Limitations
- While our study shows promise, it's important to acknowledge some limitations. We used historical data, which might not reflect the ever-changing nature of water quality. Additionally, we relied on standard safety thresholds that may not apply everywhere due to local factors like geography and environment.
- Moving forward, incorporating real-time data and considering regional variations would strengthen our approach. Overall, this research highlights the potential of machine learning for water quality assessment. By making the results understandable, identifying key factors, and demonstrating practical applications, we emphasize the value of automated systems in safeguarding clean drinking water.
- The limitations identified here serve as a guide for future research, paving the way for continuous improvement in water quality management and global public health.

## Future Scope
- The next step is to make our water quality assessments even more dynamic. Imagine incorporating live data feeds from sensors and other sources directly into our machine learning models. This constant flow of information would allow the models to learn and adapt in real-time, becoming more adept at spotting water quality issues the moment they arise. By ditching the reliance solely on historical data, we can achieve faster and more precise interventions, safeguarding public health more effectively.
- Investigate the potential of using powerful AI methods, like convolutional neural networks and recurrent neural networks, to unlock insights from intricate water quality data that has many variables.
- Let's build AI tools that explain their reasoning! This will help people who manage water quality trust the decisions these models make. Tools like LIME and SHAP can shed light on how these models arrive at their predictions, making them more transparent and reliable.

















