
The process for setting up and training a YOLO model:

1. **Install simple_image_download:**
   ```bash
   pip install simple_image_download==0.4
   ```
   Modify `download_images.py` as needed.

2. **Install labelImg for Image Labeling:**
   ```bash
   pip install labelImg
   ```
   Run `labelImg`, set directories, and label images.

3. **Prepare Training and Testing Datasets:**
   Separate images into train and test datasets.

4. **Create Classes File:**
   Add `classes.txt` to the root folder.

5. **Organize Test Folder:**
   Create test folder with images and labels subfolders.

6. **Create Custom Data YAML File:**
   ```yaml
   train: ./train
   val: ./test
   nc: 2 # number of classes
   names: ["item1","item2"]
   ```

7. **Install Required Packages:**
   ```bash
   pip install ultralytics
   pip3 install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
   ```

8. **Train the Model:**
   ```bash
   yolo task=detect mode=train epochs=100 data=data_custom.yaml model=yolov8n.pt imgsz=640
   ```
   
9. **Check Training Results:**
   Results in `run/detect/train`, trained model in `weights` folder.

10. **Predict Using Trained Model:**
    ```bash
    yolo task=detect mode=predict model=yolov8.pt show=True source="" line_thickness=1 hide_labels=True hide_conf=True
    ```

11. **Export Model to Different Format:**
    ```bash
    yolo task=detect mode=export model=yolov8n.pt format=omnx
    ```

12. **Run Custom Model in Python Script:**
    ```python
    from ultralytics import YOLO
    model = YOLO("yolov8.pt")
    model.predict(source="1.jpeg", show=True, save=True, conf=0.5)
    ```

This markdown guide provides a concise overview of the steps required to train and use a YOLO model.