Câu 1:  Nếu tăng (n), mô hình nhận thêm thông tin gì?

Khi tăng n, mô hình có thêm ngữ cảnh dài hơn -> nắm được quy luật ngữ pháp và sự phụ thuộc giữa các từ.



Câu 2: Tại sao tăng (n) lại làm sparsity tăng?

Không gian trạng thái tăng theo cấp số nhân -> hầu hết các n-gram có tần suất là 0 -> sparse



Câu 3: Tại sao smoothing cần thiết?

Để giải quyết vấn đề zero probability.



Câu 4: Perplexity đo điều gì?

Perplexity đo mức độ bối rối của mô hình trước một đoạn văn bản. Perplexity càng thấp, mô hình càng tự tin, nghĩa là nó gán xác suất càng cao cho chuỗi từ đang được đánh giá.



Câu 5: Một model có perplexity thấp hơn có luôn tạo ra văn bản tốt hơn đối với con người không? Giải thích.

Không luôn luôn. Một mô hình có Perplexity rất thấp có thể là do bị Overfitting.



Câu 6: N-gram language model thất bại ở đâu khi so với cách con người hiểu ngôn ngữ?

Thiếu khả năng khái quát hóa ngữ nghĩa, ó coi các từ là các ký hiệu độc lập rời rạc.



Câu 7: Nếu context dài 100 từ, trigram có sử dụng được thông tin của 97 từ đầu không?

Hoàn toàn không.



