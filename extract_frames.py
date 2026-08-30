"""
Extract frames from a video for dataset preparation.

This script reads a video frame by frame and saves each frame as a JPG image.
It is intended for building an image dataset before annotation and YOLO training.

Usage:
    python extract_frames.py --video path/to/video.mp4 --output data/frames
"""

import argparse
from pathlib import Path

import cv2


def extract_frames(video_path: Path, output_dir: Path) -> int:
    """Extract all frames from a video and save them as JPG files."""
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    video = cv2.VideoCapture(str(video_path))
    if not video.isOpened():
        raise RuntimeError(f"Could not open video: {video_path}")

    frame_count = 0

    while True:
        success, frame = video.read()
        if not success:
            break

        frame_path = output_dir / f"frame_{frame_count:04d}.jpg"

        saved = cv2.imwrite(str(frame_path), frame)
        if not saved:
            video.release()
            raise RuntimeError(f"Failed to save frame: {frame_path}")

        frame_count += 1

    video.release()

    print(f"Extraction completed.")
    print(f"Video: {video_path}")
    print(f"Output directory: {output_dir}")
    print(f"Total frames extracted: {frame_count}")

    return frame_count


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract video frames for object-detection dataset preparation."
    )

    parser.add_argument(
        "--video",
        type=Path,
        required=True,
        help="Path to the input video file.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/frames"),
        help="Directory where extracted frames will be saved.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    extract_frames(args.video, args.output)
