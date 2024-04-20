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
<img width="567" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/a992a714-1641-4392-8372-5cb93f8f3919">
<img width="567" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/62caeedb-b403-4867-b80a-d7eeae5e2ec9">
<img width="567" alt="image" src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/ae2335dd-a390-4168-abed-5f00fed8e1b1">









