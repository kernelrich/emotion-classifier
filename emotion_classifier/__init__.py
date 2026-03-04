"""
Emotion Classifier Package
A text emotion classification system using DistilBERT and Flask API
"""

__version__ = "1.0.0"
__author__ = "kernelrich"

from .classifier import EmotionClassifier

__all__ = ["EmotionClassifier"]