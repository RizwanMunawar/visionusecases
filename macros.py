def define_env(env):
    # Object Detection Section
    @env.macro
    def object_detection_section():
        return '''
## Object Detection | Advanced Applications

Object detection is a pivotal computer vision technique that identifies and locates objects in images or videos. It integrates classification and localization to recognize object types and mark positions using bounding boxes. Common applications include autonomous driving, surveillance, and industrial automation.

Explore key object detection projects we’ve implemented, complete with technical insights:

- **Waste Detection: 🚀** Discover how cutting-edge object detection models like Ultralytics YOLO11 or YOLOv9 revolutionize waste detection for enhanced efficiency.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/VhzkygLZido)

- **Industrial Package Identification: 📦** Learn how to accurately detect packages in industrial settings using advanced models like Ultralytics YOLO11, YOLOv10, or Ultralytics YOLOv8.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/KGyP10JOwvw)
        '''

    # Object Tracking Section
    @env.macro
    def object_tracking_section():
        return '''
## Object Tracking | Monitoring Movement

Object tracking monitors object movement across video frames. Starting with detection in the first frame, it tracks positions and interactions in subsequent frames. Common applications include surveillance, traffic monitoring, and sports analysis.

Explore our object tracking projects, showcasing technical depth and practical applications:

- **Vehicle Tracking: 🚗** Learn how to track vehicles with high accuracy using YOLOv10, YOLOv9, or YOLOv8, revolutionizing traffic monitoring and fleet management.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/gUMvcrFeVUg)
        '''

    # Pose Estimation Section
    @env.macro
    def pose_estimation_section():
        return '''
## Pose Estimation | Key Point Analysis

Pose estimation predicts spatial positions of key points on objects or humans, enabling machines to interpret dynamics. This technique can be used in sports analysis, healthcare, and animation.

Uncover our pose estimation projects with practical applications:

- **Dog Pose Estimation: 🐾** Learn how to estimate dog poses using Ultralytics YOLO11, unlocking new possibilities in animal behavior analysis.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/PmiWQgdTAuA)
        '''

    # Object Counting Section
    @env.macro
    def object_counting_section():
        return '''
## Object Counting | Automation at Scale

Object counting identifies and tallies objects in images or videos. Leveraging detection or segmentation techniques, it’s widely used in industrial automation, inventory tracking, and crowd management.

Explore our object counting projects, complete with practical applications:

- **Apples Counting on Conveyor Belt: 🍎** Learn how to count apples with precision using Ultralytics YOLO models for better inventory management.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/g5Onls24Djg)

- **Items Counting in Shopping Trolley: 🛒** See how we track and count items in shopping trolleys with cutting-edge detection models, streamlining retail operations.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/eoOkYDJIDHo)

- **Bread Counting on Conveyor Belt: 🍞** Discover how to ensure accurate bread counts on conveyor belts with Ultralytics YOLO models, boosting production efficiency.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/1qyxTP2U_Ow)
        '''

    # Instance Segmentation Section
    @env.macro
    def instance_segmentation_section():
        return '''
## Image Segmentation | Precise Pixel-Level Analysis

Image segmentation divides an image into meaningful regions to identify objects or areas of interest. Unlike object detection, it provides a precise outline of objects by labeling individual pixels. This technique is widely used in medical imaging, autonomous vehicles, and scene understanding.

Delve into our instance segmentation projects, featuring technical details and real-world applications:

- **Brain Scan Segmentation: 🧠** Learn how to segment brain scans with precision using models like Ultralytics YOLO11 or YOLOv8, revolutionizing medical imaging analysis.  
  [![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue?style=flat-square "Watch the Demo Video")](https://youtu.be/9F0fry__HPE)
        '''
