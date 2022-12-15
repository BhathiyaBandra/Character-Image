# Character Image

This code is used to convert image pixels into charaters. Character opacity is changing based on the pixel value

1. Dependancies
   1. Need to install following library
      PIL

2. Work Method
   - Input the image file to *im*
   - Use *downsample_ratio* to reduce the output image resolution. 
   | ---------- | -------------- | --------------------- |
   | resolution | Original Image | Character Image       |
   | ---------- | -------------- | --------------------- |
   | Width      | x              | x*10/downsample_ratio |
   | Height     | y              | y*10/downsample_ratio |
   | ---------- | -------------- | --------------------- |

