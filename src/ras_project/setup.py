from setuptools import setup

package_name = 'ras_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eetu',
    maintainer_email='rantala.eetu@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'tello_controller = ras_project.tello_controller:main',
                'dance_subscriber = ras_project.dance_subscriber:main',
        ],
    },
)
