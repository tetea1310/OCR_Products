import tkinter as tk
from tkinter import filedialog
import cv2
import easyocr
from PIL import Image, ImageTk
import pickle
import matplotlib.pyplot as plt
# Khởi tạo một màn hình chính
root = tk.Tk()
root.title("Nhận diện ký tự trong ảnh")

# Tạo canvas để hiển thị ảnh và kết quả
canvas = tk.Canvas(root, width=1000, height=500)
canvas.pack()

# Định nghĩa hàm để mở file ảnh và nhận diện ký tự
def open_image():
    # Sử dụng hộp thoại mở tệp để lấy đường dẫn của tệp ảnh
    path = filedialog.askopenfilename()
    # Đọc ảnh bằng OpenCV và reshape về kích thước 500x500
    img = cv2.imread(path)
    img = cv2.resize(img, (600, 600))
    # Chuyển đổi ảnh sang grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Hiển thị ảnh lên canvas
    img_tk = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_tk = Image.fromarray(img_tk)
    img_tk = ImageTk.PhotoImage(image=img_tk)
    canvas.image = img_tk
    canvas.create_image(canvas.winfo_width() / 2, canvas.winfo_height() / 2, anchor='center', image=img_tk)
    # Nhận diện ký tự trong ảnh
    with open('reader.pkl', 'rb') as f:
        reader = pickle.load(f);
    result = reader.readtext(gray)
    # Hiển thị kết quả nhận diện ký tự lên canvas
    for detection in result:
        text = detection[1]
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        font = cv2.FONT_HERSHEY_COMPLEX
        img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),1)
        img = cv2.putText(img,text,top_left,font,0.5,(255,0,0),1,2)
    plt.figure(figsize=(10,10))
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()

       
# Tạo một nút để mở file ảnh và nhận diện ký tự
open_button = tk.Button(root, text="Mở ảnh và nhận diện ký tự", command=open_image)
open_button.pack()

# Khởi động ứng dụng
root.mainloop()
