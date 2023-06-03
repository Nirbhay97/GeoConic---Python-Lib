from setuptools import setup

setup(
    name='GeoConic',
    version=0.1,
    description='Conic section mathematics and higher functions',
    author='Nirbhay Kumar',
    install_requires=[],
    platforms=['any'],
    packages=['GeoConic'],
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    )
    
# python setup.py bdist_wheel
# python -i __init__.py // tp get into the file you want to run and test