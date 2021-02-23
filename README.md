# Deep Reinforcement Learning for Automated Stock Trading Ensemble Strategy ICAIF 2020_practice-Notebook

This is the practice copy of the original version of the [Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020](https://github.com/AI4Finance-LLC/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020), including the data on which the stratergy is deployed

## Implementation
The whole stratergies are implemented in a single set of notebook file with the outputs

I have re implemented the similar model using the [sample_baseline3](https://stable-baselines3.readthedocs.io/en/master/guide/install.html) (can be downloaded from here) instead of sample_baselines on MS visual studio using latest updated TensorFlow 2.0>
### Installation
Install it using following set of codes
```bash
pip install stable_baselines3
```
**Note** This library currently will not be able to directly use GAIL and other algorithms mentioned in the paper. For that case it will be better to use the [stable_baseline](https://github.com/hill-a/stable-baselines) also the TensorFlow 2.0 is not supportable and the library might not be suitbale to use for Notebook.

Also another important required library is [gym](https://gym.openai.com/docs/#installation) and [stockstats](https://libraries.io/pypi/stockstats)
using
```bash
pip install stockstats
pip install gym
```

