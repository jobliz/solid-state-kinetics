from distutils.core import setup

setup(
    name='ssk',
    version='0.1',
    author='José Reyna',
    author_email='jose.reyna.rb@gmail.com',
    packages=['ssk', 'towelstuff.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/ssk/',
    license='LICENSE.txt',
    description='Solid State Kinetics toolbox.',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy >= 1.1.1",
        "scipy >= 0.13",
        "matplotlib >= 1.0"
    ],
)
