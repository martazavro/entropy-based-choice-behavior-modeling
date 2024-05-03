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



## Results

This project explores monkeys' choice behavior in feature-specific, reward-based learning tasks. With 216 sessions involving 9347 blocks and 75,138 trials, our study reveals that the fraction of times monkeys selected the better option often deviated from the matching law. Undermatching behavior, where the relative choice fraction is lower than the relative reward fraction, was commonly observed.

#### Method Efficiency

Traditional metrics, such as win-stay or lose-switch, explained up to 50% of the deviation from matching. We expanded the usage of entropy-based metrics to the context of feature-specific behavior, which improved explanatory power to 97%.

#### Predictive Power

Entropy-based metrics showed significant predictive power, outperforming traditional metrics. In particular, ERDS(lose) had a strong positive correlation (97%) with deviations from matching. The models using entropy-based metrics achieved higher R-squared values and lower RMSE.


| Model             | Agent | Approach      | RMSE         | MAE          | MAPE         | R-squared    |
|-------------------|-------|---------------|--------------|--------------|--------------|--------------|
| LSTM              | 1     | Entropy-Based | **0.03133**  | **0.01956**  | **15.54**    | **0.94719**  |
|                   | 2     | Entropy-Based | **0.02258**  | **0.01348**  | **9.14**     | **0.95544**  |
|                   | 1     | Traditional   | 0.05136      | 0.03348      | 29.27        | 0.85811      |
|                   | 2     | Traditional   | 0.04823      | 0.02139      | 18.92        | 0.90034      |
| GRU               | 1     | Entropy-Based | **0.03235**  | **0.01991**  | **15.31**    | **0.94370**  |
|                   | 2     | Entropy-Based | **0.02266**  | **0.01368**  | **9.19**     | **0.95511**  |
|                   | 1     | Traditional   | 0.05349      | 0.03581      | 29.88        | 0.84609      |
|                   | 2     | Traditional   | 0.02891      | 0.02208      | 19.15        | 0.92696      |
| CNN               | 1     | Entropy-Based | **0.03544**  | **0.02696**  | **20.18**    | **0.93246**  |
|                   | 2     | Entropy-Based | **0.01862**  | **0.01234**  | **10.57**    | **0.96969**  |
|                   | 1     | Traditional   | 0.07438      | 0.04594      | 30.94        | 0.70238      |
|                   | 2     | Traditional   | 0.04597      | 0.03477      | 26.58        | 0.81524      |
| Bidirectional LSTM| 1     | Entropy-Based | **0.04091**  | **0.02776**  | **16.76**    | **0.90996**  |
|                   | 2     | Entropy-Based | **0.02676**  | **0.01897**  | **13.35**    | **0.93741**  |
|                   | 1     | Traditional   | 0.06744      | 0.04750      | 34.75        | 0.75536      |
|                   | 2     | Traditional   | 0.03919      | 0.02970      | 26.93        | 0.86576      |



Entropy-based metrics significantly enhanced computational models of decision-making in feature-specific environments. These metrics consistently outperform traditional methods, offering valuable insights into complex behaviors.







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
