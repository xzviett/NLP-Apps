Qua chuỗi bài thực hành LAB 08, LAB 09 và LAB 10, cùng một kiến trúc nền tảng là Pretrained Transformer Encoder (như BERT) được tái sử dụng làm bộ trích xuất đặc trưng ngữ cảnh hóa (contextualized feature extractor), nhưng cách tổ chức dữ liệu đầu vào, khai thác biểu diễn đầu ra (hidden states) và thiết kế tầng dự đoán (task-specific head) đã tiến hóa qua ba cấp độ chi tiết hoàn toàn khác nhau:



Ở LAB 08 (Sequence Classification — Phân loại văn bản), mục tiêu là gán một nhãn duy nhất cho toàn bộ chuỗi đầu vào (như phân tích cảm xúc hoặc phân loại chủ đề). Mô hình nén thông tin ngữ nghĩa của cả câu thông qua cơ chế Self-Attention vào duy nhất vector đại diện của token đặc biệt \[CLS] ($h\_{\\text{\[CLS]}} \\in \\mathbb{R}^d$), sau đó đưa qua một tầng tuyến tính để tính phân phối xác suất trên $C$ lớp. Đây là bài toán có độ phân giải thô nhất (cấp độ chuỗi), không cần quan tâm đến ranh giới cụ thể của từng từ bên trong văn bản.



Sang LAB 09 (Token Classification — Nhận diện thực thể tên NER), bài toán dịch chuyển từ mức câu xuống mức độ từng token (token-level). Thay vì chỉ dùng vector \[CLS], mô hình tận dụng toàn bộ ma trận biểu diễn $H \\in \\mathbb{R}^{T \\times d}$ tại tất cả các vị trí token. Mỗi vector $h\_t$ được chiếu qua một bộ phân loại tuyến tính dùng chung để dự đoán nhãn thực thể theo chuẩn BIO (B-PER, I-PER, O,...). Thách thức kỹ thuật ở LAB 09 là xử lý sự lệch pha giữa từ gốc và subword tokens (như WordPiece) bằng cách gán nhãn -100 cho các token phụ để hàm mất mát Cross-Entropy bỏ qua chúng.



Đến LAB 10 (Extractive Question Answering — Dự đoán khoảng Span), độ phức tạp tăng lên mức tương tác hai chuỗi và định vị ranh giới liên tục (span-level). Đầu vào bắt buộc ghép cặp hai thành phần \[CLS] Question \[SEP] Context \[SEP] để các lớp Self-Attention thực hiện cơ chế chú ý chéo (cross-attention), đối chiếu ngữ nghĩa giữa câu hỏi và từng vị trí trong đoạn văn. Thay vì phân loại từng token độc lập như NER, LAB 10 đặt hai bộ phân loại tuyến tính độc lập trên chuỗi token của Context để dự đoán đồng thời xác suất điểm bắt đầu ($P\_{\\text{start}}$) và điểm kết thúc ($P\_{\\text{end}}$) của câu trả lời, tối ưu hóa tổng hàm mất mát $\\mathcal{L} = \\frac{1}{2}(\\mathcal{L}\_{\\text{start}} + \\mathcal{L}\_{\\text{end}})$. Hơn nữa, LAB 10 đòi hỏi kỹ thuật ánh xạ tọa độ ký tự (offset\_mapping) và cửa sổ trượt chồng lấn (sliding window với stride) để giải quyết giới hạn độ dài chuỗi và đánh giá chất lượng ranh giới thông qua hai thước đo đặc thù là Exact Match (EM) và Token-level F1.



Tóm lại, ba bài thực hành minh họa trọn vẹn sức mạnh của mô hình ngôn ngữ tiền huấn luyện: chỉ cần giữ nguyên phần thân Transformer và thay đổi cách khai thác vector ẩn từ \[CLS] (LAB 08) sang từng token độc lập (LAB 09) và cặp ranh giới liên hợp có điều kiện theo câu hỏi (LAB 10), cùng một mô hình nền tảng có thể giải quyết hiệu quả các bài toán NLP từ đơn giản đến phức tạp.

