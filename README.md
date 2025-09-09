### Computer Vision Projects

[![Deployment](https://github.com/RizwanMunawar/visionusecases/actions/workflows/deploy.yml/badge.svg)](https://github.com/RizwanMunawar/visionusecases/actions/workflows/deploy.yml)
[![Explore projects](https://img.shields.io/badge/Explore-projects-blue)](https://img.shields.io/badge/explore-projects-blue)

Welcome to a collection of hands-on computer vision projects that demonstrate how AI can see and understand the world around us. From object detection and tracking to image segmentation, pose estimation, and automated annotation, these projects cover the core techniques powering modern vision systems.

Whether you’re working on retail automation, traffic monitoring, agriculture analytics, manufacturing quality control, or wildlife research, you’ll find practical examples here built with Ultralytics YOLO models i.e. [Ultralytics YOLOv8](https://docs.ultralytics.com/models/yolov8/) and [YOLO11](https://docs.ultralytics.com/models/yolo11/) and advanced tools like [Segment Anything Model 2 (SAM 2)](https://docs.ultralytics.com/models/sam-2/). Each project includes code and documentation so you can learn, adapt, and apply these methods to your own real-world applications.

| Project name                                                                                                                                |                     Code                     | Docs | Description                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------:|:----:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Apple Counting on Conveyor Belt](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/apple-counting.md)                |      [Code](docs/usecases/apple-counting.md)      |  ✅   | Perform real-time apple counting on conveyor belts using Ultralytics YOLO11. Ideal for automated quality control and inventory management in food processing and packaging industries. |
| [Birds Tracking in Air](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/bird-tracking.md)                           |      [Code](docs/usecases/bird-tracking.md)       |  ✅   | Track multiple birds in flight using advanced YOLO object tracking models to study migration patterns, monitor wildlife behavior, or enhance aviation safety.                          |
| [Bread Counting in Baking Area on Conveyor Belt](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/bread-counting.md) |      [Code](docs/usecases/bread-counting.md)      |  ✅   | Implement real-time bread counting during baking and packaging with YOLO-based systems, optimizing production lines and reducing manual labor.                                         |
| [Crowd Density Estimation](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/crowd-density-estimation.md)             | [Code](docs/usecases/crowd-density-estimation.md) |  ✅   | Estimate crowd density in public areas using computer vision and YOLO detection to improve event management, security, and space utilization.                                          |
| [Items Counting in Shopping Trolley](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/items-counting.md)             |      [Code](docs/usecases/items-counting.md)      |  ✅   | Automatically count retail items in shopping trolleys for self-checkout automation, retail analytics, and loss prevention using YOLO models.                                           |
| [Items Segmentation in Supermarket](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/items-segmentation.md)          |    [Code](docs/usecases/items-segmentation.md)    |  ✅   | Perform item segmentation in supermarkets using YOLO’s instance segmentation for real-time shelf monitoring, inventory tracking, and product placement insights.                       |
| [Auto Annotation using SAM 2](https://github.com/RizwanMunawar/visionusecases/blob/main/docs/usecases/sam2-auto-annotation.md)              |   [Code](docs/usecases/sam2-auto-annotation.md)   |  ✅   | Speed up dataset preparation by leveraging Segment Anything Model 2 (SAM2) for automated annotation in retail, manufacturing, and research computer vision workflows.                  |

### How to Contribute

1- Ensure your use case is computer vision-based. It can belong to any computer vision task no restrictions!

2- For better user experience, upload a video of your implementation to YouTube and attach the URL for the community to watch. This step is optional, but highly encouraged!

3- Create a documentation page for your use case.
- Include implementation details such as hardware configuration, model usage, code with step by step explanation and advantages.
- Place the file in the `usecases` folder.

4- Update the mkdocs.yml file: Add the relevant path under the nav section to make your docs accessible.

**Final Step:** Once all the changes are done, open the PR and If everything will look good, I will merge your PR!
