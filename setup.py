from setuptools import setup, find_packages


setup(name='Ryanair',
      version='1.0',
      description="Selenium",
      author='Tomasz Kraczka',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==7.1.1",
          "pytest-html==3.1.1",
          "selenium==4.1.2",
        ]
      )
