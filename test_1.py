import pytest
import mediapipe
import cv2

@pytest.fixture
def input_value():
   input = 39
   return input

def test_with_input(input_value):
   assert input_value % 13 == 0
