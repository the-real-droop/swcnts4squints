from setuptools import setup, find_packages
import sys

#mainscript = 'swcnts4squints/swcnts4squints.py'

#major, minor1, minor2, s, tmp = sys.version_info
#if major==2 and minor1 < 7 or major < 2:
#    raise SystemExit("""cntapp requires Python 2.6 or later""")

extra_options = None

if sys.platform == 'darwin':
    mainscript = 'swcnts4squints/swcnts4squints.py'
    extra_options = dict(
        setup_requires=['py2app'],
        app=[mainscript],
        options=dict(py2app=dict(argv_emulation=True,
                                 includes=['sip',
                                           'PyQt4.QtCore',
                                           'PyQt4.QtGui'])),
    )
elif sys.platform == 'win32':
    mainscript = 'swcnts4squints/swcnts4squints.py'
    extra_options = dict(
        setup_requires=['py2exe'],
        #app=[mainscript],
        console=[mainscript],
        options={
            'py2exe': {
                "bundle_files": 1,
                "dll_excludes": [
                    "MSVCP90.dll",
                    "MSWSOCK.dll",
                    "mswsock.dll",
                    "powrprof.dll"],
                "includes": [
                    'sip',
                    'PyQt4.QtCore',
                    'PyQt4.QtGui'],
            },
        },
        data_files=[('phonon_backend',
              ['C:\Python27\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll'])]
    )
else:
    extra_options = {}
    #extra_options = dict(
    #        scripts=[mainscript],
    #        )

setup(name='swcnts4squints',
      version=0.5,
      description="python scripts",
      long_description="""\
              Simple app for calculating physical properties of carbon nanotubes""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python scripts',
      author='Andrew Merril',
      author_email='androomerrill@gmail.com',
      url='https://github.com/androomerrill/swcnts4squints',
      license='BSD 2-Clause',
      packages=find_packages(exclude=['docs', 'ez_setup', 'examples',
                                      'tests', 'symlinks']),
      include_package_data=True,
      exclude_package_data={'': ['README.md']},
      zip_safe=False,
      install_requires=['numpy', 'scipy'],
      entry_points={
          'gui_scripts': [
              'swcnts4squints = swcnts4squints.swcnts4squints:main',
              ]
      },
      **extra_options
)

