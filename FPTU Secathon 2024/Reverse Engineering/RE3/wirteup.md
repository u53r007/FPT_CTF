### TITLE
>RE3
### DESCRIPTION
> Phân tích file ELF để in được.


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
> Ida, Ghidra, Pwndbg, DIE
### FLAG
>FUSec{Y0ugotm2friendscongrat}
### SOLVED
Tiếp cận đề bài mở file RE_Challenge3 bằng tool RE thì chỉ thấy xuất hiện các hàm sub => file này đang bị pack. Sử dụng các công cụ phát hiện pack để xem file bị pack như thế nào. Sử dụng DIE thì ta thấy nó sử dụng UPX-packed.

![image](https://github.com/user-attachments/assets/cddf747d-d5b5-4b88-9f2b-1aa7b00ea90f)

Ta thực hiện unpack cái UPX đó:
```
upx -d RE_Challenge3
```
Sau khi unpack, tìm đến hàm __main__ ta phân tích bằng psudocode có thể hiểu sơ như sau:

__Hàm main__:
- Kiểm tra đối số:
  - Nó kiểm tra xem số lượng đối số (argc) có chính xác là 3 hay không.
  - Nó xác minh rằng đối số thứ hai (đối số đầu sau tên chương trình)  là __"get_flag"__.
- Nếu kiểm tra không thành công, nó sẽ in thông báo lỗi và thoát với giá trị trả về là 1.
- Nếu kiểm tra thành công, nó gọi một hàm có tên __decrypt_flag__.

![image](https://github.com/user-attachments/assets/fdaee623-53c3-4c4d-a7f4-5072a64493e9)

Ta tiếp tục đến với hàm __decrypt_flag__:
- Nó kiểm tra đối số thứ ba phải là: __"secretflagkey"__ nếu đúng thì nó sẽ in ra flag, nếu không thì nó sẽ thoát chương trình.

![image](https://github.com/user-attachments/assets/2595c8d2-5869-4b54-8d37-8ee5e138a9d4)

Vậy thông qua 2 hàm ta vừa phân tích ta có thể hiểu sơ là chương trình cần chạy với 2 đối số là: __get_flag__ và __secretflagkey__. Từ đó ta chạy chương trình là ra flag:
```
./RE_Challenge3 get_flag secretflagkey
```
#### END!!
