# Thai License Plate Recognition System 🚗🇹🇭

ระบบตรวจจับและอ่านป้ายทะเบียนรถยนต์ภาษาไทยอัตโนมัติ (ALPR) แบบเรียลไทม์ ด้วย **YOLOv8** + **EasyOCR**

---

## ✨ ฟีเจอร์หลัก

- ตรวจจับป้ายทะเบียนรถยนต์แบบ Real-time ผ่านเว็บแคม
- อ่านตัวอักษรภาษาไทยและตัวเลขด้วย EasyOCR
- ยืนยันผลด้วยการอ่านซ้ำ 4 รอบก่อนบันทึก (ลด False Positive)
- บันทึกภาพป้ายทะเบียนที่ตรวจพบลง `saved_plates/`
- บันทึก Log (ทะเบียน + เวลา + path รูป) ลงไฟล์ `parking_log.csv`
- แจ้งเตือนด้วยเสียงพูดภาษาไทยผ่าน gTTS เมื่อตรวจพบป้ายสำเร็จ

---

## 🛠️ เทคโนโลยีที่ใช้

| เทคโนโลยี | รายละเอียด |
|-----------|------------|
| [YOLOv8](https://github.com/ultralytics/ultralytics) | Object Detection ตรวจจับตำแหน่งป้ายทะเบียน |
| [EasyOCR](https://github.com/JaidedAI/EasyOCR) | OCR อ่านตัวอักษรภาษาไทย |
| [OpenCV](https://opencv.org/) | ประมวลผลวิดีโอและภาพ |
| [gTTS](https://pypi.org/project/gTTS/) | Text-to-Speech แจ้งเตือนภาษาไทย |
| Python 3.10+ | ภาษาโปรแกรมหลัก |

---

## 📁 โครงสร้างโปรเจกต์

```
Detect_Plate/
├── Detect_Plate.ipynb              # Notebook หลัก (Train + Run)
├── yolov8n.pt                      # Base model YOLOv8 Nano (pre-trained)
├── parking_log.csv                 # Log การตรวจจับทั้งหมด
├── plate/                          # Dataset ป้ายทะเบียนไทย (Roboflow)
│   ├── train/                      # ภาพสำหรับ Training
│   ├── valid/                      # ภาพสำหรับ Validation
│   ├── test/                       # ภาพสำหรับ Testing
│   └── data.yaml                   # Config Dataset
├── Train/
│   └── thai_plate_v1_fast4/
│       └── weights/
│           └── best.pt             # Model ที่ Train แล้ว
└── saved_plates/                   # ภาพป้ายทะเบียนที่ตรวจพบ
```

---

## ⚙️ การติดตั้ง

### ความต้องการของระบบ

- Python 3.10 หรือสูงกว่า
- เว็บแคม
- GPU (แนะนำ) หรือ CPU

### ติดตั้ง Dependencies

```bash
pip install ultralytics opencv-python easyocr pandas pillow matplotlib gTTS playsound==1.2.2
```

---

## 🚀 วิธีรัน

1. Clone โปรเจกต์

```bash
git clone https://github.com/xFieldxGod/Detect_Plate.git
cd Detect_Plate
```

2. ติดตั้ง Dependencies ตามด้านบน

3. เปิดไฟล์ `Detect_Plate.ipynb` ใน Jupyter Lab หรือ VS Code

4. รัน Cell หลักเพื่อเริ่มระบบตรวจจับผ่านเว็บแคม

5. กด `q` เพื่อหยุดโปรแกรม

> **หมายเหตุ:** ค่าเริ่มต้นใช้ `device="mps"` (Mac Apple Silicon)
> หากใช้ Windows/Linux ให้เปลี่ยนเป็น `device="cuda"` (GPU NVIDIA) หรือ `device="cpu"`

---

## 🧠 การ Train โมเดล (ถ้าต้องการ Train ใหม่)

```python
model = YOLO("yolov8n.pt")
model.train(
    data="./plate/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="thai_plate_v1_fast",
    device="mps",  # เปลี่ยนเป็น "cuda" หรือ "cpu" ตามเครื่องของคุณ
)
```

---

## 📊 Dataset

| รายละเอียด | ข้อมูล |
|-----------|--------|
| ชื่อ Dataset | Thai License Plate |
| แหล่งที่มา | [Roboflow Universe](https://universe.roboflow.com/naruesorn/thai-license-plate-j6y9l/dataset/1) |
| จำนวนภาพ | 349 ภาพ |
| Format | YOLOv8 (640×640) |
| License | CC BY 4.0 |

---

## 📋 ตัวอย่างผลลัพธ์ (parking_log.csv)

| Timestamp | Plate | Image |
|-----------|-------|-------|
| 2025-12-01 15:56:57 | กจ3046 | saved_plates/กจ3046_20251201_155657.jpg |
| 2025-12-01 16:10:22 | 1กค771 | saved_plates/1กค771_20251201_161022.jpg |

---

## ✍️ ผู้พัฒนา

- [@xFieldxGod](https://github.com/xFieldxGod)

หากพบปัญหาหรือข้อเสนอแนะ สามารถเปิด Issue หรือ Pull Request ได้เลย 🙌

---

## 📄 License

Dataset: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
