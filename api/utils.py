import face_recognition
import numpy as np

def compare_facial_encodings(student_image_file, saved_facial_encodings) -> bool:
    
    #* Convert the saved_facial_encodings string to an nd-array
    saved_facial_encodings_array = np.array(eval(saved_facial_encodings))
    
    image = face_recognition.load_image_file(student_image_file)
    new_image_encodings = face_recognition.face_encodings(image)[0]
    
    result = face_recognition.compare_faces([new_image_encodings], 
                                            saved_facial_encodings_array, tolerance=0.4)
    return result[0]
    