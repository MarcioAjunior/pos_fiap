if __name__ == '__main__':
    import numpy as np
    time = np.arange(100)
    
    random = np.sin(time) + np.random.normal(size=time.size)
    