from setuptools import find_packages, setup
package_name = 'my_first_package'
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='me',
    maintainer_email='me@example.com',
    description='ROS2 study',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={'console_scripts': [
        'my_subscriber = my_first_package.my_subscriber:main',
        'my_publisher = my_first_package.my_publisher:main',
    ]},
)
