import sys
import time
from datetime import datetime
from tkinter import messagebox



from facenet.face_contrib import *
import mysql.connector


def attendance(i, n, c, f):
    with open('attendance.csv', 'r+', newline='\n') as file:
        DataList = file.readlines()
        namelist = []
        for data in DataList:
            ent = data.split(',')
            namelist.append(ent[0])
        if ((i not in namelist) and (n not in namelist) and (c not in namelist) and (f not in namelist)):
            curr = datetime.now()
            dt = curr.strftime("%d/%m/%Y")
            h = curr.strftime('%H:%M:%S')
            file.writelines(f'\n{i},{n},{c},{f},{dt},{h}')


def add_overlays(frame, faces, frame_rate, colors, confidence=0.8):
    if faces is not None:
        for idx, face in enumerate(faces):
            face_bb = face.bounding_box.astype(int)
            cv2.rectangle(frame, (face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]), colors[idx], 2)

            if face.name and face.prob:
                if face.prob > confidence:
                    class_name = face.name
                    s = str(class_name)
                    r = re.findall(r'\d', s)
                    id =''.join(r)

                    conn = mysql.connector.connect(host='localhost', user="root", password='Vilong242',
                                                   db='face_recognition')
                    cur = conn.cursor()

                    cur.execute("select Student_ID from student where Student_ID=" + str(id))
                    i = cur.fetchone()
                    i = '+'.join(i)

                    cur.execute("select Name from student where Student_ID=" + str(id))
                    n = cur.fetchone()
                    n = '+'.join(n)

                    cur.execute("select Class from student where Student_ID=" + str(id))
                    c = cur.fetchone()
                    c = '+'.join(c)

                    cur.execute("select Faculty from student where Student_ID=" + str(id))
                    f = cur.fetchone()
                    f = '+'.join(f)


                    cv2.putText(frame, f'Student ID:{i}', (face_bb[0], face_bb[3] + 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, colors[idx], thickness=2, lineType=1)
                    cv2.putText(frame, f'Name:{n}', (face_bb[0], face_bb[3] + 45), cv2.FONT_HERSHEY_COMPLEX, 0.6, colors[idx], thickness=2, lineType=1)
                    cv2.putText(frame, f'Class:{c}', (face_bb[0], face_bb[3] + 70), cv2.FONT_HERSHEY_COMPLEX, 0.6, colors[idx], thickness=2, lineType=1)
                    cv2.putText(frame, f'Faculty:{f}', (face_bb[0], face_bb[3] + 95), cv2.FONT_HERSHEY_COMPLEX, 0.6, colors[idx], thickness=2, lineType=1)
                    cv2.putText(frame, '{:.02f}'.format(face.prob * 100), (face_bb[0], face_bb[3] + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[idx], thickness=1, lineType=2)
                    
                    attendance(i,n,c,f)
                else :
                    class_name = 'Unknown People'
                    cv2.putText(frame, class_name, (face_bb[0], face_bb[3] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[idx], thickness=2, lineType=2)
        cv2.putText(frame, str(frame_rate) + " fps", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2, lineType=2)


def run(model_checkpoint, classifier, output_file=None):
    frame_interval = 3  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    width = frame.shape[1]
    height = frame.shape[0]
    if output_file is not None:
        video_format = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_file, video_format, 20, (width, height))

    face_recognition = Recognition(model_checkpoint, classifier)
    start_time = time.time()
    colors = np.random.uniform(0, 255, size=(1, 3))
    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()

        if (frame_count % frame_interval) == 0:
            faces = face_recognition.identify(frame)
            for i in range(len(colors), len(faces)):
                colors = np.append(colors, np.random.uniform(150, 255, size=(1, 3)), axis=0)
            # Check our current fps
            end_time = time.time()
            if (end_time - start_time) > fps_display_interval:
                frame_rate = int(frame_count / (end_time - start_time))
                start_time = time.time()
                frame_count = 0

        add_overlays(frame, faces, frame_rate, colors)

        frame_count += 1
        cv2.imshow('Welcome to school', frame)
        if output_file is not None:
            out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    if output_file is not None:
        out.release()
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run('models', 'models/your_model.pkl')