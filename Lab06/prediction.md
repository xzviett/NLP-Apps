Prediction 1: Nếu một key có dot product lớn hơn các key khác, attention weight của nó sẽ như thế nào?

* Prediction: Nó sẽ chiếm một attention weight (trọng số) lớn hơn đáng kể so với các key khác.
* Reason: Dot product là thước đo độ tương đồng giữa vector. Điểm cao nhất chứng tỏ Key đó khớp với Query nhất. Khi đi qua hàm mũ e^x của Softmax, sự chênh lệch này bị khuếch đại lớn, sinh ra trọng số lớn nhất.
* Confidence: Cao



Prediction 2: Nếu tất cả scores giống nhau s = \[1, 1, 1, 1], attention weights sẽ như thế nào?

* Prediction: Mọi token sẽ nhận được attention weight bằng nhau và bằng chính xác 1/N (ở đây là 1/4).
* Reason: Khi tất cả các score bằng nhau, tử số của hàm Softmax của mọi phần tử đều bằng nhau. Mẫu số là tổng của 4 phần tử giống hệt nhau. Khi không có thông tin nào nổi bật, Attention trở thành phép lấy trung bình cộng giống hệ Average Word2Vec.
* Confidence: Cao



Prediction 3: Nếu một score lớn hơn rất nhiều (s = \[1, 1, 10]), attention sẽ tập trung như thế nào?

* Prediction: Gần như 100% trọng số sẽ dồn hết vào phần tử có score 10, trong khi các phần tử kia bị triệt tiêu gần về 0.
* Reason: Đây là hệ quả của hàm số mũ e^x. Tử số của phần tử thứ ba là e^10, trong khi hai tử số đầu chỉ là e^1. Mẫu số sum = 2.71 + 2.71 + 22,026 = 22,031. Do đó alpha\_3 = 22.026 / 22.031 = 0.9997. Mô hình sẽ chỉ nhìn duy nhất vào token này và lấy giá trị Value của nó làm Context vector.
* Confidence: Cao



Prediction 4: Nếu sequence tăng từ 10 tokens -> 1000 tokens, chi phí tính attention sẽ thay đổi như thế nào?

* Prediction: Chi phí tính toán sẽ tăng theo cấp số nhân (gấp 10,000 lần), vì độ phức tạp của Self-Attention là O(N^2).
* Reason: Trong cơ chế Attention đầy đủ, mỗi query phải tính dot-product với tất cả các keys (N tokens). Do đó, có N query thì cần tính NxN = N^2 phép toán. Tăng N từ 10 lên 1000 (tăng 100 lần), chi phí sẽ tăng 100^2 = 10,000 lần. 
* Confidence: Cao



Prediction 5: Attention có luôn chọn đúng token mà con người cho là quan trọng nhất không?

* Prediction: Không.
* Reason: Attention không hiểu ngữ nghĩa giống con người, nó chỉ chạy tối ưu hóa gradient (loss function) dựa trên tập huấn luyện. Nếu dữ liệu nhiễu, trọng số Attention sẽ không trùng khớp với logic giải thích của con người.
* Confidence: Trung bình











