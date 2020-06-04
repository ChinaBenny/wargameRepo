from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='benny-orcattack-game',
    version='2.1.1',
    packages=['wargame'],
    url='https://test.pypi.org/project/benny-orcattack-game/',
    license='LICENSE.txt',
    description='Benny coding the first fantasy game ',
    long_description=readme,
    author='Benny',
    author_email='1058619984@qq.com'

)


