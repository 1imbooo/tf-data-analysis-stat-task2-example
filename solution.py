import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 661128504 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:

    def bootstrap_confidence_interval(data, confidence_level):
        num_bootstraps = 1000
        sample_size = len(data)
        bootstrapped_means = np.empty(num_bootstraps)

        for i in range(num_bootstraps):
            bootstrap_sample = np.random.choice(data, size=sample_size, replace=True)
            bootstrapped_means[i] = np.mean(bootstrap_sample)

        lower_quantile = (1 - confidence_level) / 2
        upper_quantile = 1 - lower_quantile
        lower_bound = np.quantile(bootstrapped_means, lower_quantile)
        upper_bound = np.quantile(bootstrapped_means, upper_quantile)
        
        return [lower_bound, upper_bound]

    
    def acceleration_confidence_interval(data, confidence_level):
        time = 59 # время измерения пути
        distance = data
        errors = np.random.exponential(1, size=len(distance)) - 0.5 # генерируем ошибки измерения пути
        measured_speeds = distance / time + errors # вычисляем измеренную скорость
        acceleration = np.diff(measured_speeds) / time # вычисляем ускорение
       
        return bootstrap_confidence_interval(acceleration, confidence_level)

    confidence_level = p
    distance = x 
    interval = acceleration_confidence_interval(distance, confidence_level)
    
    return interval[0], interval[1]
