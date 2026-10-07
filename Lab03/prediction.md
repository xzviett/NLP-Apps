Prediction 1: Những từ nào gần nhau nhất? (doctor, physician, hospital, banana, car)

* Prediction: doctor và physician sẽ gần nhau nhất. Theo sau là nhóm doctor/physician với hospital. banana và car sẽ nằm ở những cụm hoàn toàn xa cách và không liên quan.
* Reason: "doctor" và "physician" là hai từ đồng nghĩa. "Hospital" có chung chủ đề nhưng khác từ loại và vai trò cú pháp nên khoảng cách sẽ xa hơn một chút. Quả chuối và ô tô không có cùng bất kỳ context nào với nhóm y tế.
* Confidence: Rất cao.



Prediction 2: Nếu context window tăng từ 2 → 5, similarity có thay đổi không?

* Prediction: Có thay đổi. Khi tăng window size, các từ cùng chủ đề sẽ xích lại gần nhau hơn, trong khi các từ đồng nghĩa có thể bị giảm độ tương đồng tương đối.
* Reason: Window nhỏ k=2 tập trung vào quan hệ cú pháp và cấu trúc ngữ pháp. Window lớn k=5 sẽ quét rộng ra cả câu, bắt được quan hệ ngữ nghĩa theo mảng chủ đề.
* Confidence: Cao.



Prediction 3: Nếu embedding dimension: 50 → 100 → 300 thì chất lượng có chắc chắn tăng không?

* Prediction: Chất lượng thường sẽ tăng mạnh từ 50 lên 100 hoặc 300, nhưng sau mức 300 sẽ bão hòa, và nếu corpus quá nhỏ thì việc tăng số chiều sẽ làm mô hình tệ đi.
* Reason: Số chiều cao giúp vector có đủ dung lượng để biểu diễn các đặc trưng ngữ nghĩa phức tạp. Tuy nhiên, nếu tăng số chiều quá lớn trong khi tập dữ liệu huấn luyện (corpus) nhỏ, mô hình sẽ bị Overfitting.
* Confidence: Cao.



Prediction 4: Từ doctor, physician có chắc chắn gần nhau không nếu corpus chỉ có 100 câu?

* Prediction: Khả năng cao là chúng sẽ có similarity rất thấp hoặc vector của chúng là vector rỗng.
* Reason: Với chỉ 100 câu, hiện tượng Data Sparsity sẽ vô cùng nghiêm trọng. Từ "physician" có thể không xuất hiện lần nào, hoặc chỉ xuất hiện 1 lần cạnh từ "said", khiến mô hình không đủ điểm mù dữ liệu để liên kết nó với "doctor".
* Confidence: Rất cao.

























