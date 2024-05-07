import random
import torch


def generate_random_list(shape):
    """
    Generate a list with random numbers and shape 'shape'
    """
    if len(shape) == 0:
        return []
    else:
        inner_shape = shape[1:]
        if len(inner_shape) == 0:
            return [random.uniform(-1, 1) for _ in range(shape[0])]
        else:
            return [generate_random_list(inner_shape) for _ in range(shape[0])]
        

def to_torch(custom_tensor):
    shape = custom_tensor.shape
    pytorch_tensor = torch.zeros(shape)
    
    def _iterate_indices(shape):
        if len(shape) == 0:
            yield ()
        else:
            for index in range(shape[0]):
                for sub_indices in _iterate_indices(shape[1:]):
                    yield (index,) + sub_indices
    
    # Iterate over all elements using the custom tensor's __getitem__ method
    for indices in _iterate_indices(shape):
        value = custom_tensor[indices]
        pytorch_tensor[tuple(indices)] = value
    
    return pytorch_tensor

def compare_torch(tensor1, tensor2, epsilon=1e-5):
    diff = torch.abs(tensor1 - tensor2)    
    return torch.all(diff < epsilon)