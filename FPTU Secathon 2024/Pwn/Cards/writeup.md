### TITLE
>Cards
### DESCRIPTION
> "Người không chơi là người không bao giờ thắng, Người thua là người chưa thắng, Người bỏ cuộc là thất bại, Còn chơi là còn gỡ." - Nhà cái đến từ Tâu Âu. Flag format: FUSec{...}

>nc challenge.fuctf.com 8006
### CATEGORY
>Pwn
### SCORE
>100
### HINT
>None
### DIFFICULTY
>easy
### FLAG
>FUSec{th1s_1s_3x4ctly_h0w_my_pwn2own_l00k_l1k3!!}
### SOLVED
Tiếp cận với đề bài sẽ cho 2 files: 1 là file cardg và cái còn lại là file code C cardg.c. Ta bắt đầu khai thác file code C trước. Để ý kĩ trong hàm play() sẽ thấy, ở phần cược vàng khi nhập số vào thì hàm if sẽ chỉ kiểm tra xem có nhập số quá lớn hơn số vàng hiện có hay không thôi. Âu!! Vậy thì nhập thử số âm xem sao :)))

![image](https://github.com/uS3rR00t05/2024/assets/165979681/e82332a9-e506-4f9f-9d29-2efcf384bf8e)

Chạy file cardg để thử giả thuyết hoặc netcat lên server để thử nuôn cho phẻ. Nhập một số âm cực lớn, bam tỷ phú trong một nốt nhạc! :))) Code bị lỗi logic!
![image](https://github.com/uS3rR00t05/2024/assets/165979681/6d0556fa-5753-467d-90e3-9c3a7b99e099)

Xong chỉ cần chọn 2 để mua flag thôi.
#### END!!
