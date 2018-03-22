# http://python-packaging.readthedocs.io/en/latest/minimal.html
# Help from: http://www.scotttorborg.com/python-packaging/minimal.html
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
import os
from os import path
from setuptools import setup, find_packages
import rstcheck


mypackage_root_dir = 'curlnagios'

# function to check a readme file
def check_readme(file='README.rst'):
    """
    Checks readme rst file, to ensure it will upload to pypi and be formatted
    correctly.
    :param file:
    :return:
    """
    # Get the long description from the relevant file
    with open(file, encoding='utf-8') as f_object:
        readme_content = f_object.read()

    errors = list(rstcheck.check(readme_content))
    if errors:
        msg = 'There_path are errors in {}, errors \n {}'.format(file,
                                                            errors[0].message)
        raise SystemExit(msg)
    else:
        msg = 'No errors in {}'.format(file)
        print(msg)

# Get requirements for this package
here_path = path.abspath(path.dirname(__file__))
with open(os.path.join(here_path, 'requirements.txt')) as f:
    requires = [x.strip() for x in f if x.strip()]

# Get the version from VERSION file
with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
    version = version_file.read().strip()

readme_path = path.join(here_path, 'README.rst')
# Get the long description from the relevant file
with open(readme_path, encoding='utf-8') as f:
    long_description = f.read()

# Check the readme
# when checking rst file you ensure it will be healthy to publish on pypi.org
check_readme(readme_path)

# Define setuptools specifications
setup(name='curlnagios',
      version=version,
      description='curl check_http nagios plugin',
      long_description=long_description,  # this is the file README.rst
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: System :: Monitoring',
      ],
      url='https://github.com/pablodav/curlnagios',
      author='Pablo Estigarribia',
      author_email='pablodav@gmail.com',
      license='MIT', # Choose your license
      # http://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
      packages=find_packages(),
      include_package_data=True,
      # use package_data if you want to include more files in the package
      #package_data={
      #    'data': 'src/data/*',  
      #},
      data_files=[('VERSION', ['{}/VERSION'.format(mypackage_root_dir)])],
      entry_points={
          'console_scripts': [
              # http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
              'curlnagios = curlnagios.__main__:main'
          ]
      },
      install_requires=requires, # we have already readed requirements.txt in line 30
      # Use test_require  to add pytest requirements when using unit tests
      #tests_require=['pytest',
      #               'pytest-cov'],
      zip_safe=False)
