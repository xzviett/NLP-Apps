Prediction 1: Một pretrained Transformer fine-tuned trên IMDb có khả năng đạt kết quả tốt hơn Transformer

nhỏ được train from scratch trên cùng dữ liệu không?

* Prediction: Có.
* Reason: Một Transformer train from scratch khi bắt đầu nhận dữ liệu IMDb thì mọi ma trận trọng số đều là các con số vô nghĩa. Nó phải tự học lại từ đầu cả cấu trúc ngữ pháp (cú pháp, từ loại) lẫn ngữ nghĩa cảm xúc, trong khi tập dữ liệu IMDb quá nhỏ bé so với sự phức tạp của ngôn ngữ. Ngược lại, Pretrained Transformer đã trải qua rất nhiều thời gian huấn luyện trên kho ngữ liệu khổng lồ. Nó đã học được language representation tổng quát và sâu sắc. Quá trình Fine-tuning chỉ đơn thuần là việc bẻ lái sự hiểu biết sẵn có đó để tập trung vào sắc thái cảm xúc, giúp nó tránh được overfitting và dễ dàng nhận diện các cấu trúc cảm xúc phức tạp (phủ định, tương phản).
* Expected evidence: Khi chạy thực nghiệm, Accuracy và F1 của Pretrained Model trên tập Test sẽ cao hơn mô hình tự code ở LAB 07. Đồng thời, hàm Loss của nó sẽ hội tụ nhanh hơn nhiều.



Prediction 2: Nếu freeze toàn bộ pretrained encoder và chỉ train classification head:

BERT encoder

↓ frozen

classification head

↓ train

prediction

* Prediction: C. Kém hơn.
* Reason: Việc đóng băng Encoder và chỉ cập nhật trọng số của lớp Linear cuối cùng được gọi là Feature Extraction. Tuy nhiên, đặc trưng ngôn ngữ mà BERT học được ở giai đoạn pretraining mang tính chất chung (General domain). Nó thiếu sự nhạy bén đặc thù đối với cách dùng từ lóng, châm biếm, hoặc ngữ cảnh chuyên biệt của mảng điện ảnh (IMDb). Khi thực hiện Full Fine-tuning (cập nhật cả Encoder), mọi lớp Attention của BERT sẽ được "mài giũa" và tái căn chỉnh để thích nghi hoàn hảo với domain mới, từ đó khai thác trọn vẹn sức mạnh của mô hình và cho ra kết quả tốt hơn hẳn so với việc chỉ train lớp phân loại ở cuối.



Prediction 3

Nếu chỉ có 10% training data:

100%

50%

25%

10%

pretrained model hay model train from scratch sẽ giảm performance mạnh hơn?

* Prediction: Model train from scratch sẽ giảm performance mạnh hơn.
* Reason: Cơ sở toán học của Deep Learning yêu cầu số lượng điểm dữ liệu phải đủ lớn để tối ưu hóa một mô hình có hàng triệu tham số. Khi bị cắt giảm xuống chỉ còn 10% dữ liệu, mô hình train from scratch sẽ lập tức rơi vào trạng thái Overfitting nặng nề: nó chỉ ghi nhớ vẹt các mẫu trong tập Train nhỏ bé mà hoàn toàn mất đi khả năng tổng quát hóa trên tập Test. Ngược lại, lợi thế lớn nhất của Pretraining chính là Transfer Learning. Trọng số của pretrained model đã chứa sẵn tri thức ngôn ngữ, nó chỉ cần một lượng dữ liệu cực nhỏ để gợi nhớ và điều chỉnh trọng số về đúng định hướng của bài toán. Do đó, dù chỉ còn 10% dữ liệu, pretrained model vẫn sẽ duy trì được hiệu suất ổn định và vượt trội hoàn toàn so với mô hình xây từ con số không.

