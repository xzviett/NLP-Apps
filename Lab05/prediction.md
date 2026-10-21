Prediction 1: Giữa TF-IDF + Logistic Regression và RNN + Embedding, model nào xử lý word order trực tiếp hơn?

* Prediction: RNN + Embedding.
* Reason: TF-IDF hoạt động theo cơ chế Bag-of-Words, biến văn bản thành tập hợp tần suất từ vựng và triệt tiêu hoàn toàn thứ tự từ. Ngược lại, RNN + Embedding đưa từng vector từ vào mô hình một cách tuần tự theo đúng dòng thời gian. Hidden state h\_t luôn được tính dựa trên h\_t-1, giúp mô hình mã hóa trực tiếp cấu trúc cú pháp và trật tự từ vào bộ nhớ.
* Confidence: Ca0.



Prediction 2: Giữa RNN và LSTM, model nào xử lý dependency dài tốt hơn?

* Prediction: LSTM.
* Reason: RNN cơ bản bị kẹt ở bài toán Vanishing Gradient vì các phép nhân ma trận liên tiếp khi truyền ngược qua thời gian. LSTM giải quyết triệt để điểm mù này bằng cách thiết kế thêm một luồng thông tin song song gọi là Cell State C\_t cùng hệ thống các cổng gates. Forget Gate và Input Gate cho phép LSTM cộng/trừ thông tin thay vì nhân liên tiếp, tạo ra một gradient superhighway cho đạo hàm truyền ngược đi rất xa mà không bị suy biến.
* Confidence: Cao.



Prediction 3: Nếu sequence length tăng từ 50 → 200, training của RNN sẽ thay đổi như thế nào?

* Prediction: Thời gian huấn luyện tăng và mô hình khó hội tụ hơn.
* Reason: Việc tăng chiều dài chuỗi lên gấp 4 lần buộc RNN phải unroll thêm hàng loạt bước thời gian. Điều này không chỉ tiêu tốn nhiều RAM và thời gian tính toán hơn, mà còn khiến hiện tượng Vanishing Gradient trở nên trầm trọng. Mạng sẽ gần như mất hoàn toàn khả năng cập nhật trọng số cho các từ ở đầu chuỗi khi nhận tín hiệu lỗi.
* Confidence: Cao.



Prediction 4: Nếu truncate toàn bộ review về 30 tokens, thông tin classification có thể bị ảnh hưởng không?

* Prediction: Có, độ chính xác có thể sẽ suy giảm mạnh.
* Reason: Ví dụ trong các bài review phim, thông thường các câu đầu tiên thường chỉ là lời dạo đầu hoặc tóm tắt bối cảnh (ví dụ: "Tôi đi xem phim này vào cuối tuần cùng bạn..."). Phần phía sau mới mang cảm xúc quyết định (ví dụ: "nhưng đây là một thảm họa, kịch bản quá tệ") thường nằm ở giữa hoặc cuối bài review. Việc truncate sẽ bỏ lỡ các keywords này.
* Confidence: Trung bình.



Prediction 5: LSTM có chắc chắn cho accuracy cao hơn RNN trên mọi dataset không?

* Prediction: Không.
* Reason: Trên các tập dữ liệu mà văn bản cực kỳ ngắn (như SMS, Zalo, Messenger) hoặc tính chất quá đơn giản, RNN cơ bản hoàn toàn có khả năng học được mà không bị Vanishing Gradient. Hơn nữa, vì LSTM có số lượng tham số cao gấp nhiều lần RNN, nó có rủi ro bị Overfitting nhanh hơn và chạy chậm hơn trên các tập dữ liệu này.
* Confidence: Trung bình.





