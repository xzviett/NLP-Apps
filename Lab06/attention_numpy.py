import numpy as np

def softmax(x):
    """
    Hàm tính softmax trên trục cuối (hàng) của ma trận.
    Trừ đi giá trị max để chống tràn số (numerical stability).
    """
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / np.sum(e_x, axis=-1, keepdims=True)

def scaled_dot_product_attention(Q, K, V):
    """
    Hàm tính toán Scaled Dot-Product Attention bằng thuần NumPy.
    Input:
        Q: Ma trận Query có kích thước (seq_len_q, d_k)
        K: Ma trận Key có kích thước (seq_len_k, d_k)
        V: Ma trận Value có kích thước (seq_len_k, d_v)
    Output:
        S: Ma trận điểm số (scores) chưa qua softmax
        A: Ma trận trọng số (attention weights)
        C: Ma trận ngữ cảnh (context matrix)
    """
    d_k = K.shape[-1]
    S = np.dot(Q, K.T) / np.sqrt(d_k)
    A = softmax(S)
    C = np.dot(A, V)
    return S, A, C