try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='py_lispnetworking',
      packages=['py_lispnetworking'],
      package_dir = {'py_lispnetworking': '.'},
      install_requires=['netifaces', 'scapy'],
      version='1.2',
      description='py_lispnetworking',
      long_description='''py-lispnetworking - A python module to deal with LISP control-plane packets''',
      zip_safe=True,
      )
