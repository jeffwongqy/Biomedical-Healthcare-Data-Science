# Predictive Modeling of Lung Cancer Adenocarcinoma Genes Using Tree-Based Approaches

<img src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/35e35cd7-2507-47d5-8079-8a11cbaf7b07" width="500" alt="Lung Cancer Image">

## Project Background
Lung cancer remains one of the most prevalent and lethal forms of cancer worldwide, with adenocarcinoma being its most common subtype. Despite advancements in treatment, the prognosis for lung adenocarcinoma patients often remains poor due to late-stage diagnoses and limited understanding of the molecular mechanisms driving the disease.

Recent breakthroughs in genomic sequencing have provided researchers with vast amounts of data on the genetic alterations associated with lung adenocarcinoma. However, the complexity and heterogeneity of these genomic profiles present significant challenges in identifying key genes and pathways involved in the development and progression of the disease.

In this context, predictive modeling techniques offer a promising approach to uncovering the genetic signatures underlying lung adenocarcinoma. By leveraging tree-based approaches, such as decision trees, random forests, and gradient boosting machines, researchers can analyze large-scale genomic datasets to identify biomarkers, molecular pathways, and potential therapeutic targets with greater accuracy and efficiency.

## Project Objective
The primary objective of this project is to develop and validate predictive models for identifying key genes associated with lung adenocarcinoma using tree-based approaches. Specifically, the project aims to:

1. Data Collection and Preprocessing: Gather comprehensive genomic datasets, including gene expression profiles, somatic mutations, copy number variations, and clinical data, from public repositories and research cohorts. Preprocess the data to remove noise, correct for batch effects, and standardize features for compatibility with tree-based algorithms.

2. Feature Selection and Model Training: Employ various tree-based algorithms, such as decision trees, random forests, and gradient boosting machines, to select informative features and build predictive models. Explore different parameter settings and ensemble techniques to optimize model performance and generalization across diverse datasets.

3. Model Evaluation and Interpretation: Assess the predictive accuracy, robustness, and generalizability of the developed models using cross-validation, independent validation cohorts, and performance metrics such as the area under the receiver operating characteristic curve (AUC-ROC) and precision-recall curve. Interpret the models to identify key genes, molecular pathways, and biological insights underlying lung adenocarcinoma progression.

4. Clinical Translation and Validation: Validate the predictive models in clinical settings using patient-derived samples and real-world data. Evaluate the models' utility in predicting patient outcomes, treatment response, and disease prognosis, and assess their potential for guiding personalized therapeutic interventions and clinical decision-making.

## Data Collection
Collected data from BARRA:CuRDa (https://sbcb.inf.ufrgs.br/barracurda) is to utilize a curated RNA-seq database specifically tailored for cancer research, ensuring high-quality and relevant genomic data for analysis and modeling in the context of lung cancer adenocarcinoma.

## Data Preprocessing
(A) Select the first 50 columns for analysis:  To reduce computational complexity while focusing on the most relevant features for initial exploration and modeling.
(B) Check for missing values: To ensure data completeness and integrity for accurate analysis and modeling.
(C) Distribution of Samples Corresponding to Each Lung Cancer Types: To understand the variability and characteristics of each type, aiding in the identification of potential patterns or differences that could inform diagnosis, prognosis, or treatment strategies.

## Data Splitting
Splitting data into 80% training and 20% testing is to train machine learning models on a majority of the data while reserving a portion for independent evaluation, ensuring the model's generalizability and performance on unseen data.
![Screenshot 2024-04-20 224823](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/67bf1db7-a3ea-47dc-8b65-985c1a9ddc7b)

## Data Resampling - SMOTE-Tomek
Using SMOTE-Tomek to resample the class labels is to address the class imbalance by synthesizing new minority class instances while simultaneously removing potentially noisy or borderline instances, improving the model's ability to learn from imbalanced data.

<img src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/67fa90ec-65e7-4c83-820d-29b95b43026a" width="700" alt="Screenshot Image">

<img src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/5dda9c70-a1af-49f3-bae2-18e6f057a07f" width="350" alt="Output Image">

<img src="https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/2bc3d43e-ebd2-4954-8a31-1145fe295cb1" width="350" alt="Output2 Image">

## Data Transformation
(A) Standard Scaler: To apply standard scaling transformation to numerical features, ensuring they are centered around zero with a standard deviation of one for improved model performance and interoperability.

![Screenshot 2024-04-20 225737](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/9fdd06ca-55ec-4ab9-abdd-c48fe6241800)

![Screenshot 2024-04-20 225828](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/125ca150-2389-401f-8360-a2d27efc6c4c)

(B) Label Encoder: To utilize label encoding to transform categorical features into numerical representations, facilitating machine learning algorithms' ability to process categorical data effectively.

![Screenshot 2024-04-20 225933](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/b4615826-0650-4587-a357-1ab9058831fb)

![Screenshot 2024-04-20 225920](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/f59f47b8-5c0c-4976-b43d-79bae2088267)

## Baseline Model Selection
Selecting a baseline model using **default parameters** and from **stratified k-fold cross-validation** as well as **hold-out validation**is to establish a robust initial benchmark for model performance, considering both default parameter settings and cross-validation to ensure a reliable comparison across different folds and to provide a solid foundation for subsequent model refinement and evaluation.

Considering both metrics, it seems that the Extra Trees Classifier or Random Forest Classifier has the highest accuracy on both the stratified k-fold validation and the hold-out test set. Therefore, we may want to choose the Extra Trees Classifier or Random Forest Classifier for further hyperparameter optimization.

NOTE: Check out the Jupyter Notebook for more detailed results. 

## Hyperparameters Optimization - Random Forest Classifier
Hyperparameter optimization is crucial for Random Forest Classifier despite its high performance because it allows fine-tuning of parameters to further enhance its effectiveness. While Random Forests are robust and versatile, adjusting hyperparameters such as the number of trees, maximum depth of trees, and minimum samples per leaf can optimize its performance for specific datasets and tasks. Hyperparameter optimization ensures that the Random Forest Classifier is effectively tailored to the characteristics of the data, potentially improving accuracy, generalization, and computational efficiency. This process maximizes the algorithm's potential and ensures that it achieves the best possible performance across different scenarios, ultimately leading to more reliable and accurate predictions.


![Screenshot 2024-04-20 230220](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/37971c87-63d2-4e55-ad2d-ed5e3677b611)


![Screenshot 2024-04-20 230348](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/04456682-4f7f-4293-90b3-6a2b12de96fb)

## Model Training and Evaluation using Optimized Hyperparameters for RFC
Model training and evaluation on a hyperparameter-optimized Random Forest Classifier ensure maximized performance by fine-tuning parameters for optimal accuracy and generalization.

![Screenshot 2024-04-20 230444](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/240707c6-0433-4310-b35f-57514d5f0953)

Classification Report:

![Screenshot 2024-04-20 230522](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/c1ab029b-3a48-4b11-8428-9817df9e90f7)

The classification report for the optimized Random Forest Classifier reveals strong performance on both the training and testing sets. With precision, recall, and F1-score all consistently high across both classes, the model demonstrates robustness in correctly identifying instances of both classes. The weighted average F1-score of 0.99 for the training set indicates excellent overall performance, while the testing set's weighted average F1-score of 0.94 suggests generalization to unseen data, though slightly lower than the training set. These results signify effective hyperparameter optimization, resulting in a well-generalized model with high accuracy and balanced performance across classes.

ROC-AUC Curve:

![output](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/db4fba4a-f66c-4e71-8bf0-d8c932c0d9e5)

A high AUC of 0.9936 for the training set indicates excellent discrimination ability, suggesting that the model can effectively differentiate between positive and negative instances in the training data. However, the AUC of 0.9315 for the testing set, while still relatively high, is slightly lower than that of the training set. This discrepancy suggests that while the model performs well on unseen data, there may be some degree of overfitting to the training data. Nonetheless, the testing set's AUC value still indicates strong discriminatory power and suggests that the model's performance generalizes well to new data, albeit with a slight drop in performance compared to the training set.

Confusion Matrix:

![output2](https://github.com/jeffwongqy/Biomedical-Healthcare-Genomics-Data-Science/assets/100281127/803acf61-971e-4ac9-a9a7-cacf13ac7759)

The confusion matrices provide a detailed breakdown of the performance of the optimized Random Forest Classifier on both the training and testing sets. In the training set, there were 162 true positives (TP) and 162 true negatives (TN), indicating that the model correctly classified instances of both classes. There was only one false positive (FP) and one false negative (FN), indicating a high level of accuracy and balance in classification. Similarly, in the testing set, there were 38 true positives and 21 true negatives, showing the model's ability to correctly identify instances of both classes in unseen data. However, there were two false positives and two false negatives, suggesting a slight decrease in performance compared to the training set. Overall, the results indicate strong performance and generalization of the model to new data, albeit with a small amount of misclassification.





