def plot_fractions(data_plot):
  sns.set(style="whitegrid")
  plt.figure(figsize=(12, 6))
  plt.subplot(1, 2, 1)
  plt.scatter(data_plot.reward_fraction_run, data_plot.choice_fraction_run, alpha=0.5)
  plt.plot([0, 1], [0, 1], 'k--', linewidth=2)
  plt.xlabel('Reward fraction on left')
  plt.ylabel('Choice fraction on left')
  plt.xticks(rotation=45)

  plt.tight_layout()
  plt.show()
