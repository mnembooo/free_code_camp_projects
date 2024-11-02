import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
        
    data = np.reshape(np.array(numbers), (3, 3))
    calculations = {}
    
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    
    for name, func in operations.items():
        calculations[name] = [
            func(data, axis=0).tolist(),
            func(data, axis=1).tolist(),
            func(data.flatten()).tolist()
        ]
    
    return calculations
