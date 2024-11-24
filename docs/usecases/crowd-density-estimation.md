---
comments: true
description: Learn how to estimate crowd density using Ultralytics YOLO11 for efficient crowd monitoring and analysis.
keywords: crowd density estimation, YOLO11, Ultralytics YOLO11, AI crowd analysis, crowd monitoring, real-time crowd analysis, computer vision, crowd detection, advanced image processing
---

# Accurate Crowd Density Estimation Using Ultralytics YOLO11 🎯

Discover how to utilize [Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11/) for accurate crowd density estimation. This guide will take you through a step-by-step implementation using a YOLO11-based system to measure and monitor crowd density in various environments, improving safety and event management capabilities.

<div class="embed-container">
  <iframe src="https://drive.google.com/file/d/1kF1AZbLWOsMzQOoU_mFeonxB-4ysgawz/preview" 
          allow="autoplay">
  </iframe>
</div>

## System Specifications Used for This Implementation

- **CPU**: Intel® Core™ i7-10700 CPU @ 2.90GHz for efficient processing.
- **GPU**: NVIDIA RTX 3060 for faster object detection.
- **RAM & Storage**: 32 GB RAM and 512 GB SSD for optimal performance.
- **Model**: Pre-trained YOLO11 model for person detection.
- **Dataset**: Custom dataset for various crowd scenarios to fine-tune YOLO11 performance.

## How to Implement Crowd Density Estimation

### Step 1: Setup and Model Initialization

To get started, the code utilizes a pre-trained YOLO11 model for person detection. This model is loaded into the `CrowdDensityEstimation` class, which is designed to track individuals in a crowd and estimate crowd density in real time.

#### Code to Initialize and Track with YOLO11

```python
import cv2
from estimator import CrowdDensityEstimation

def main():
    estimator = CrowdDensityEstimation()  
    
    # Open video capture (0 for webcam, or video file path)
    cap = cv2.VideoCapture("path/to/video/file.mp4")
    
    # Get video properties for output
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('crowd-density-estimation.mp4', 
                          fourcc, fps, (frame_width, frame_height))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        processed_frame, density_info = estimator.process_frame(frame)
        estimator.display_output(processed_frame, density_info)  # Display
        out.write(processed_frame)  # Write output frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

This setup captures frames from a video source, processes them using YOLO11 to detect people, and calculates crowd density.

### Step 2: Real-Time Crowd Detection and Tracking

The core of the implementation relies on tracking individuals in each frame using the YOLO11 model and estimating the crowd density. This is achieved through a series of steps, which include detecting people, calculating density, and classifying the crowd level.

#### Code for Crowd Density Estimation

The main class `CrowdDensityEstimation` includes the following functionality:

- **Person Detection**: Using YOLO11 to detect individuals in each frame.
- **Density Calculation**: Based on the number of detected persons relative to the frame area.
- **Tracking**: Visualization of tracking history for each detected person.
  
```python
# Install ultralytics package
# pip install ultralytics

import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict

class CrowdDensityEstimation:
    def __init__(self, model_path='yolo11n.pt', conf_threshold=0.3):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.track_history = defaultdict(lambda: [])
        self.density_levels = {
            'Low': (0, 0.2), # 0-0.2 persons/m²
            'Medium': (0.2, 0.5), # 0.2-0.5 persons/m²
            'High': (0.5, 0.8), # 0.5-0.8 persons/m²
            'Very High': (0.8, float('inf')) # >0.8 persons/m²
        }

    def extract_tracks(self, im0):
        results = self.model.track(im0, persist=True, 
                                   conf=self.conf_threshold, 
                                   classes=[0])
        return results

    def calculate_density(self, results, frame_area):
        if not results or len(results) == 0:
            return 0, 'Low', 0

        person_count = len(results[0].boxes)
        density_value = person_count / frame_area * 10000  

        density_level = 'Low'
        for level, (min_val, max_val) in self.density_levels.items():
            if min_val <= density_value < max_val:
                density_level = level
                break
                
        return density_value, density_level, person_count
```

### Step 3: Visualizing Density and Results

Once density is calculated, the processed frame is annotated with information like density level, person count, and a tracking visualization. This enhances situational awareness by providing clear visual cues.

#### Displaying Density Information on Video Frames

```python
def display_output(self, im0, density_info):
    density_value, density_level, person_count = density_info

    cv2.rectangle(im0, (0, 0), (350, 150), (0, 0, 0), -1)
    
    cv2.putText(im0, f'Density Level: {density_level}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(im0, f'Person Count: {person_count}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(im0, f'Density Value: {density_value:.2f}', (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Crowd Density Estimation', im0)
```

## Applications of Crowd Density Estimation

1- **Public Safety** 

  - Early Warning System: Detecting unusual crowd formations.
  - Emergency Response: Identifying areas of high density for quick intervention.

2- **Event Management** 
  
  - Capacity Monitoring: Real-time tracking of crowd sizes in venues.
  - Safety Compliance: Ensuring attendance stays within safe limits.
  - Flow Analysis: Understanding movement patterns for better event planning.

3- **Urban Planning** 
  
  - Space Utilization: Analyzing how people use public spaces.
  - Infrastructure Planning: Designing facilities based on crowd patterns.

## Explore More

- [Contribute to Ultralytics Solutions](https://docs.ultralytics.com/solutions/)
- [Author's LinkedIn Post Discussion](https://www.linkedin.com/posts/ivan-apedo_ai-computervision-yolo11-activity-7266460747285602304-D_xR?utm_source=share&utm_medium=member_desktop)  
  
Unlock the potential of advanced crowd monitoring using YOLO11 and streamline operations for various sectors! 🚀
