import streamlit as st
import subprocess # to run cli commands in the program
import os # file handling
import shutil # directory handling (to remove exisiting dir)
import moviepy.editor as mpe # to convert format of vedio from avi to mp4

# Set up the title of the web app
st.title('YOLOv8 Object Detection for Videos')


# Function to clear a directory
def clear_directory(directory_path):
    if os.path.exists(directory_path): # checks if dir exists
        shutil.rmtree(directory_path) # remove existing dir
    os.makedirs(directory_path, exist_ok=True) # create new empty dir

# File uploader allows user to add their own video
uploaded_file = st.file_uploader("Upload a video...", type=["mp4", "avi"])

if uploaded_file is not None:
    # Clear the output directory
    clear_directory(r'runs\detect') # delete all previous prediction

    # Save the uploaded video to a temporary path
    temp_video_path = 'temp_video.mp4'  # Assuming mp4 format, change if necessary

    with open(temp_video_path, 'wb') as file: # write binary take variable as file
        file.write(uploaded_file.getbuffer()) # write data to file variable
    
    # Display the uploaded video
    st.video(temp_video_path)
    
    # Run YOLO model prediction using subprocess
    # Adjust the YOLO command based on your model and input type
    # Replace 'yolov8n.pt' with your model's path 
    subprocess.run( # to run cli commands
        ['yolo', 'detect', 'predict', f'model=yolov8s-oiv7.pt', f'source={temp_video_path}', 'show=true'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Handle predicted output for videos accordingly
    # Assuming your YOLO command saves output videos in '\runs\detect\folder\predict1'
    predicted_video_path = r'runs\detect\predict\temp_video.avi'  # Change if necessary
    
    # converting .avi into .mp4
    clip = mpe.VideoFileClip(predicted_video_path)
    clip.write_videofile("output.mp4")
    # Check if the predicted video exists and display it
    if os.path.exists("output.mp4"):
        st.video("output.mp4")

    # Clean up: remove temporary files if needed
    os.remove(temp_video_path)
