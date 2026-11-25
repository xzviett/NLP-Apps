Prediction 1: Nếu question và context chứa nhiều từ giống nhau nhưng chỉ một vị trí thực sự trả lời câu hỏi,

model có dễ bị nhầm không?

* Prediction: Có, mô hình rất dễ bị nhầm lẫn (đặc biệt ở giai đoạn đầu huấn luyện hoặc khi các câu gây nhiễu có cấu trúc ngữ pháp gần giống câu hỏi), dẫn đến việc trích xuất nhầm đáp án nằm ở câu sai.
* Reason: Thiên lệch khớp từ khóa bề mặt: Trong cơ chế Cross-Attention giữa Question và Context, các token giống hệt nhau về mặt chữ (ví dụ cùng nhắc tới tên một nhân vật, địa danh hoặc năm) tạo ra điểm số attention ($Q \\cdot K^T$) rất cao một cách tự nhiên.Suy luận ngữ nghĩa sâu vs. Bẫy từ vựng: Nếu một câu gây nhiễu trong Context chứa tới 80% từ vựng trùng với Question nhưng mang ý phủ định, khác thời điểm hoặc khác chủ thể hành động, mô hình chưa được fine-tune kỹ sẽ bị "hút" về vùng có mật độ trùng lặp từ vựng cao nhất thay vì thực sự hiểu mối quan hệ cú pháp – ngữ nghĩa để chọn đúng vị trí trả lời.



Prediction 2: Answer span càng dài thì boundary prediction có khó hơn không?

* Prediction: Có, answer span càng dài thì việc dự đoán chính xác ranh giới (start và end) càng khó hơn rõ rệt.
* Reason: Tính độc lập của hai đầu dự đoán ($P\_{\\text{start}}$ và $P\_{\\text{end}}$): mô hình dự đoán xác suất điểm đầu $i$ và điểm cuối $j$ qua hai bộ phân loại tuyến tính tách biệt mà không có cơ chế ràng buộc cấu trúc cú pháp trực tiếp giữa chúng.Sự mơ hồ của ranh giới mở rộng: Với đáp án ngắn 1–2 từ (như năm "1998" hoặc tên người "Albert Einstein"), điểm bắt đầu và kết thúc được định vị rõ ràng bởi thực thể. Ngược lại, với đáp án dài (một cụm giới từ, một định nghĩa hoặc cả mệnh đề), mô hình rất dễ bị lệch 1–2 từ ở biên — ví dụ bao gồm thừa mạo từ ("the"), giới từ ("in", "by"), dấu câu ở cuối, hoặc ngắt cụt giữa chừng một mệnh đề phụ, làm giảm mạnh tỷ lệ khớp tuyệt đối.



Prediction 3: Nếu context chứa nhiều thông tin không liên quan performance sẽ thay đổi như thế nào?

* Prediction: Hiệu suất (cả Exact Match và F1) sẽ suy giảm đáng kể khi đoạn Context chứa nhiều thông tin dư thừa và đặc biệt là các câu gây nhiễu.
* Reason: Nhiễu loạn phân phối Softmax: Hàm Softmax cho $P\_{\\text{start}}$ và $P\_{\\text{end}}$ chuẩn hóa xác suất trên toàn bộ $L$ tokens của chuỗi đầu vào. Khi Context dài ra và chứa nhiều đoạn văn không liên quan, tổng mẫu số $\\sum\_{k=1}^L e^{z\_k}$ tăng lên, làm phân tán trọng số Self-Attention và làm giảm độ tự tin (xác suất đỉnh) tại vị trí đáp án thật.



Prediction 4: Nếu chỉ thay đổi thứ tự một số câu trong context nhưng giữ nguyên answer, model có bị ảnh hưởng

không?

* Prediction: Hiệu suất tổng thể sẽ tương đối ổn định (chỉ biến động nhẹ) nhờ cơ chế Self-Attention bất biến hoán vị kết hợp Positional Embeddings, tuy nhiên vẫn có thể bị ảnh hưởng nhẹ nếu câu chứa đáp án bị đẩy xuống quá sâu ở cuối đoạn văn dài hoặc bị tách rời khỏi câu chứa thông tin tiền đề (đại từ thay thế).
* Reason: Tính chất của Transformer Encoder: Khác với mạng hồi quy RNN/LSTM xử lý tuần tự từ trái sang phải (rất nhạy cảm với vị trí đầu/cuối chuỗi), cơ chế Self-Attention của BERT cho phép mọi token trong Question tương tác trực tiếp với mọi token trong Context với khoảng cách bước nhảy bằng $1$, bất kể câu chứa đáp án nằm ở đầu hay giữa đoạn văn.

