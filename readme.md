# Entropy-Based Approach to Modeling Reward-Dependent Choice Behavior in a Feature-Specific Reinforcement Learning Task



## Overview
A decision is a central concept of \textbf{behavioral economics}, a detailed understanding of which has been a focus of research in various fields, and yet - it is still not fully discovered. The evolution of choice behavior computational models, particularly within the reinforcement learning framework, significantly improved the field. However, traditional models often struggle to accurately capture the complexities in decision-making and frequently demonstrate inconsistencies between expected and actual behavior - a phenomenon known as \textbf{undermatching}. This study leverages \textbf{entropy-based method}, a \textbf{model-free} approach based on information theory, to address the problem in \textbf{feature-specific reinforcement learning} tasks in which the agent is unaware of the task-reward connections. Unlike previous methodologies that primarily assess general decision-making tendencies, this study applies an entropy-based approach to explore the dynamics of choice behaviors driven by specific features in controlled experimental settings with monkeys. Our findings suggest that this entropy-based method not only \textbf{explains} feature-specific choice behavior significantly better than previously existing methods but also \textbf{improves} the \textbf{predictive accuracy} of computational models of choice. This approach represents a significant advance in integrating behavioral insights into computational frameworks across various scientific and technological domains. It also deepens our understanding of feature-specific choice behaviors and their impact on decision dynamics. Finally, the study contributes to the broader field of behavioral economics by providing a more precise way to explain the decisions and bridge gaps between theoretical economics and practical, observable behaviors in controlled experiments.


## Project Structure


thesis/
│
├── helpers/
│ ├── code.py
│ ├── convert_all_to_json.m
│ ├── convert_all.m
│ ├── convert.m
│ └── eda.py
│
├── metrics/
│ ├── behavioral_metrics.py
│ ├── conditional_entropy.py
│ ├── entropy_metrics_efficient.py
│ ├── entropy_metrics.py
│ ├── entropy.py
│ ├── get_metrics.py
│ └── utils.py
│
├── plots/
│ ├── *.png
│
├── test_models/
│ ├── bilstm.py
│ ├── cnn.py
│ ├── gru.py
│ ├── lstm.py
│ └── stepwise_regression.py
│
├── utils/
│ ├── config.py
│ ├── merge_csv_to_one_dataset.py
│ ├── model_performance.py
│ └── train_preprocessing.py
│
└── visualisations/
├── 3d_surface_both_agents.py
├── 3d_surface.py
├── correlation_bar.py
└── correlation.py





## Dependencies
Python 3.8+
pandas
numpy
scikit-learn
keras
matplotlib
scipy