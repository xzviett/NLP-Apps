import nltk
from collections import Counter
import math

class NGramLanguageModel:
    def __init__(self, n):
        self.n = n
        self.vocab = set()
        self.ngram_counts = Counter()    
        self.context_counts = Counter()  
        self.vocab_size = 0
        self.total_tokens = 0          
        
    def fit(self, corpus):
        """Tương đương với build_vocabulary(), count_ngrams(), và train_ngram()"""
        print(f"Đang huấn luyện {self.n}-gram model...")
        for doc in corpus:
            sentences = nltk.sent_tokenize(doc.lower())
            for sent in sentences:
                tokens = nltk.word_tokenize(sent)
                
                self.vocab.update(tokens)
                self.total_tokens += len(tokens)
                
                # Thêm padding (token bắt đầu và kết thúc câu)
                # Ví dụ Bigram: ['<s>', 'the', 'cat', '</s>']
                # Ví dụ Trigram: ['<s>', '<s>', 'the', 'cat', '</s>']
                if self.n > 1:
                    padded_tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
                else:
                    padded_tokens = tokens + ['</s>']
                    self.total_tokens += 1 
                
                self.vocab.update(['<s>', '</s>'])
                
                # Trích xuất và đếm n-grams cùng context
                for i in range(len(padded_tokens) - self.n + 1):
                    # Trích xuất tuple n-gram hiện tại
                    ngram = tuple(padded_tokens[i : i + self.n])
                    self.ngram_counts[ngram] += 1
                    
                    # Trích xuất tuple context (n-1 từ trước đó)
                    if self.n > 1:
                        context = tuple(padded_tokens[i : i + self.n - 1])
                        self.context_counts[context] += 1
                        
        self.vocab_size = len(self.vocab)
        print(f"Huấn luyện xong! Vocabulary size: {self.vocab_size}")

    def _preprocess_context(self, context):
        """Hàm phụ trợ: Xử lý context đầu vào (lowercase, tokenize chuẩn, và cắt đúng độ dài N-1)"""
        if isinstance(context, str):
            context = tuple(nltk.word_tokenize(context.lower()))
        elif isinstance(context, list):
            context = tuple(context)
            
        if self.n > 1:
            if len(context) >= self.n - 1:
                context = context[-(self.n - 1):]
            else:
                context = tuple(['<s>'] * (self.n - 1 - len(context))) + context
        else:
            context = () 
            
        return context

    def probability(self, context, word):
        """Tính P(word | context) bằng Maximum Likelihood Estimation (MLE)"""
        context = self._preprocess_context(context)
        ngram = context + (word,) if self.n > 1 else (word,)
        
        if self.n == 1:
            return self.ngram_counts.get(ngram, 0) / self.total_tokens if self.total_tokens > 0 else 0.0
        else:
            ctx_count = self.context_counts.get(context, 0)
            if ctx_count == 0:
                return 0.0 
            return self.ngram_counts.get(ngram, 0) / ctx_count

    def sentence_probability(self, sentence):
        """Tính xác suất P(S) của cả câu bằng Chain Rule"""
        tokens = nltk.word_tokenize(sentence.lower())
        
        if self.n > 1:
            padded_tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
        else:
            padded_tokens = tokens + ['</s>']
            
        prob = 1.0
        for i in range(len(padded_tokens) - self.n + 1):
            word = padded_tokens[i + self.n - 1]
            context = tuple(padded_tokens[i : i + self.n - 1])
            
            p = self.probability(context, word)
            prob *= p
            
        return prob

    def next_word_distribution(self, context):
        """Trả về top các từ có khả năng xuất hiện cao nhất dựa trên context"""
        context = self._preprocess_context(context)
        dist = {}
        
        for word in self.vocab:
            if word == '<s>': continue 
            
            # MẸO NHỎ ĐỂ BÁO CÁO ĐẸP HƠN: 
            # Bỏ qua các dấu câu (., ?, !) vì trên thực tế dấu câu luôn có xác suất cao nhất
            if not word.isalpha(): continue 
            
            p = self.probability(context, word)
            if p > 0:
                dist[word] = p
                
        return dict(sorted(dist.items(), key=lambda item: item[1], reverse=True))

    def sentence_log_probability(self, sentence):
        """Tính log xác suất của câu bằng cách cộng các log probability"""
        tokens = nltk.word_tokenize(sentence.lower())
        
        if self.n > 1:
            padded_tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
        else:
            padded_tokens = tokens + ['</s>']
            
        log_prob = 0.0
        for i in range(len(padded_tokens) - self.n + 1):
            word = padded_tokens[i + self.n - 1]
            context = tuple(padded_tokens[i : i + self.n - 1])
            
            p = self.probability(context, word)
            
            if p == 0:
                return float('-inf') 
            
            log_prob += math.log(p)
            
        return log_prob

    def laplace_probability(self, context, word):
        """Tính P(word | context) sử dụng Add-one / Laplace Smoothing"""
        context = self._preprocess_context(context)
        ngram = context + (word,) if self.n > 1 else (word,)
        
        if self.n == 1:
            return (self.ngram_counts.get(ngram, 0) + 1) / (self.total_tokens + self.vocab_size)
        else:
            ctx_count = self.context_counts.get(context, 0)
            return (self.ngram_counts.get(ngram, 0) + 1) / (ctx_count + self.vocab_size)

    def corpus_perplexity(self, eval_corpus, smoothing=False):
        """Tính Perplexity của model trên một tập corpus (Train/Valid/Test)"""
        log_prob_sum = 0.0
        N = 0 
        
        for doc in eval_corpus:
            # FIX LỖI: Bắt buộc phải sent_tokenize để không tạo n-gram ảo nối giữa 2 câu
            sentences = nltk.sent_tokenize(doc.lower()) 
            for sent in sentences:
                tokens = nltk.word_tokenize(sent)
                if self.n > 1:
                    padded_tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
                else:
                    padded_tokens = tokens + ['</s>']
                    
                for i in range(len(padded_tokens) - self.n + 1):
                    word = padded_tokens[i + self.n - 1]
                    ctx = tuple(padded_tokens[i : i + self.n - 1])
                    
                    p = self.laplace_probability(ctx, word) if smoothing else self.probability(ctx, word)
                    
                    if p == 0:
                        return float('inf')
                    
                    log_prob_sum += math.log(p)
                    N += 1
                    
        if N == 0: return float('inf')
        return math.exp(-log_prob_sum / N)