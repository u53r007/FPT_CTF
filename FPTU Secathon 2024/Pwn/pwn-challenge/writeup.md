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
Đề bài không có file exe, elf hay source code để tham khảo code chỉ có cái server thôi. Netcat vào server thử xem nó là cái gì. Hừm!! Server sẽ yêu cầu nhập vào một string bất kì và sẽ response back lại cái string vừa nhập. Vậy nhập thử một string siêu dài thử xem sao :)))

![image](https://github.com/uS3rR00t05/2024/assets/165979681/f315aec0-e5a9-492b-bd7e-a52d1df3e962)
Server khôn nhè :))) có vẻ như nó sẽ tự cắt string ra thành 2 dòng nếu string quá dài để tránh buffer overflow. Haizz!! Vẫn còn một cách nữa!! Do server sẽ response lại bất kì cái gì nhập vào vậy thử nhập vào __%x__ để xem server có thực hiện validation không?

![image](https://github.com/uS3rR00t05/2024/assets/165979681/06837fcc-0afa-4138-a47f-e8732a779e1b)

Ây!!! Không validation là dở rồi :))) Vậy tiếp theo chỉ cần nhập vào vài kí tự __%p__ để xem giá trị tại địa chỉ con trỏ đó (giá trị sẽ được hiển thị dưới dạng hex).

![image](https://github.com/uS3rR00t05/2024/assets/165979681/870bd604-713b-4697-ba18-831043c8f41b)

Paste cái dòng đó qua __cyberchef__ hoặc sử dụng __hex__ để giải mã chuỗi hex đó:

![image](https://github.com/uS3rR00t05/2024/assets/165979681/ae81e833-2849-4451-9a9e-7c1a2747827e)

Nhìn dòng đó trông Sú quá :))) Có vẻ như cái flag mình cần nhưng nó cứ sai sai sao ấy :<< Thì ra cái này nó đang viết dưới dạng __little endian__ thực hiện __swap endianess__ sang __big endian__ và xóa bớt mấy cái dư thừa coi thử:
![image](https://github.com/uS3rR00t05/2024/assets/165979681/80faf8a6-ab9e-4978-8208-8e037d372dff)

Giống cái flag mình cần tìm rồi đấy mà nó vẫn cứ ngược ngược nhờ :). Tiếp theo cần tách chuỗi hex ra đúng 4 bytes để sắp xếp vị trí chúng lại là nó sẽ ra đúng cái flag cần tìm:
![image](https://github.com/uS3rR00t05/2024/assets/165979681/815b10ef-06d5-44d5-a8c3-1ff5fcd67b04)

>Source tham khảo: [Endianess](https://www.youtube.com/watch?v=LxvFb63OOs8&t=7s) 

#### END!!


