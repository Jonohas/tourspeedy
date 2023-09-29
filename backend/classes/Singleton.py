
class Singleton(type):
    _instances = {}  # Dictionary to hold instance of the class
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # If instance is not created yet, create one and store it in _instances
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]  # Return the created instance
