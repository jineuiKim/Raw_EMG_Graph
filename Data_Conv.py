import spacepy.pycdf as pycdf

# Open the CDF file
cdf_file = pycdf.CDF('t1.cdf')

# Get a list of global attributes
global_attrs = cdf_file.attrs.keys()

# Get a list of variable names
variable_names = cdf_file.varnames

print(varaible_names)