from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-lua',
    version=version,
    description="CKAN Plugins, in Lua",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Ross Jones',
    author_email='ross@servercode.co.uk',
    url='https://github.com/rossjones/ckanext-lua',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.lua'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lupa==0.21'
        # luajit
        # libluajit-5.1-dev
        # pkg-config
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        lua=ckanext.lua.plugin:LuaPlugin
    ''',
)
