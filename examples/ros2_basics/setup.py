from setuptools import setup

package_name = 'ros2_basics'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ROS 2 Hands-on readers',
    maintainer_email='maintainers@example.invalid',
    description='Generic ROS 2 Humble Python examples; not an R2 driver.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'talker = ros2_basics.talker:main',
            'listener = ros2_basics.listener:main',
        ],
    },
)
