import setuptools
from base_provider.version import Version


setuptools.setup(name='baseProvider',
                 version=Version('0.0.1').number,
                 description='Base for DBaaS providers',
                 long_description=open('README.md').read().strip(),
                 author='DBaaS Team',
                 author_email='db@g.globo',
                 url='',
                 py_modules=['provider_utils'],
                 install_requires=[],
                 license='BSD 3-Clause License',
                 zip_safe=False,
                 keywords='dbaas',
                 classifiers=['Packages', 'DBaaS'])
