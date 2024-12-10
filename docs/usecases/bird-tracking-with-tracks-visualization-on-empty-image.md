---
comments: true  
description: Learn how to track birds with path visualization using Ultralytics YOLO11 for real-time monitoring and ecological research through computer vision.  
keywords: bird tracking, YOLO11, Ultralytics YOLO11, AI wildlife monitoring, bird path visualization, ecological research, real-time bird tracking, computer vision, environmental data collection  
---

# Real-Time Bird Tracking with Path Visualization Using Ultralytics YOLO11 🦅  

Explore how to track birds and visualize their flight paths using [Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11/). This guide will show you how to detect birds, calculate flight paths, and visualize their movement using a custom-trained YOLO11 model.

<div class="embed-container">
  <iframe src="https://drive.google.com/file/d/1QkCcTqfZmB9aPIb9ml62je-A3hljdCR-/preview" 
          allow="autoplay">
  </iframe>
</div>

### Step 1: Load the YOLO Model and Video

We start by loading the fine-tuned YOLO model and preparing the video file for processing. The model used in this tutorial is already trained to detect birds efficiently in real-time.  

```python  
import cv2  
import numpy as np  
from ultralytics import YOLO  
from ultralytics.utils.plotting import Annotator  

# Load the YOLO model for bird detection  
model = YOLO("yolo11s.pt")  

# Load the video file  
cap = cv2.VideoCapture("path/to/video/file.mp4")  

# Retrieve video properties like width, height, and frame rate  
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,  
                                       cv2.CAP_PROP_FRAME_HEIGHT,  
                                       cv2.CAP_PROP_FPS))  

# Initialize video writers for saving original and tracking visualizations  
vwriter = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 
                          fps, (w, h))  
vwriter1 = cv2.VideoWriter("birds_black.avi", cv2.VideoWriter_fourcc(*"MJPG"), 
                           fps, (w, h))  
```

### Step 2: Start Video Processing

Now it's time to read the video frame by frame, preparing each frame for further processing while ensuring the video feed runs continuously until all frames are processed.

```python  
while cap.isOpened():  
    success, im0 = cap.read()  # Read a video frame  
    if not success:  
        break  

    ann = Annotator(im0, line_width=3)  # Initialize annotator for drawing  

    # Create a blank frame for path visualization
    empty_image = np.zeros_like(im0)  
```

### Step 3: Detect and Track Birds

We will utilize the YOLO model loaded in memory during Step #01 to detect birds in the current frame, extracting bounding boxes, class labels, and unique tracking IDs for each detected bird.

```python  
# Perform bird detection and tracking  
results = model.track(im0, persist=True)  

# Extract bounding boxes, class labels, and tracking IDs  
boxes = results[0].boxes.xyxy.cpu().numpy()  
clss = results[0].boxes.cls.cpu().tolist()  
track_ids = results[0].boxes.id.int().cpu().tolist()  
```

### Step 4: Visualize Bird Movement Paths

In this step, we will determine the centroid of each detected bird's bounding box, draw circles to represent their movement, and overlay tracking IDs on a blank frame for path visualization.

```python  
for box, cls, t_id in zip(boxes, clss, track_ids):  
    # Calculate the centroid of the bounding box  
    x1, y1, x2, y2 = box  
    cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)  

    # Draw a white circle at the centroid to represent bird movement  
    circle_radius = 30  
    cv2.circle(empty_image, (cx, cy), radius=circle_radius, 
               color=(255, 255, 255), thickness=-1)  

    # Display tracking ID inside the circle for easy identification  
    font_scale = 1.0  
    font_thickness = 2  
    text_size = cv2.getTextSize(str(t_id), cv2.FONT_HERSHEY_SIMPLEX, 
                                font_scale, font_thickness)[0]  
    text_x = cx - text_size[0] // 2  
    text_y = cy + text_size[1] // 2  
    cv2.putText(empty_image, str(t_id), (text_x, text_y), 
                cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), 
                font_thickness)  

    # Annotate the original frame with detection boxes  
    ann.box_label(box, label=model.names[cls], color=(235, 219, 11))  
```

### Step 5: Save and Display Frames

Now it's time to display both the original and tracking visualization frames while saving them as video files for future reference and analysis.

```python  
# Display the original frame  
cv2.imshow("Original Frame", im0)  

# Save processed frames to video files  
vwriter.write(im0)  
vwriter1.write(empty_image)  

# Stop if the user presses 'q'  
if cv2.waitKey(1) & 0xFF == ord("q"):  
    break
```

### Step 6: Release Resources

Finally, we release all resources like video files and close display windows to complete the tracking process.  

```python  
# Release all resources  
vwriter.release()  
vwriter1.release()  
cap.release()  
cv2.destroyAllWindows()  
```

### Complete Code in One Block

```python  
import cv2  
import numpy as np  
from ultralytics import YOLO  
from ultralytics.utils.plotting import Annotator  

model = YOLO("yolo11s.pt")   # Load the YOLO model 
cap = cv2.VideoCapture("path/to/video/file.mp4")   # Load the video 

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,  
                                       cv2.CAP_PROP_FRAME_HEIGHT,  
                                       cv2.CAP_PROP_FPS))  

# Initialize video writers  
vwriter = cv2.VideoWriter("output.avi", 
                          cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))  
vwriter1 = cv2.VideoWriter("birds_black.avi", 
                           cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))  

# Process video frames  
while cap.isOpened():  
    success, im0 = cap.read()  
    if not success:  
        break  

    ann = Annotator(im0, line_width=3)  
    empty_image = np.zeros_like(im0)  

    # Detect and track birds  
    results = model.track(im0, persist=True)  
    boxes = results[0].boxes.xyxy.cpu().numpy()  
    clss = results[0].boxes.cls.cpu().tolist()  
    track_ids = results[0].boxes.id.int().cpu().tolist()  

    for box, cls, t_id in zip(boxes, clss, track_ids):  
        x1, y1, x2, y2 = box  
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)  

        # Draw tracking circles  
        circle_radius = 30  
        cv2.circle(empty_image, (cx, cy), radius=circle_radius, 
                   color=(255, 255, 255), thickness=-1)  

        # Display tracking ID  
        font_scale = 1.0  
        font_thickness = 2  
        text_size = cv2.getTextSize(str(t_id), cv2.FONT_HERSHEY_SIMPLEX, 
                                    font_scale, font_thickness)[0]  
        text_x = cx - text_size[0] // 2  
        text_y = cy + text_size[1] // 2  
        cv2.putText(empty_image, str(t_id), (text_x, text_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), 
                    font_thickness)  

        # Annotate original frame  
        ann.box_label(box, label=model.names[cls], color=(235, 219, 11))  

    # Display frames  
    cv2.imshow("Original Frame", im0)  

    # Save frames to output files  
    vwriter.write(im0)  
    vwriter1.write(empty_image)  

    if cv2.waitKey(1) & 0xFF == ord("q"):  
        break  

# Release resources  
vwriter.release()  
vwriter1.release()  
cap.release()  
cv2.destroyAllWindows()  
```

### Real World Applications

There are many real-world applications for this, but a few where this idea can be used are mentioned below:  

- **Wildlife Monitoring:** Study flight paths in real-time to monitor habitat usage, track species movement, and understand animal behavior for conservation purposes.  
- **Ecological Research:** Analyze migration patterns and seasonal movements to gain insights into bird populations and their responses to environmental changes.  
- **Environmental Impact Assessment:** Evaluate how ecological changes affect bird populations by analyzing flight data and habitat shifts over time.

### FAQ

#### What is bird tracking with path visualization?

Bird tracking with path visualization involves detecting birds in videos or live streams, tracking their movements, and displaying flight paths visually using computer vision models like YOLO11.  

#### Which models are best for bird tracking?

Models like Ultralytics YOLO11, [YOLOv10](https://docs.ultralytics.com/models/yolov10/) and [Ultralytics YOLOv8](https://docs.ultralytics.com/models/yolov8/) are highly effective for bird detection and path visualization due to their real-time tracking capabilities.  

#### Can this system work in real-time?

Yes, with the right hardware (GPU-accelerated systems) and optimized models, real-time bird tracking is achievable for ecological monitoring and wildlife research.  

#### What are the real-world applications of bird tracking?

Bird tracking is used in wildlife monitoring, ecological research, environmental impact assessments, and even aviation safety to prevent bird-aircraft collisions.  

### Social Resources

- [Join the Discussion on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7269657411311845376/)

Start your bird tracking journey with YOLO11 today! 🚀