---
comments: true
description: Discover how to achieve advanced items segmentation in supermarkets with Ultralytics YOLO11 for efficient object detection and analysis.
keywords: items segmentation, supermarket object detection, YOLO11, Ultralytics YOLO11, AI segmentation, retail analytics, object detection in retail, real-time segmentation, computer vision, custom dataset, advanced image processing
---

# Revolutionizing Supermarkets: Items Segmentation and Counting with Ultralytics YOLO11 ❤️‍🔥

Discover how to leverage the power of [Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11/) to achieve precise object segmentation and counting. In this guide, you'll learn step-by-step how to use YOLO11 to streamline processes, enhance accuracy, and unlock new possibilities in computer vision applications.

<div class="embed-container">
  <iframe src="https://drive.google.com/file/d/1BbvRy8w-vTsmfYi82j97-rYE1q-KS6Pe/preview" 
          allow="autoplay">
  </iframe>
</div>

## System Specifications Used to Create This Demo

- **CPU**: Intel® Core™ i5-10400 CPU @ 2.90GHz for optimal performance.
- **GPU**: NVIDIA RTX 3050 for real-time processing.
- **RAM & Storage**: 64 GB RAM and 1 TB SSD for large datasets.
- **Model**: Fine-tuned YOLO11 for items segmentation in trolley.
- **Dataset**: Custom-labeled supermarket images.

## How to Perform Items Segmentation and Counting

### Step 1: Train or Fine-Tune YOLO11

To get started, you can train the YOLO11 model on a custom dataset tailored to your specific use case. However, if the pre-trained YOLO11 model already performs well for your application, there's no need for customization, you can directly use the pre-trained weights for faster and efficient deployment. Explore the full details in the [Ultralytics Documentation](https://docs.ultralytics.com/tasks/segment/).

### Step 2: How to draw the segmentation masks


```{.py annotate}
# Install ultralytics package
# pip install ultralytics

import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
from collections import Counter

model = YOLO(model="path/to/model/file.pt")
cap = cv2.VideoCapture("path/to/video/file.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,
                                       cv2.CAP_PROP_FRAME_HEIGHT,
                                       cv2.CAP_PROP_FPS))

vwriter = cv2.VideoWriter("instance-segmentation4.avi",
                          cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))
while True:
    ret, im0 = cap.read()
    if not ret:
        break

    object_counts = Counter()  # Initialize a counter for objects detected
    results = model.track(im0, persist=True)
    annotator = Annotator(im0, line_width=3)

    if results[0].boxes.id is not None and results[0].masks is not None:
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().cpu().tolist()
        clss = results[0].boxes.cls.cpu().tolist()
        boxes = results[0].boxes.xyxy.cpu()
        for mask, box, cls, t_id in zip(masks, boxes, clss, track_ids):
            if mask.size>0:
                object_counts[model.names[int(cls)]] += 1
                color = colors(t_id, True)
                mask_img = im0.copy()
                cv2.fillPoly(mask_img, [mask.astype(int)], color)
                cv2.addWeighted(mask_img, 0.7, im0, 1 - 0.7, 0, im0)
                annotator.seg_bbox(mask=mask, mask_color=color,
                                   label=str(model.names[int(cls)]),
                                   txt_color=annotator.get_txt_color(color))

    vwriter.write(im0)
    cv2.imshow("Ultralytics FastSAM", im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vwriter.release()
cap.release()
cv2.destroyAllWindows()
```

<figure>
    <img width="1920" src="https://github.com/user-attachments/assets/2f28cb0a-47d4-45c1-a86e-1db50605b12a" alt="Image Segmentation with YOLO11">
    <figcaption>Fig-1: Image segmentation using YOLO11.</figcaption>
</figure>

### Step 3: Count Segmented Objects

Now, we have already drawn the object masks, we can now count the objects.

```python
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
from collections import Counter

model = YOLO(model="path/to/model/file.pt")
cap = cv2.VideoCapture("path/to/video/file.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,
                                       cv2.CAP_PROP_FRAME_HEIGHT,
                                       cv2.CAP_PROP_FPS))

vwriter = cv2.VideoWriter("instance-segmentation4.avi",
                          cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))
while True:
    ret, im0 = cap.read()
    if not ret:
        break

    object_counts = Counter()  # Initialize a counter for objects detected
    results = model.track(im0, persist=True)
    annotator = Annotator(im0, line_width=3)

    if results[0].boxes.id is not None and results[0].masks is not None:
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().cpu().tolist()
        clss = results[0].boxes.cls.cpu().tolist()
        boxes = results[0].boxes.xyxy.cpu()
        for mask, box, cls, t_id in zip(masks, boxes, clss, track_ids):
            if mask.size>0:
                object_counts[model.names[int(cls)]] += 1
                color = colors(t_id, True)
                mask_img = im0.copy()
                cv2.fillPoly(mask_img, [mask.astype(int)], color)
                cv2.addWeighted(mask_img, 0.7, im0, 1 - 0.7, 0, im0)
                annotator.seg_bbox(mask=mask, mask_color=color,
                                   label=str(model.names[int(cls)]),
                                   txt_color=annotator.get_txt_color(color))

    # Display total counts in the top-right corner
    x, y = im0.shape[1] - 200, 30
    margin = 10

    for i, (label, count) in enumerate(object_counts.items()):
        text = f"{label}={count}"
        font_scale = 1.4
        font_thickness = 4
        padding = 15
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX,
                                       font_scale, font_thickness)
        rect_x2 = im0.shape[1] - 10
        rect_x1 = rect_x2 - (text_size[0] + padding * 2)

        y_position = y + i * (text_size[1] + padding * 2 + 10)
        if y_position + text_size[1] + padding * 2 > im0.shape[0]:
            break
        rect_y1 = y_position
        rect_y2 = rect_y1 + text_size[1] + padding * 2
        cv2.rectangle(im0, (rect_x1, rect_y1), (rect_x2, rect_y2),
                      (255, 255, 255), -1)
        text_x = rect_x1 + padding
        text_y = rect_y1 + padding + text_size[1]
        cv2.putText(im0, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX,
                    font_scale, (104, 31, 17), font_thickness)

    vwriter.write(im0)
    cv2.imshow("Ultralytics FastSAM", im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vwriter.release()
cap.release()
cv2.destroyAllWindows()
```

<figure>
    <img width="1920" src="https://github.com/user-attachments/assets/c5c11037-e61e-4816-9423-216ca67576c0" alt="Object Counting in Shopping Trolley using YOLO11.">
    <figcaption>Fig-2: <a href="../../count/">Object Counting</a> in Shopping Trolley using YOLO11.</figcaption>
</figure>

## Applications in Retail

- **Smart Inventory Management**: Categorize items and track movement effortlessly.
- **Retail Analytics**: Gain insights into customer behavior and product popularity.

## Explore More

- [Join the Discussion on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7265303716050698240)  

Transform your retail operations with YOLO11 today! 🚀
