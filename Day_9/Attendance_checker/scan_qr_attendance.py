import cv2

attendance = {}

def mark_attendance(data):
    emp_id, name = data.split(",")
    attendance[emp_id] = {"Name": name}
    print(f"Marked Present: {name}")

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

print("Scanning for QR Code...")

while True:
    success, frame = cap.read()
    data, bbox,success = detector.detectAndDecode(frame)
    
    if data:
        mark_attendance(data)
        break

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("\nToday's Attendance:")
for emp_id, info in attendance.items():
    print(f"ID: {emp_id}, Name: {info['Name']}")
