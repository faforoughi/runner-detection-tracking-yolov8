# Runner Detection and Tracking with YOLOv8 & ByteTrack

An end-to-end computer vision project for detecting and tracking runners in a race scene using **YOLOv8** for object detection and **ByteTrack** for multi-object tracking.

The project covers the complete pipeline from video frame extraction and dataset preparation to model training, evaluation, and runner tracking across video frames.

## Project Overview

The objective of this project is to detect and track runners in a crowded race scene extracted from the Iranian film *Children of Heaven*.

Frames were extracted from the source video and prepared as an object detection dataset with a single target class:

- `runner/person`

A YOLOv8 model was fine-tuned on the custom dataset, and ByteTrack was subsequently used to maintain runner identities across consecutive video frames.

## Pipeline

```text
Source Video
    ↓
Frame Extraction
    ↓
Dataset Preparation & Annotation
    ↓
YOLOv8 Training
    ↓
Model Evaluation
    ↓
Runner Detection
    ↓
ByteTrack Multi-Object Tracking
    ↓
Tracked Output Video

## Results

The following examples demonstrate runner detection and multi-object tracking using YOLOv8 and ByteTrack. Bounding boxes, tracking IDs, and confidence scores are displayed for detected targets across different race scenes.

### Sample Tracking Results

<p align="center">
  <img src="assets/result_1.png" width="800">
</p>

<p align="center">
  <img src="assets/result_2.png" width="800">
</p>
