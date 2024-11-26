### TITLE
>RE1
### DESCRIPTION
> Phân tích file ELF để lấy license key


> Flag format: FUSec{...}

### CATEGORY
>RE
### SCORE
>100
### HINT
>None
### DIFFICULTY
>Easy

### Tool
> Ida, Ghidra, Pwndbg
### FLAG
>FUSec{sjdcnksduqisjcdnmclsudhcwesafvfvasdsdd}
### SOLVED
Mở file RE_Challenge1 bằng tool RE và phân tích hàm __main__ và __check_license_key__ sử dụng psudo code. Phân tích sơ 2 hàm đấy ta có thể hiểu sơ như sau:

Hàm __main__:
  - Khởi tạo biến:
    - Nó khởi tạo hai mảng, v7 và v8, mỗi mảng có 38 giá trị số nguyên được mã hóa cứng, về sau được sử dụng trong quá trình xác thực license key.
    - Nó khai báo một chuỗi bộ đệm __s__ để giữ license key do người dùng nhập.
  - Xác thực định dạng license key xem có thỏa:
    - Phải bắt đầu bằng "FUSec{" (tiền tố).
    - Phải kết thúc bằng "}" (hậu tố).
    - Phần giữa (giữa tiền tố và hậu tố) phải chứa chính xác 38 ký tự.
  - Xác minh license key:
    - Nếu định dạng chính xác, hàm sẽ trích xuất 38 ký tự ở giữa từ đầu vào và gọi hàm __check_license_key__.
    - Hàm __check_license_key__ so sánh 38 ký tự này với các giá trị có nguồn gốc từ v7 và v8.

![image](https://github.com/user-attachments/assets/6b7f7517-7bb0-428c-b045-a7844d94b3e6)

Hàm __check__license_key__:
  - Chức năng lặp qua từng ký tự trong số 38 ký tự trong license key đã nhập. Đối với mỗi ký tự, nó so sánh nó với kết quả của công thức: v7 [i] - v8 [i]. Nếu ký tự không khớp với giá trị mong đợi, hàm trả về 0 (không hợp lệ) và 1 nếu hợp lệ.

![image](https://github.com/user-attachments/assets/30768489-f8dd-4df4-a54e-8c38d2bd286d)

Qua phân tích ta thấy rằng các giá trị số nguyên của v7 và v8 được ghi cứng vào trong hàm __main__ nên ta chỉ cần viết một script để tách các giá trị đó ra thành 2 mảng v7,v8 và join v7,v8 theo dạng: 
> __FuSec{<join(v7,v8)>}__

![image](https://github.com/user-attachments/assets/6a0c45c1-6b73-4371-9fe4-e09029fd4047)

Viết script __Join.py__ và chạy là ra flag.
#### END!!
