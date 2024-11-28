### TITLE
>pwnme
### DESCRIPTION
> just a simple buffer overflow. Flag format: FUSec{...}

>nc challenge.fuctf.com 8001
### CATEGORY
>Pwn
### SCORE
>250
### HINT
>None
### DIFFICULTY
>simple as description :))
### Tools
> Python script & pwndbg or Ida.
### FLAG
>FUSec{On35H00tOnEkil1}

### SOLVED
Tiếp cận đề bài là 2 files: pwn_1 và file code C pwn_1.c. Đọc sơ qua file code C có thể thấy đây là dạng bài buffer overflow làm tràn Instruction Pointer (IP) để trả về kết quả hàm mong muốn (Ret2win). Trong code thì hàm hacked() cũng không có tham số nên chỉ đơn giản là trả về hàm đó để mở flag.

![image](https://github.com/user-attachments/assets/4b119c4e-3ffd-46a7-8a80-9b3a28a550b8)

- __Giai đoạn thử__

Trước tiên tìm offset của hàm hacked(). Có nhiều cách để làm điều đó craft payload (ropstar.py), xài cyclic pwndbg hoặc metasploit, disassemble xong tự tính :))) Ở đây mình xài pwndbg để tìm offset:
```
$ cyclic 100
```
> aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa

 run xong điền cyclic vào

![image](https://github.com/user-attachments/assets/635d454a-4c03-4987-b4c9-f64408781044)

Do đây là file 64-bit nên sẽ không làm overflow được RIP như EIP trong 32-bit, vậy lấy đỡ offset của thằng ngay trên nó là RSP lấy 8 bytes đầu.

```
$ cyclic -l daaaaaaa
```
![image](https://github.com/user-attachments/assets/9b348aba-4c87-48cd-bb7f-af709bbcb8df)

Vậy là đã tìm được offset của hacked() là 24. Giờ dùng payload để chuyển hướng RIP sang hàm hacked() (payload có thể tự craft hoặc dùng của pwntools local_run.py).
![image](https://github.com/uS3rR00t05/2024/assets/165979681/9e735278-21b3-4c58-add0-3c7f4fabd0f5)
Tada thành công!! Nếu đọc kĩ source code thì sẽ thấy là hàm hacked() đã được trả về đúng kết quả nhưng flag chưa có vì code đang chạy trên local nên làm gì có file flag mà đọc :))). Thêm bước thử nữa tạo 1 file flag.txt điền đại vô đó coi nó có chạy không.
![image](https://github.com/uS3rR00t05/2024/assets/165979681/6d385b28-ae73-48cb-9bce-cf26c084edbc)
Tuyệt!! xong bước thử trên local giờ deploy lên trên server.

- __Giai đoạn deploy__
  
Giai đoạn này sẽ khó hơn xíu vì không thể copy cái script rồi quăng lên trên server được vì:
- Cái script được thiết lập chạy trên local.
- Bản chất code vẫn trả kết quả cuối cùng là lỗi overflow (SIGSEGV Segmentation fault) và cái flag ta thấy thực chất chỉ nằm trên RSP nên khi deploy lên server sẽ không output kết quả ra. 

Nên phải tạo một script khác để capture dòng response đầu tiên của server trả về trước khi trả lỗi overflow. Có thể nhờ chat gờ bê tê :)))
Vào pwndbg:
>disassemble hacked để có thể check address của hàm hacked().

![image](https://github.com/uS3rR00t05/2024/assets/165979681/4314a9ad-45b8-4bf9-97d8-9490d164f666)

xong sau đó chạy file script exploit.py sẽ ra được flag.
>[!NOTE]
>Phải chọn đúng địa chỉ của instruction __mov rbp,rsp__ thì mới mở flag được là bởi vì đang xài offset của RSP chứ không phải RIP.

>Source tham khảo:
>[PicoCTF JohnHammond](https://www.youtube.com/watch?v=eg0gULifHFI)
>[Ret2win](https://www.youtube.com/watch?v=E4ZWJsGySoY&t=508s)
#### END!!
