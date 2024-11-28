### TITLE
>Basic Steganography
### DESCRIPTION
> Flag format: FUSec{...}

> During the process of collecting digital evidence, you (a member of the digital investigation team) suspect that an image file (fictory.jpg) is obtained that has hidden information inside. Let's try to find that information.
### CATEGORY
>Forensic
### SCORE
>100
### HINT
>None
### DIFFICULTY
>Easy
### FLAG
>FUSec{70VictoryDienBienPhu}
### SOLVED
Phân tích bức hình fictory.jpg. Việc đầu tiên nên làm tất nhiên là mở bức hình xem nó là cái gì đã. Bức hình thì quá nổi tiếng rồi nhưng cũng không có gì đặc sắc liên quan tới flag chúng ta cần. Sau đó thử extract metadata:
```
$ exiftool fictory.jpg
```
Trong metadata cũng không có gì cần chú ý cả. Cuối cùng thử extract hex của bức hình.
```
$ xxd fictory.jpg
```
![image](https://github.com/user-attachments/assets/78e5e241-b12c-4842-917d-f6b67628b43d)

Và nó ra luôn :)) Ảo thật đấy!!

#### END!!
