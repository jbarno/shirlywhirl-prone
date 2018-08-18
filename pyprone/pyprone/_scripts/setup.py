from setuptools import setup

setup(
    name='getter',
    version='0.1',
    py_modules=['scripts'],
    install_requires=[
        'Click',
        'facebook-sdk',
    ],
    entry_points='''
        [console_scripts]
        getter=scripts.getter:get_from
    ''',
)