from distutils.core import setup

setup(
    name='zinc',
    version='0.1.0',
    author='Eric Swanson',
    author_email='eswanson@alloscomp.com',
    packages=['zinc'],
    scripts=['bin/OrderTester.py'],
    url='http://pypi.python.org/pypi/Zinc/',
    license='LICENSE.txt',
    description='Wrapper for Zinc ecommerce API (zinc.io).',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
