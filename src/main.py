from functions import *

if(__name__=="__main__"):
    # an array with necessary file paths
    args = []
    # paths to the facial landmarks file
    args.append("../files/shape_predictor_68_face_landmarks.dat")
    # path to alarm audio file
    args.append("../files/alarm.wav")
    # index of the camera being used - webcam is generally zero - check acc to your system
    args.append(0)

    landmark_detection(args)
