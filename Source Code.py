import streamlit as st
import cv2
import numpy as np
import tempfile
import os

# Lane Detection Functions (same as your original code)
def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(blur, 50, 150)

def region_of_interest(canny):
    height, width = canny.shape
    mask = np.zeros_like(canny)
    triangle = np.array([[ 
        (200, height), 
        (800, 320), 
        (1050, height)
    ]], np.int32)
    cv2.fillPoly(mask, triangle, 255)
    return cv2.bitwise_and(canny, mask)

def houghLines(cropped_canny):
    return cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), 40, 5)

def display_lines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

def make_points(image, line):
    slope, intercept = line
    y1 = image.shape[0]
    y2 = int(y1 * 3 / 5)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return [[x1, y1, x2, y2]]

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope, intercept = fit
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    left_avg = np.average(left_fit, axis=0) if left_fit else None
    right_avg = np.average(right_fit, axis=0) if right_fit else None

    lines_out = []
    if left_avg is not None:
        lines_out.append(make_points(image, left_avg))
    if right_avg is not None:
        lines_out.append(make_points(image, right_avg))
    return lines_out

def addWeighted(frame, line_image):
    return cv2.addWeighted(frame, 0.8, line_image, 1, 1)

# Streamlit App
st.title("🚗 Lane Detection Web App")
st.write("Upload a video to visualize lane detection using OpenCV + Streamlit.")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)
    stframe = st.empty()

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.resize(frame, (1280, 720))
        canny_image = canny(frame)
        cropped = region_of_interest(canny_image)
        lines = houghLines(cropped)
        avg_lines = average_slope_intercept(frame, lines)
        line_img = display_lines(frame, avg_lines)
        result = addWeighted(frame, line_img)

        # Convert to RGB and display in Streamlit
        result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        stframe.image(result_rgb, channels="RGB", use_container_width=True)  # Updated here
    
    cap.release()
    os.remove(tfile.name)
