TF-IDF vs Average Word2Vec cái nào phù hợp hơn cho dataset được giao?


Prediction: TF-IDF sẽ tốt hơn Average Word2Vec cho tập review phim IMDB.

Reason: Để biết một bài review là khen hay chê, ta thường chỉ cần chú ý đến một vài từ khóa (ví dụ: terrible, boring, masterpiece, excellent). TF-IDF làm rất tốt việc bắt đúng các từ khóa này và đánh trọng số cao cho chúng. Ngược lại, review phim thường khá dài. Nếu dùng Average Word2Vec, ta phải cộng trung bình vector của tất cả các từ trong câu. Việc này sẽ khiến vector của vài từ cảm xúc khen/chê bị chìm và hòa lẫn vào hàng trăm từ bình thường khác (như the, a, actor, scene), khiến mô hình khó nhận diện được cảm xúc thật của bài viết.





Prediction 1: TF-IDF + Logistic Regression có khả năng hoạt động tốt không?

* Prediction: Có, mô hình này sẽ hoạt động rất tốt.
* Reason: Dù đơn giản, TF-IDF kết hợp với Logistic Regression luôn là một baseline cực kỳ mạnh mẽ và ổn định cho phân loại văn bản, đặc biệt là khi văn bản có độ dài vừa và chứa nhiều từ khóa đặc trưng rõ ràng.
* Confidence: Cao.



Prediction 2: Average Word2Vec có chắc chắn tốt hơn TF-IDF không?

* Prediction: Không chắc chắn.
* Reason: Với các văn bản dài như review phim, việc cộng trung bình tất cả các vector của Word2Vec có thể làm nhiễu và pha loãng các từ mang cảm xúc chính, khiến nó thậm chí có thể kém hơn cả TF-IDF.
* Confidence: Cao.



Prediction 3: Nếu tăng vocabulary size thì accuracy chắc chắn tăng không?

* Prediction: Không.
* Reason: Tăng kích thước từ vựng quá lớn sẽ đưa vào mô hình rất nhiều từ hiếm, từ sai chính tả hoặc nhiễu. Khiến mô hình chậm đi, dễ dẫn đến hiện tượng Overfitting.
* Confidence: Bình thường.



Prediction 4: Nếu bỏ stopwords thì performance chắc chắn tăng không?

* Prediction: Không.
* Reason: Dù loại bỏ stopwords giúp giảm nhiễu và giảm kích thước ma trận, nhưng trong một số bài toán (như phân tích cảm xúc), các stopwords như not, very, but lại mang ý nghĩa ngữ pháp cực kỳ quan trọng để đảo ngược hoặc nhấn mạnh cảm xúc.
* Confidence: Cao.



Prediction 5: Accuracy và F1 có thể cho kết luận khác nhau không?

* Prediction: Có thể.
* Reason: Nếu bộ dữ liệu bị mất cân bằng thì Accuracy có thể lên đến 90% dù mô hình dự đoán rất tệ lớp negative. Khi đó, F1-score sẽ thấp và phản ánh đúng thực tế yếu kém của mô hình hơn là Accuracy.
* Confidence: Bình thường.

