import streamlit as st 
from PIL import Image # to handle image files
import subprocess # to run cli commands in the program
import os # file handling
import shutil # directory handling (to remove exisiting dir)

# Set up the title of the web app
st.title('YOLOv8 Object Detection')

# Function to clear a directory
def clear_directory(directory_path):
    if os.path.exists(directory_path): # checks if dir exists
        shutil.rmtree(directory_path) # remove existing dir
    os.makedirs(directory_path, exist_ok=True) # create new empty dir

# File uploader allows user to add their own image
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Clear the output directory
    clear_directory(r'runs\detect') # delete all previous prediction

    # Save the uploaded image to a temporary file
    temp_image_path = 'temp_image.jpg' 
    with open(temp_image_path, 'wb') as file: # write binary take variable as file
        file.write(uploaded_file.getbuffer()) # write data to file variable
    
    # Display the uploaded image 
    image = Image.open(temp_image_path) # open img using variable
    st.image(image, caption='Uploaded Image.', use_column_width=True) # to show image in web
    
    # Run YOLO model prediction using subprocess
    # Replace 'yolov8n.pt' with your model's path 
    # yolo detect predict model=yolov8s-oiv7.pt source=0 show=true   
    subprocess.run( # to run cli commands
        ['yolo', 'detect', 'predict', f'model=yolov8s-oiv7.pt', f'source={temp_image_path}', 'show=true'],
        stdout=subprocess.PIPE, # to see output of the command
        stderr=subprocess.PIPE, # to see if there were any error messages
        text=True
    )
    
    # Assuming your YOLO command saves output images in '\runs\detect\folder\predict1'
    predicted_image_path = r'runs\detect\predict\temp_image.jpg'   # takeing the path of stored output
    
    # Check if the predicted image exists and display it
    if os.path.exists(predicted_image_path): # chceking for output
        predicted_image = Image.open(predicted_image_path) # opening img
        st.image(predicted_image, caption='Predicted Image.', use_column_width=True) # printing img on web

    # Clean up: remove temporary file if needed
    os.remove(temp_image_path) # clearing the variable to release memory

