# A-Trading-Strategy-Using-Bollinger-bands---keltner-squeeze-with-SAR-
## Article of this project is on the Medium
[https://medium.com/@eric07310115/使用-bollinger-bands-keltner-squeeze- 配合-sar-指標的順勢交易策略-4c6ffab5b64c](https://medium.com/@eric07310115/%E4%BD%BF%E7%94%A8-bollinger-bands-keltner-squeeze-%E9%85%8D%E5%90%88-sar-%E6%8C%87%E6%A8%99%E7%9A%84%E9%A0%86%E5%8B%A2%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-4c6ffab5b64c)

## brief description to the code
data.py : to get the history information using TWstock API

BB_keltner_squeezer_with_sar.ipynb : construct trading strategy and do the backtesting to evaluate the performance of individual stock

BB_keltner_squeezer_with_kdj.ipynb : another trading strategy but the performance is worse, so I did not mention it on the article

test_hyperparameter_strategy1.ipynb : Using the HiPlot and Optuna python packages to conduct trials on a BB_keltner_squeezer_with_sar trading strategy and search for parameter plateaus.

test_hyperparameter_strategy2.ipynb : Using the HiPlot and Optuna python packages to conduct trials on a BB_keltner_squeezer_with_kdj trading strategy and search for parameter plateaus.
