Khả năng sử dụng chung một kiến trúc Pretrained Transformer (như BERT) cho cả hai bài toán hoàn toàn khác nhau về cấu trúc đầu ra là Sequence Classification (LAB 08) và Token Classification (LAB 09) chỉ bằng cách thay đổi lớp dự đoán cuối cùng (prediction head) xuất phát từ bản chất biểu diễn ngôn ngữ của cơ chế Self-Attention.   



Về mặt cấu trúc, đầu ra của một khối Pretrained Transformer Encoder đối với chuỗi đầu vào gồm $T$ tokens luôn là một ma trận biểu diễn ngữ cảnh (contextual representation) kích thước $H \\in \\mathbb{R}^{T \\times d}$, với $d$ là số chiều ẩn (ví dụ $d = 768$). Khác với các biểu diễn tĩnh truyền thống như Word2Vec (mỗi từ chỉ gắn với một vector cố định), mỗi hàng $h\_i \\in \\mathbb{R}^d$ trong ma trận $H$ tại tầng cuối cùng là kết quả tổng hợp thông tin hai chiều xuyên suốt toàn bộ câu thông qua nhiều lớp Multi-Head Self-Attention. Nhờ đó, bản thân ma trận $H$ đã chứa đựng đồng thời cả ngữ nghĩa tổng quát của toàn bộ chuỗi lẫn thông tin cú pháp, ngữ cảnh chi tiết của từng token riêng lẻ trong mối liên hệ với các từ xung quanh.   



Chính cấu trúc biểu diễn giàu thông tin và đối xứng này cho phép tầng prediction head phía trên hoạt động như một bộ giải mã chuyên biệt cho từng bài toán (task-specific head):   

* Nhánh Sequence Classification: Khi bài toán chỉ cần một nhãn duy nhất đại diện cho toàn bộ văn bản (như phân loại cảm xúc tích cực hay tiêu cực), mô hình trích xuất duy nhất vector tại vị trí token đặc biệt \[CLS] đứng đầu chuỗi ($h\_{\\text{\[CLS]}} \\in \\mathbb{R}^d$). Nhờ cơ chế tự chú ý toàn cục, \[CLS] đóng vai trò như điểm hội tụ thông tin từ mọi token trong câu, và một lớp tuyến tính đơn giản $W\_{\\text{seq}} \\in \\mathbb{R}^{d \\times C\_{\\text{seq}}}$ là đủ để ánh xạ vector này sang nhãn của cả chuỗi.   
* Nhánh Token Classification (NER): Khi bài toán yêu cầu gán nhãn chi tiết cho từng từ (như B-PER, I-PER, O), mô hình giữ lại toàn bộ chuỗi vector ngữ cảnh $(h\_1, h\_2, \\dots, h\_T)$ của mọi token và áp dụng chung một phép chiếu tuyến tính $W\_{\\text{tok}} \\in \\mathbb{R}^{d \\times C\_{\\text{tok}}}$ lên từng vector độc lập. Vì mỗi $h\_i$ đã tích hợp sẵn ngữ cảnh lân cận, bộ phân loại tại từng vị trí đủ cơ sở để phân định ranh giới thực thể và giải quyết tính đa nghĩa của từ.   

Tóm lại, mô hình Pretrain – Fine-tune tách biệt rõ ràng giữa bộ trích xuất đặc trưng ngôn ngữ tổng quát (Encoder) và tầng ánh xạ đầu ra đặc thù (Prediction Head), giúp tái sử dụng tri thức nền tảng khổng lồ cho đa dạng bài toán hạ nguồn một cách linh hoạt và hiệu quả.  

