# Linear-regression
This model has several versions.

The last version has one problem. Only reliable points and degree gives reliable results. 

I think i know why. Since my model computes the gradient of each degree, then updates them all.
This is why there is no problem at the first degree and 70 percent the second and 30 the third ...

I will try to compute the gradient and update it simultaneously for every degree.
Hope this will make a difference. 

unfortunately. it didn't.

