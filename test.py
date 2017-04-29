import cv2
import face_recognition

cap = cv2.VideoCapture('test_video.mp4')
#fp = open('face_embed.txt', 'w')
all_encodings = []
while (cap.isOpened()):
    ret, frame = cap.read()
    rows,cols = frame.shape[0:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2),-90,1)
    frame = cv2.warpAffine(frame, M, (cols,rows))
    # get faces
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    results = face_recognition.compare_faces(all_encodings, face_encodings)
    if not results:
        all_encodings.append(face_encodings)
    #fp.write(str(face_encodings) + '\n')
    #cv2.imshow('frame', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

print 'number of unique faces = {}'.format(len(all_encodings))
#fp.close()
