### TITLE
>Passio
### DESCRIPTION
>Bobby asked me for help with a RSA problem without n, I looked at it then told him "Are you sure?"

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
>FUsec{S1mpl3_biN0m1al_sQu4r3}
### SOLVED
Tiếp cận đề bài ta có 2 file: passio.py và output.txt. Lấy file mã hóa __passio.py__ phân tích ta sẽ hiểu sơ hàm mã hóa như sau:

__Hàm encrypt(m)__:
- Tạo ra hai số nguyên tố lớn __p__ và __q__
- Tính toán modulus sử dụng: __p x q__
- Mã hóa tin nhắn __m__ sử dụng số mũ __e__ (e= 65537)
- __c=m^e mod n__
- Tính 2 tham số bổ sung:
  - __a__ = __(p-q)^2__
  - __b__ = __(- a + p^2 + (n/p)^2 )//2__

Thông qua những gì phân tích có thể thấy đây là thuật toán mã hóa RSA nhưng có thêm tham số bổ sung. Các bước giải:

1. Giải ngược 2 tham số a,b để ra n.
2. Có được n ta thực hiện factor n để ra p,q sử dụng __Factor.py__.
3. Dùng script giải mã RSA để giải flag từ n, p, q sử dụng __RSAdecrypt.py__.
> Source tham khảo: [RSA](https://youtu.be/JD72Ry60eP4?si=QYETk6Euso91bV2R), [RSA breaking](https://www.youtube.com/watch?v=-ShwJqAalOk)

#### END!!
