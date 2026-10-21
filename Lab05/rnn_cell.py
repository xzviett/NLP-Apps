import numpy as np
import torch
import torch.nn as nn

input_size = 3
hidden_size = 2

torch.manual_seed(42)
pytorch_cell = nn.RNNCell(input_size, hidden_size)

W_xh = pytorch_cell.weight_ih.detach().numpy()
W_hh = pytorch_cell.weight_hh.detach().numpy()
b_h = (pytorch_cell.bias_ih + pytorch_cell.bias_hh).detach().numpy().reshape(-1, 1)

class SimpleRNNCell:
    def __init__(self, W_xh, W_hh, b_h):
        self.W_xh = W_xh
        self.W_hh = W_hh
        self.b_h = b_h

    def forward(self, x_t, h_prev):
        a_t = np.dot(self.W_xh, x_t) + np.dot(self.W_hh, h_prev) + self.b_h
        h_t = np.tanh(a_t)
        return h_t

x_t = np.array([[0.5], [1.0], [-0.2]])   
h_prev = np.array([[0.1], [-0.1]])       

my_cell = SimpleRNNCell(W_xh, W_hh, b_h)
my_h_t = my_cell.forward(x_t, h_prev)

pt_x_t = torch.tensor([[0.5, 1.0, -0.2]])
pt_h_prev = torch.tensor([[0.1, -0.1]])
pt_h_t = pytorch_cell(pt_x_t, pt_h_prev)

print("=== KẾT QUẢ TỪ SIMPLERNNCELL ===")
print(my_h_t.flatten())
print("\n=== KẾT QUẢ TỪ PYTORCH RNNCELL ===")
print(pt_h_t.detach().numpy().flatten())