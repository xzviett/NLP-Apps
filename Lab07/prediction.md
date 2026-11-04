Prediction 1: Một Transformer có thể xử lý các token trong sequence song song hơn RNN không?

* Prediction: Có.
* Reason: Transformer xử lý toàn bộ sequence trong một bước thông qua các phép nhân ma trận. Việc tính Q, K, V và Attention Scores diễn ra đồng thời cho tất cả các token.
* Confidence: Cao



Prediction 2: Nếu bỏ positional encoding, Transformer có còn biết thứ tự token không?

* Prediction: Không.
* Reason: Phép tính Self-Attention bản chất là một phép toán trên tập hợp. Nó tính độ tương đồng giữa các vector mà không hề có định niệm về khoảng cách hay vị trí. 
* Confidence: Cao



Prediction 3: Nếu hai câu có cùng tập token nhưng khác thứ tự, Transformer không có positional information có thể phân biệt chúng không?



* Prediction: Không thể phân biệt.
* Reason: Lấy ví dụ hai câu "dog bites man" và "man bites dog". Nếu không có Positional Encoding, tập hợp vector đầu vào là giống hệt nhau. Cơ chế Self-Attention sẽ sinh ra các trọng số Attention tương tự nhau (chỉ khác vị trí hàng/cột), và khi đi qua bước tổng hợp Global Pooling, biểu diễn cuối cùng của hai câu sẽ hoàn toàn giống nhau, khiến mô hình nhầm lẫn.
* Confidence: Cao



Prediction 4: Hai attention heads có nhất thiết học cùng một attention pattern không?

* Prediction: Không nhất thiết.
* Reason: Mỗi head sở hữu một bộ ma trận trọng số W^Q, W^K, W^V được khởi tạo ngẫu nhiên. Trong quá trình học (Backpropagation), gradient descent sẽ tối ưu hóa để các heads bóc tách các đặc trưng khác nhau nhằm giảm tối đa hàm Loss. Có head sẽ chuyên bắt quan hệ ngữ pháp, có head chuyên bắt quan hệ ngữ nghĩa.
* Confidence: Trung bình



Prediction 5: Tăng số attention heads có chắc chắn làm accuracy tăng không?

* Prediction: Không chắc chắn.
* Reason: Mặc dù nhiều heads giúp học được nhiều khía cạnh hơn, nhưng nếu tăng quá mức, mô hình có thể bị Overfitting trên dữ liệu huấn luyện, và dư thừa khi nhiều heads học cùng một pattern vô nghĩa.
* Confidence: Cao



Prediction 6: Transformer có luôn nhanh hơn RNN trên mọi sequence length không?

* Prediction: Không. Trên các sequence cực kỳ dài, Transformer sẽ chậm hơn rất nhiều.
* Reason: Độ phức tạp tính toán của RNN đối với chiều dài chuỗi T là O(T) (tuyến tính). Trong khi đó, ma trận Self-Attention của Transformer đòi hỏi mọi token phải tính phép nhân ma trận với mọi token khác, dẫn đến độ phức tạp là O(T^2). Khi sequence length T quá lớn, chi phí T^2 sẽ trở thành nút thắt cổ chai làm tràn bộ nhớ và tăng thời gian tính toán.
* Confidence: Cao.











