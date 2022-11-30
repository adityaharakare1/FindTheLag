from yolov5.detect import run
a = run(source='frame534.jpg', weights='best.pt')
print(a)