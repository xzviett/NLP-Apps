Prediction 1

Khi chuyển: unigram → bigram → trigram vocabulary có tăng không?



Prediction: Kích thước Vocabulary không tăng.

Reason: Vocabulary là tập từ đơn (unigram) duy nhất tạo nên corpus nên dù có chuyển sang bigram hay trigram thì vocabulary đều không thay đổi.

Confidence: Cao



Prediction 2

Số lượng n-gram sẽ thay đổi như thế nào?



Prediction: Tổng số n-gram đếm được giảm dần (N -> N-1 -> N-2), unique n-gram tăng lên.

Reason: Do câu càng dài thì tỉ lệ trùng lặp giữa các trigram càng nhỏ (nhỏ hơn bigram) -> số lượng trigram lớn hơn.

Confidence: Cao.



Prediction 3

Mô hình nào có khả năng gặp zero probability nhiều hơn?



Prediction: Trigram.

Reason: Context càng dài, xác suất để xuất hiện 3 từ đi liền nhau theo đúng thứ tự thấp.

Confidence: Cao.



Prediction 4

Mô hình nào dự kiến có perplexity thấp hơn trên training set?



Prediction: Mô hình Trigram sẽ có perplexity thấp nhất.

Reason: 

Confidence: Thấp.



Prediction 5

Nếu corpus rất nhỏ, trigram có chắc chắn tốt hơn bigram không?



Prediction: Không.

Reason: Corpus nhỏ không thể cung cấp đủ tần suất thống kê cho các chuỗi 3 từ -> Overfitting.

Confidence: Trung bình

