from setuptools import setup

setup(
  name = 'text_reuse',
  version = '0.0.1',
  description = "A package used to identify reused test between two portions of text",
  url = 'https://github.com/ambro034/text_reuse.git',
  author_name = 'Graham W. Ambrose',
  license = 'unlicense',
  package = find_packages(),
  install_requires = ["pandas","IPython.display","re"]
)
  
