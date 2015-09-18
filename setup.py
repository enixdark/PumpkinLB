from setuptools import setup

try:
    with open('README.rst', 'rt') as f:
        long_description = f.read()
except:
    long_description = "See README"

setup(name='PumpkinLB',
        version='1.4',
        scripts=['PumpkinLB.py'],
        packages=['pumpkinlb'],
        author='Tim Savannah',
        author_email='kata198@gmail.com',
        maintainer='Tim Savannah',
        maintainer_email='kata198@gmail.com',
        provides=['PumpkinLB'],
        description='A simple, fast, pure-python load balancer',
        url='https://github.com/kata198/PumpkinLB',
        long_description=long_description,
        license='GPLv3',
        keywords=['load balancer', 'load balance', 'python', 'balance', 'lb', 'http', 'socket', 'port', 'forward', 'tcp', 'fast', 'server', 'network'],
        classifiers=['Development Status :: 4 - Beta',
                     'Programming Language :: Python',
                     'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                     'Programming Language :: Python :: 2',
                      'Programming Language :: Python :: 2.7',
                     'Topic :: Internet',
                     'Topic :: Internet :: WWW/HTTP',
                     'Topic :: System :: Distributed Computing',
                     'Topic :: System :: Networking',
        ]
)
