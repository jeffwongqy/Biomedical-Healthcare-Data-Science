# **Neural Network Approach for Calories Burnt Prediction**

![attribute](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/9797a2f0-ff1e-4de6-a746-8e29b453fc01)

### **Abstract**
This study compares the performance of a 1D-CNN model and a DNN model in predicting calorie expenditure. Cross-validation results reveal that both models demonstrate strong performance, yet the 1D-CNN model outperforms the DNN model in mean R2-score and RMSE. Specifically, the 1D-CNN model achieves a mean R2-score of 0.9910 and a mean RMSE of 4.3522, whereas the DNN model scores slightly lower with a mean R2-score of 0.9845 and a mean RMSE of 5.7260. Testing scores for the 1D-CNN model closely align with training scores, indicating robust generalization to unseen data, while the DNN model shows signs of potential overfitting. Thus, based on superior performance metrics and generalization ability, the 1D-CNN model emerges as the most suitable choice for predicting calorie expenditure in this context.

### **Project Background**
The increasing prevalence of sedentary lifestyles and the associated health risks have prompted a growing interest in developing accurate methods for estimating calories burnt during physical activities. Traditional methods such as heart rate monitoring and self-reporting have limitations in terms of accuracy and reliability. However, with the advancement of machine learning techniques, particularly neural networks, there is an opportunity to enhance the accuracy of calorie expenditure prediction.

Neural networks, inspired by the functioning of the human brain, have shown remarkable capabilities in pattern recognition and nonlinear mapping. By training a neural network model on a dataset containing various physiological and contextual parameters, such as heart rate, age, gender, duration, and type of physical activity, it is possible to create a predictive model that estimates calories burnt with greater precision.

This project aims to leverage neural network approaches to develop a robust and accurate system for predicting calories burnt during physical activities. By harnessing the power of machine learning, we seek to address the limitations of existing methods and provide individuals with a reliable tool to monitor and manage their energy expenditure effectively.

### **Project Objectives**
The primary objective of this project is to design and implement a neural network-based system capable of accurately predicting the calories burnt during different physical activities. To achieve this goal, the following specific objectives will be pursued:

1. Data Collection and Preprocessing: Gather a comprehensive dataset containing physiological and contextual parameters related to physical activities, including heart rate, age, gender, duration, and type of activity. Preprocess the data to ensure consistency and remove any outliers or noise.

2. Neural Network Model Development: Design and train a neural network architecture suitable for calorie expenditure prediction. Experiment with different network architectures, activation functions, and optimization algorithms to identify the most effective configuration.

3. Model Evaluation and Validation: Evaluate the performance of the trained neural network model using appropriate metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). Validate the model using cross-validation techniques to assess its generalization ability.

4. Performance Comparison: Compare the performance of the developed neural network approach with existing methods for calorie expenditure prediction, such as heart rate monitoring or self-reporting. Assess the accuracy, reliability, and usability of the proposed system in practical scenarios.
