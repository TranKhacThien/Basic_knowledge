# An toàn và bảo mật thông tin

## Chương 1. Các khái niệm cơ sở và hệ mã cổ điển

Câu 1: Phân biệt các thuật ngữ cryptography, cryptanalysis, cryptology. "Khoa học mật mã" tương ứng với từ tiếng anh nào?

Trả lời:

- cryptography(sinh, chế mật mã): nghiên cứu các kỹ thuật toán học nhằm cung cấp các công cụ hay dịch vụ đảm bảo an toàn thông tin.
- cryptanalysis(phá giải mã): nghiên cứu các ký thuật toán học nhằm phục vụ phân tích mật mã và tạo ra các đoạn mã giả nhằm đánh lừa bên nhận.
- cryptology(ngành mật mã): thường được quan niệm là sự kết hợp của hai ngành cryptography và cryptanalysis.

Khoa học mật mã tương ứng với từ :cryptography

Câu 2: Trong thời kỹ nào kỹ thuật mật mã chưa được coi là ngành khoa học? tại sao?

Trả lời: Thời kỳ tính từ thượng cổ cho đến năm 1949 kỹ thuật mật mã chưa được coi là ngành khoa học. Vì trong thời kỹ này ngành này còn mang nhiều tính thủ công, kỹ thuật hơn là tính khoa học.

Câu 3: Hãy phân biệt các hệ mã thông thường(Morse Code, ASCII code) với các hệ mật mã?

Trả lời:

- Hệ mã thông thường biến đổi thông tin đầu vào mã không dùng khóa còn đối với hệ mật mã sử dụng thêm khóa trong quá trình biến đổi đầu vào.
- Đối với các hệ mã thông thương(Morse Code, ASCII code) một đoạn văn bản sau A sau khi mã hóa thành văn bản B thì bất kỳ một người nào iết văn bản đó được mã hóa bằng thuật toán nào(ví dụ: Morse Code, ASCII code) đều có thể từ văn bản B mà tìm ra văn bản A. Còn đối với hệ mật mã một người mặc dù có văn bản B và biết thuật toán mã hóa nhưng nếu không biết khóa sẽ không thể suy ra được văn bản A.

Ví dụ:

- Đối với hệ mã ASCII Code: Nếu một người nhận được đoạn văn bản `97 110 32 116 111 97 110 32 98 97 111 32 109 97 116 32 116 104 111 110 103 32 116 105 110` người đó dễ dàng giải mã được chuỗi thông tin `an toan bao mat thong tin`.
- Đối vơi hệ mật mã afine cipher: Nếu một người nhận được đoạn văn bản `wj pkwj xwk iwp pdkjc pej` nếu người đó không biết khóa là (1,4) thì người đó sẽ không thể giải mã ra chuỗi tin ban đầu là `an toan bao mat thong tin` mặc dù người đó biết đoạn mã được mã hóa bằng hệ mã afine cipher.

Câu 4: Hãy phân tích ý nghĩa của luật Kirchoff để thấy tại sao hệ mật mã hiện đại không chấp nhận quan điểm che giấu thuật toán mật mã:

Câu 5: Phân tích nhược điểm chính của hệ mã đối xứng(SKC):

Trả lời: Nhược điểm chính của hệ mã đối xứng:

- Trong hệ mã đối xứng vai trò của hai phía là như nhau và có thể đổi vai trò. Chính vì vậy về sau nếu có mâu thuẫn sẽ không thể xác định được người mã hóa hoặc giải mã.
- Trong hệ mã đối xứng nếu hai người muốn trao đổi thì họ phải có một khóa bí mật chỉ hai người đó biết. Nếu một người muốn trao đổi với n người thì họ phải lưu n khóa để có thể giao tiếp với n người đó. Trong một hệ thống có n người thì số lượng khóa cần tạo và quản lý là n(n-1)/2.
- Trên cơ sở mã đối xứng ta không thể xây dựng khái niệm chữ ký điện tử và dịch vụ không thể phủ nhận được.
- Vấn đề khó khăn trong xác lập và phân phối khóa giữa hai bên thường ở xa nhau và chỉ có thể liên lạc qua một kênh truyền thông thường không thể trách nghe trộm.

Câu 6: Ưu điểm chính của mã công khai với mã mật:

Trả lời:

- Hệ mã công khai đơn giản hóa việc tạo,quản lý khóa: cụ thể mỗi người chỉ cần quản lý một cặp khóa là có thể trao đổi với tất cả mọi người khác.
- Hệ mã công khai giúp phân biệt được người mã hóa và giải mã.
- Cho phép xây dựng chữ ký điện tử cũng như dịch vụ không thể phủ nhận được.

Câu 11 : Tìm số lượng khóa thực sử được dùng với khóa nhân tính. Hãy lập luận chi tiết:

Trả lời:
Số lượng khóa thực sử được sử dụng với khóa nhân tính là 12 vì những khóa khác sẽ không tạo ra ánh xạ một một giữa bản chữ gốc sang bản thế.

Ví dụ: nếu khóa là 2 thì sẽ có hai kỹ tự b và c có thể cùng được mã hóa thành ký tự c. Như vậy việc giải mã sẽ gặp khó khăn.

Câu 12: Hãy tìm số khóa khả thi affine cipher. Lập luận chi tiết.

Trả lời. Số lượng khóa khả thi của affine cipher là 12x26=312.
Giải thích: Hệ mã afine cipher là sự kết hợp của hai hệ mã nhân tính và cộng tính.
Với hệ mã nhân tính ta có 12 khóa khả thi, hệ mã công tính ta có 26 khóa khả thi nên số khóa khả thi của hệ mã affine cipher là tích của 12x26.

Câu 13: Tại sao không thể nói mọi khóa của hệ khóa một bảng thế là an toàn như nhau?

Trả lời:
Không thể nói mọi khóa của mật mã một bảng thế là an toàn như nhau vì có khóa giúp che giấu thông tin có khóa không giúp che giấu thông tin.
Ví dụ như khóa
a  b  c  d
A  B  C  D
không có tác dụng che giấu thông tin nên sẽ không an toàn bằng các khóa khác.

Câu 14: Tại sao không thể sử dụng quan hệ thứ tự trong cùng một nhóm tần suất để phân tích giải mã. Giải thích qua ví dụ.

Trả lời: Không thể dùng quan hệ thứ tự trong cùng một nhóm tần suất để giải mã vì độ chênh lệch tần suất giữa các ký tự trong cùng một nhóm tần suất là không lớn nên sẽ không đúng trong mọi văn bản.

Ví dụ: ta có văn bản : `this is a shit`
ta mã hóa sử dụng khóa:
t->A
h->B
i->C
s->D
a->E

sau khi mã hóa ta sẽ được đoạn mã: ABCD CD  E DBCA
 ta thấy xác suất các từ trong sâu này ều thuộc nhóm 2 gồm các từ với tần xuất trong văn bản tiếng anh được sắp xếp giảm dần là  : `t,a,o,i,s,h,r`. Nếu ta tính xác suât của sâu ta sẽ thầy p(A)=2/11,p(B)=2/11,p(C)=3/11,p(D)=3/11,p(E)=1/11. Nếu ta sử dụng quan hệ thứ tự trong nhóm 2 để giải mã ta thấy hai ký tự trong bản mã là C và D có xác xuất lớn nhất sẽ là mã hóa của `t` trong nhóm 2 như vậy là sai vì thực tế `t` là mã hóa của A. do vậy không thể sử dụng quan hệ tần xuất trong cùng một nhóm.

 Câu 15 : Tại sao nói quy luật tần suất không đông đều chi phối mạnh mẽ hơn ở các từ có độ dài lớn hơn.

 Trả lời:
 Ta thấy với các từ dài thì giữa các ký tự trong từ sẽ có quan hệ ràng buộc lớn hơn nên việc phân bố tần suất sẽ không đồng đều hơn.
 Ví dụ: ví dụ như nếu ta xét từ có hai âm tiết như oX thì X có thể nhận một trong 4 giá trị `n,f,r,x` còn nếu với một từ có nhiều âm tiết như mXasure thì X chỉ có thể nhận một giá trị `e` do vậy các từ có chưa nhiều âm tiết sẽ khiến cho một số từ có thể ghép với nhiều từ khác có xác xuất cao hơn.

Câu 16: Giải tới cùng ví dụ 1.8:

Câu 17: Hãy giải thích tại sao đồ tần suất trong mật mã đồng âm lại bằng phẳng và tại sao lại có dư thừa?

Trả lời: Trong mật mã đồng âm một ký tự ở bản góc có thể được mã hóa thành các ký tự khác nhau trong bản mã(các ký tự này gọi là đồng âm). Mà số lượng các ký đồng âm với một ký tự được xếp sao cho từ nào có tần suất xuất hiện nhiều sẽ có số lượng từ đồng âm nhiều hơn. Chính vì điều đó làm cho đồ thị tần suất phân bố đều hơn. Chình vì một ký tự trong văn bản gốc có thể được mã hóa thành các ký tự khác nhau trong bản mã nên số số lượng ký tự trong bản mã phải nhiều hơn trong bản gốc dẫn đến dư thừa.

Câu 18: Hãy so sánh IC của một bản rõ M và IC của một bản mã ngẫu nhiên R có cùng độ dài?

Trả lời :
Ta biết rằng IC của một văn bản phụ thuộc vào hai yếu tố:

- Độ dài
- Tần suất xuất hiện các ký tự

Giữa bản rõ M và bản mã R theo đầu bài có cùng độ dài nên IC của hai văn bản sẽ chỉ khác nhau nếu tần xuất xuất hiện các ký tự khác nhau.

Nếu ta sử dụng các hệ mã có bảo toàn tần xuất các ký tự thì giá trị IC sẽ bằng nhau ngược lại sẽ khác nhau.

## Chương 2: Mật mã khối và mã khóa đối xứng

Câu 1: Confusion và diffusion là gì? Nguyên lý tạo ra chúng có khác nhau?

Trả lời:

- Confusion(hỗn loạn, rắc rối): Sự phụ thuộc của bản rõ và bản mã phải thực sự phức tạp để gây rắc rối hỗn loạn cho kẻ thù có ý định phân tích tìm quy luật để phá mã. Quan hệ hàm sỗ  giũa mã-tin là hàm phi tuyến.
- Diffusion(khuếch tán): Làm khuếch tán những mẫu văn bản mang đặc tính thống kê(gây ra do sự dư thừa ngôn ngữ) lẫn vào toàn bộ văn bản. Từ đó gây khó khăn cho kẻ thù trong việc dò phá mã trên cơ sở thống kê cá mẫu lặp lại cao. Sự thay đổi một bit trong một khối bản rõ phải dẫn đến sự thay đổi hoàn toàn trong khối mã tạo ra.

Nguyên lý tạo ra sự confusion là sử dụng phép thay thế trong khi đó diffusion được tạo ra băng phép hoán vị. Toàn bộ sơ đô biến đổi mật mã sẽ là một lưới các biến đổi thây thế-hoán vị.

Câu 2: Cấu trúc sử dụng vòng lặp Feistel là gì ?Tại sao lại cần nhiều vòng lặp? Sự thực hiện các vòng lặp có hoàn toàn giống nhau?

Trả lời: Chúng ta cần sử dụng nhiều vòng lặp để tạo ra tính confusion và diffusion. Các vòng lặp được thực hiện với cùng một hàm f nhưng với các tham số khác nhau. Theo đó đầu vào của một vòng lặp là đầu ra của vòng lặp trước và một khóa con.

Câu 3: Tính đối hợp là gì? Tại sao cần tính đổi hợp trong thiết kế DES?

Trả lời:

- Tính đổi hợp của hàm f tức là hàm f bằng hàm ngược của nó: f=f^-1 hay f(f(x))=x;
- Cần tính đối hợp trong thiết kế DES đề có thể giải mã DES. DES(DES^-1(x))=x

Câu 4: Trong thuật toán DES chứng minh tính đối hợp của T và F đồng thơi chỉ rõ tại sao DES(DES^-1(x))=x với mọi x là chuỗi nhị phân 64 bit.

Trả lời:

Câu 5: Các khóa con của DES có hoàn toàn biệt lập không( không thể suy ra lẫn nhau)?

Trả lời:Các khóa con của DES không hoàn toàn biệt lập(có thể suy ra nhau). Ví dụ nếu ta biết khóa con 1 ta sẽ có thể tách để tìm ra đầu vào của khóa con 1 từ đó có thể tìm được khóa con 2 theo sơ đồ sinh khóa con của DES.

Câu 6: Các S-Box có tính chất gì đặc biết? Có thể ra bao nhiêu S-box nếu không quan tâm tới các tính chất đó?

Trả lời:

Các tính chất đặc biệt của S-Box:

- Các bit vào luôn phụ thuộc không tuyến tính và các bit ra.
- Sửa đổi một bit vào làm thay đổi ít nhất hai bit ra.
- Khi một bit vào thay đổi và 5 bit còn lại cho thay đổi thì S-Box thể hiện ra một tính gọi là phân bố đồng nhất: So sánh bit 0 và bit 1 pử đầu ta luôn ở mức cân bằng. Tính chất này khiến cho việc phân tích theo lý thuyết thống kê để tìm cách phá giải S-Box trở nên vô nghĩa.

Nếu không kể đến các tính chất trên có thể xây dựng được số S-Box là :16x16x4

Câu 7: Hãy giải thích chiều dài thực sự của 2-DES là 57:

![2-DES](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/2-DES.png)
Trả lời:

Câu 8: Hãy vẽ sơ đồ giải mã cho CBC,CFB

Trả lời:

Sơ đồ mã hóa và giải mã CBC:

![CBC](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/CBC.png)

Sơ đồ mã hóa và giải mã CFC:
![CFB](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/CFB.png).

## Chương 3:Hệ mật mã khóa công khai
