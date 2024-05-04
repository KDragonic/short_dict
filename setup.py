from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='quick_dict',
  version='1.0.0',
  author='Dragonic',
  author_email='denkoropov@gmail.com',
  description='Модуль был создан для личного пользования, для более удобной работы с dict',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/KDragonic/short_dict',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='dict fun fast',
  project_urls={
    'Documentation': 'https://github.com/KDragonic/short_dict'
  },
  python_requires='>=3.10'
)