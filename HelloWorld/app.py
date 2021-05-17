# import ecommerce.shipping  # import entire module
from pathlib import Path  # import specific class or function

path = Path()
for file in path.glob('*'):
    print(file)
