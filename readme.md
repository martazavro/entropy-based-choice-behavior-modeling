# Entropy-Based Approach to Modeling Reward-Dependent Choice Behavior in a Feature-Specific Reinforcement Learning Task

This is a part of undergraduate thesis conducted by [Marta Nahorniuk](https://www.linkedin.com/in/marta-nahorniuk-895403204/)  under the supervision of [Dr. Mehran Moradi Spitmann](https://www.linkedin.com/in/mehranspitmann)

## Overview
A decision is a central concept of **Behavioral Economics**, a detailed understanding of which has been a focus of research in various fields, and yet - it is still not fully discovered. The evolution of choice behavior computational models, particularly within the reinforcement learning framework, significantly improved the field. However, traditional models often struggle to accurately capture the complexities in decision-making and frequently demonstrate inconsistencies between expected and actual behavior - a phenomenon known as **undermatching**. This study leverages **entropy-based method**, a **model-free** approach based on information theory, to address the problem in **feature-specific reinforcement learning** tasks in which the agent is unaware of the task-reward connections. Unlike previous methodologies that primarily assess general decision-making tendencies, this study applies an entropy-based approach to explore the dynamics of choice behaviors driven by specific features in controlled experimental settings with monkeys. Our findings suggest that this entropy-based method not only **explains** feature-specific choice behavior significantly better than previously existing methods but also **improves** the **predictive accuracy** of computational models of choice. This approach represents a significant advance in integrating behavioral insights into computational frameworks across various scientific and technological domains. It also deepens our understanding of feature-specific choice behaviors and their impact on decision dynamics. Finally, the study contributes to the broader field of behavioral economics by providing a more precise way to explain the decisions and bridge gaps between theoretical economics and practical, observable behaviors in controlled experiments.


## Repository Structure

This repository is structured into multiple directories, here is an outline of the content and function of each directory:

- `data_helpers`: Contains utility scripts for data converting and handling.
   - `convert_all_to_json.m`: MATLAB script to convert data to JSON format.
   - `convert_all.m`: MATLAB script for converting data to CSV format.
   - `convert.m`: MATLAB script for converting a single experiment recording to CSV format.
   - `eda.py`: Exploratory data analysis in Python.

- `metrics`: Contains scripts and functions for entropy-based metrics calculations.
   - `behavioral_metrics.py`: Functions for calculating behavioral metrics, like p(win), p(stay), better-stay, lose-worse, etc.
   - `binary_to_decimal.py`: Binary matrix conversion to a list of decimal values.
   - `conditional_entropy.py`: The calculation of conditional entropy.
   -  `conditional_probability.py`: The calculation of conditional probability.
   - `entropy_metrics_efficient.py`: Efficient calculation of entropy-based metrics.
   - `entropy_metrics.py`: Calcultation functions for ERDS, EODS, ERODS and their decompositions.
   - `entropy.py`: Entropy calculation.
   - `get_metrics.py`: Script to calculate both traditional behavorial and entropy-based metrics.
   - `nansum_zero_helper.py`: A function that handles summation.

- `models`: Contains machine learning and other models for testing the efficiency of entropy-based approach.
   - `bilstm.py`: Bidirectional LSTM model.
   - `cnn.py`: Convolutional Neural Network model.
   - `gru.py`: Gated Recurrent Unit model.
   - `lstm.py`: Long Short-Term Memory model.
   - `stepwise_regression.py`: Script for stepwise regression analysis.

- `utils`: Contains utility scripts for various operations.
   - `config.py`: Configuration settings.
   - `merge_csv_to_one_dataset.py`: Script to merge multiple CSV files into one dataset.
   - `model_performance.py`: Script for evaluating model performance.
   - `train_preprocessing.py`: Script for data preprocessing before training.

- `visualisations`: Contains scripts for generating visualizations.

- `vizualisation_plots`: Contains various plots generated from the analysis.


## Dependencies
- Python 3.8+
- pandas
- numpy
- scikit-learn
- keras
- scipy
- matplotlib

### License
Distributed under the [**MIT**](https://github.com/martazavro/entropy-based-choice-behavior-modeling/blob/master/LICENSE) license.
