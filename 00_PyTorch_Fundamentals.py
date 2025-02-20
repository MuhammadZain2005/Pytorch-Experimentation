# Resource Notebook: https://www.learnpytorch.io/00_pytorch_fundamentals/
import torch
import numpy

# Introduction to Tensors - way to represent multi-dimensional data

# Scalar
scalar = torch.tensor(7)
print(scalar)
print(scalar.item()) # Get tensor back as Python int
print(scalar.ndim) # Checking dimensions

# Vector 
vector = torch.tensor([7,7])
print(vector)
print(vector.ndim) # Dimensions (number of square brackets)
print(vector.shape) # Number of elements

# Matrix
MATRIX = torch.tensor([[7, 8],[9, 8]])
print(MATRIX)
print(MATRIX.ndim)
print(MATRIX.shape)

## TENSOR
TENSOR = torch.tensor([[[1,2,3],[3,6,9],[2,4,5]]])
print(TENSOR)