#!/usr/bin/env python



# receursively find the receptive field, r, of a convolutional network at layer m. gives the receptive field corresponding to convolution only along one dimension


# recursively find product of strides up to the desired layer number m
def findStridesProduct(m, strides):
    if m == 1:
        return 1
    else:
        return strides[m-1] * findStridesProduct(m-1, strides)

# find receptive field starting at m and receurse to m=0 (tail recursive)
# kernels is list of size of each kernel, strides is list of strides used by each kernel
def findReceptiveField(m, kernels, strides):
    if m == 0:  # the receptive field of the input to the convolution
        return 1
    else:
        # at each recursion you recalculate the strides product.
        # it would be better to recursively precalculate the product at each layer beforehand to skip re-computing the same products
        strides_product = findStridesProduct(m, strides)
        return findRecptiveField(m-1, kernels, strides) + (kernels[m] - 1) * strides_product


# strides is a list with strides[m] corresponding to stride used for convolutional layer m. strides[0] should be 0 or 1 (since no convolution has yet been applied), although the function will never access the 0 index anyway (indexing by m for simplicity/readability)


# VGG-16 architecture hardcoded as an example:
kernels = list(3, 3, 2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2)
strides = list(1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2)
receptive = list()
for i in range(len(kernels)):
    # rewrite findReceptiveField so that it stores every receptive field up to and including the one you want
    receptive[i] = findReceptiveField(i, kernels, strides) 

for i in range(len(kernels)):
    print("layer %d :" % i)
    print("\t kernel size: %s \n \t kernel stride: %s \n \t receptive field size: %s \n" % (kernels[i], strides[i], receptive[i]))
