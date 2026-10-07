import numpy as np
import nltk

def build_vocabulary(corpus):
    """Xây dựng từ điển ánh xạ từ -> index và index -> từ"""
    vocab = set()
    for doc in corpus:
        tokens = nltk.word_tokenize(doc.lower())
        vocab.update(tokens)
        
    vocab = sorted(list(vocab))
    word2idx = {w: i for i, w in enumerate(vocab)}
    idx2word = {i: w for i, w in enumerate(vocab)}
    
    return word2idx, idx2word, len(vocab)

def build_cooccurrence_matrix(corpus, word2idx, window=2):
    """Xây dựng ma trận co-occurrence dựa trên context window"""
    V = len(word2idx)
    matrix = np.zeros((V, V))
    
    for doc in corpus:
        tokens = nltk.word_tokenize(doc.lower())
        length = len(tokens)
        
        for i, target_word in enumerate(tokens):
            if target_word not in word2idx:
                continue
            target_idx = word2idx[target_word]
            
            start = max(0, i - window)
            end = min(length, i + window + 1)
            
            for j in range(start, end):
                if i != j: 
                    context_word = tokens[j]
                    if context_word in word2idx:
                        context_idx = word2idx[context_word]
                        matrix[target_idx, context_idx] += 1
                        
    return matrix

def cosine_similarity(vec_a, vec_b):
    """Tính Cosine Similarity giữa 2 vector bằng công thức toán học"""
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
        
    return dot_product / (norm_a * norm_b)

def most_similar(word, matrix, word2idx, idx2word, top_k=5):
    if word not in word2idx:
        return f"Từ '{word}' không có trong từ điển."
        
    target_idx = word2idx[word]
    target_vec = matrix[target_idx]
    
    similarities = []
    for i in range(len(matrix)):
        if i != target_idx: 
            sim = cosine_similarity(target_vec, matrix[i])
            similarities.append((idx2word[i], sim))
            
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]
