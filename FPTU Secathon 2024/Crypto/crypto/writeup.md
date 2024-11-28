### TITLE
>crypto
### DESCRIPTION
>Decrypt this message: ['159.96.34.204', '136.182.188.58', '155.20.31.30', '12.234.113.15', '153.170.118.69', '189.152.240.17', '180.27.111.161', '87.205.101.118', '45.1.136.2', '122.3.3.3']

>Flag format: FUSec{...}
### CATEGORY
>Crypto
### SCORE
>100
### HINT
>None
### DIFFICULTY
>Easy
### FLAG
>FUSec{howdyiamnowinyourhanddecrypted}
### SOLVED
Tiếp cận với đề bài là một đoạn IPv4 và đoạn code mã hóa __encrypt.py__. Phân tích đoạn code có thể chú ý một vài hàm sau:
- __cipher(k, d)__: Mã hóa dữ liệu __d__ bằng khóa __k__ với thuật toán giống RC4, xuất ra một bytearray.
- __encr(pt, k)__: Mã hóa plaintext __pt__ bằng khóa __k__, thêm padding và chuyển đổi kết quả thành danh sách các địa chỉ IPv4.
- __d2ip(d)__: Chuyển đổi dữ liệu được mã hóa __d__ thành danh sách các địa chỉ IPv4, coi mỗi chunk 4 bytes là một số 32 bit.

Qua phân tích các hàm của encrypt.py ta có thể craft code để decrypt như sau:
- __Chuyển đổi IPv4 sang dữ liệu d__: Sử dụng __socket.inet_aton__ để chuyển đổi địa chỉ IPv4 thành các khối 4 bytes và kết hợp chúng thành một bytearray.
- __Xóa padding__: Sử dụng byte cuối cùng để xác định và loại bỏ padding.
- __Giải mã__: Đảo ngược hàm __cipher(k, d)__ sử dụng khóa __k__ để giải mã bytearray.

Chạy file __decrypt.py__ để ra flag.
#### END!!
