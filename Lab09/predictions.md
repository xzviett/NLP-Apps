Prediction 1: Nếu sử dụng pretrained Transformer thay vì một classifier đơn giản dựa trên word features, NER

sẽ thay đổi như thế nào?

* Prediction: Hiệu suất NER của Pretrained Transformer sẽ vượt trội hoàn toàn so với các bộ phân loại truyền thống dựa trên đặc trưng từ đơn lẻ (như Bag-of-Words, TF-IDF).
* Reasons: Giải quyết tính đa nghĩa phụ thuộc ngữ cảnh (Contextual Disambiguation): Cùng một từ "Apple" nhưng trong "Apple released a new iPhone" là ORG, còn trong "I ate a red apple" là O. Bộ phân loại dựa trên word features tĩnh không thể phân biệt hai trường hợp này vì đặc trưng đầu vào của từ giống hệt nhau. 



Prediction 2: Các entity dài nhiều token sẽ dễ hay khó hơn entity chỉ có một token?

* Prediction: Các thực thể dài gồm nhiều token (ví dụ: "United Nations Security Council") sẽ khó dự đoán chính xác hơn so với thực thể chỉ có 1 token (ví dụ: "Microsoft").
* Reasons:

  * Trong đánh giá NER chuẩn (entity-level metrics), một thực thể nhiều từ chỉ được tính là đúng (True Positive) khi mô hình dự đoán đúng đồng thời tất cả các nhãn từ đầu đến cuối (B-ORG, I-ORG, I-ORG, I-ORG). Chỉ cần sai một token ở giữa (nhầm I-ORG thành O) hoặc ngắt nhầm ranh giới ở cuối, toàn bộ thực thể đó bị tính là sai hoàn toàn.
  * Sự nhập nhằng của từ nối bên trong: Các thực thể dài thường chứa giới từ hoặc từ phổ thông viết thường ở giữa (ví dụ: "of", "and", "the" trong "Bank of America"). Mô hình rất dễ bị nhầm lẫn và gán nhãn O cho các từ nối này, làm đứt gãy thực thể thành hai mảnh rời rạc.



Prediction 3: Entity hiếm xuất hiện trong training data có khả năng gây lỗi nhiều hơn không?

* Prediction: Có, các thực thể hiếm xuất hiện trong tập dữ liệu huấn luyện sẽ gây ra tỷ lệ lỗi (False Negatives) cao hơn rõ rệt.
* Reasons: 

  * Thiếu hụt cập nhật Gradient trong quá trình Fine-tuning: Những thực thể xuất hiện dày đặc (như "New York", "U.S.", "Clinton") được cập nhật trọng số liên tục qua hàng trăm batch, giúp mô hình ghi nhớ cả đặc trưng từ vựng lẫn ngữ cảnh. Ngược lại, thực thể hiếm chỉ xuất hiện 1–2 lần (hoặc bằng 0) không đủ tín hiệu gradient để điều chỉnh biểu diễn riêng biệt.
  * Các tên riêng hiếm, tên nước ngoài hoặc thuật ngữ đặc thù thường không có nguyên vẹn trong từ điển của Tokenizer (WordPiece/BPE) nên bị chẻ thành nhiều mảnh subword vô nghĩa (ví dụ: "Kyrgyzstan" bị tách thành \['ky', '##rg', '##yz', '##stan']). Việc bị phân mảnh làm suy yếu tín hiệu ngữ nghĩa gốc của từ.



