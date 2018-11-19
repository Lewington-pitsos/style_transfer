import unittest
import os
from transfer import process
from fastai.conv_learner import open_image
from pathlib import Path

class TestProcess(unittest.TestCase):
  def setUp(self):
    self.original_dir = os.getcwd()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
  
  def test_rand_crop_crops_to_correct_size(self):
    img_path = Path("data/style/don-kenn-3.jpg")
    img = open_image(img_path)

    h, w, _ = img.shape

    self.assertTrue(h > 285)
    self.assertTrue(w > 220)

    cropped_img = process.rand_crop(img, 285, 220)

    cropped_h, cropped_w, _ = cropped_img.shape

    self.assertEqual(285, cropped_h)
    self.assertEqual(220, cropped_w)
  
  def test_correct_all_crops_crops(self):
    img_path = Path("data/style/don-kenn-2.jpg")
    img = open_image(img_path)

    h, w, _ = img.shape 

    self.assertEqual(h, 360)
    self.assertEqual(w, 605)

    crops = process.all_crops(img, 285, 220)

    self.assertEqual(6, len(crops))

    for crop in crops:
      print(crop.shape)
      self.assertEqual(285, crop.shape[0])
      self.assertEqual(220, crop.shape[1])

  def tearDown(self):
    os.chdir(self.original_dir)

if __name__ == '__main__':
    unittest.main()
