### TITLE
>pwn-challenge
### DESCRIPTION
> Can you snag the flag by exploiting a simple buffer overflow? Flag format: FUSec{...}

>nc challenge.fuctf.com 8003
### CATEGORY
>Pwn
### SCORE
>100
### HINT
>None
### DIFFICULTY
>simple as description :))
### FLAG
>FuSec{flag-a7j349dx}
### SOLVED
Đề bài không có file exe, elf hay source code để tham khảo code chỉ có cái server thôi. Netcat vào server thử xem nó là cái gì. Server sẽ yêu cầu nhập vào một string bất kì và sẽ trả lại cái string vừa nhập. Do server sẽ trả lại bất kì cái gì nhập vào vậy thử nhập vào __%x__ để xem server có thực hiện validation không?

Server không thực hiện validation và code bị lỗi format string. Tiếp theo nhập vào vài kí tự __%p__ để xem giá trị tại địa chỉ con trỏ đó (giá trị sẽ được hiển thị dưới dạng hex).

Paste cái dòng đó qua __cyberchef__ hoặc sử dụng __hex__ để giải mã chuỗi hex đó và chuyển chuỗi từ __little endian__ sang __big endian__ và xóa bớt mấy dòng thừa. Sau đó tách chuỗi hex ra 4 bytes và thực hiện ghép lại đúng thứ tự sẽ ra flag.

>Source tham khảo: [Endianess](https://www.youtube.com/watch?v=LxvFb63OOs8&t=7s) 

#### END!!


