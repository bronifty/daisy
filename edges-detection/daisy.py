# Import pydaisi
import pydaisi as pyd

# Instantiate a Daisi object
edge_image_computation = pyd.Daisi("bronifty/Edge Image Computation")

# Call the endpoint of the compute_deriv() function
# and return the result immediately with the .value attribute
edge_image_computation.compute_deriv(image=None).value