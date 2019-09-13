# Sobel-Edge-Detection

Objective:

The objective of this task is to detect edges along the x and y -axis in the given image using
Sobel operator.

Approach:

I am using two 3x3 kernels which are convolved with the image to respond to edges running
vertically and horizontally changes relative to the pixel grid. Both the kernels are move in the
two perpendicular directions. Each is applied separately to get the edges in vertical and
horizontal directions.

where * here denotes the 2-dimensional convolution operation.

A is the source image

Gx and Gy are two images which at each point contain the horizontal and vertical
derivative approximations respectively

These can then be combined together to calculate an approximation of the gradient at each
point and is combined.

