from distutils.core import setup

with open('README') as file:
    readme = file.read()

# NOTE: change the 'name' field below with some unique package name.
# then update the url field accordingly.

setup(
    name='benny_wargamepkg_private',
    version='2.0.0',
    packages=['wargame'],
    url='http://localhost:8081/simple',
    license='LICENSE.txt',
    description='test pkg private',
    long_description=readme,
    author='benny',
    author_email='1058619984@qq.com'
)

