from setuptools import setup
from setuptools import find_packages
import os

version = '0.2'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (read('README.txt')
                    + '\n' +
                    read('js', 'forkit', 'test_forkit.js.txt')
                    + '\n' +
                    read('CHANGES.txt'))

setup(name='js.forkit',
      version=version,
      description="Fanstatic packaging of forkit.js",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Andreas Kaiser',
      author_email='disko@binary-punks.com',
      url='https://github.com/disko/js.forkit/',
      license='BSD',
      packages=find_packages(),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['fanstatic',
                        'setuptools', ],
      entry_points={'fanstatic.libraries': ['forkit.js = js.forkit:library', ], },)
