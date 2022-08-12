from setuptools import setup


def get_long_description():
    with open("README.md", "r") as file:
        long_description = file.read()
        return long_description


setup(
    name="MultiInstanceLinux",
    version="1.3.5",
    author="sathya-pramodh",
    author_email="sathyapramodh17@gmail.com",
    description="Multi Instance Macro Handler for Minecraft on Linux.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/sathya-pramodh/MultiInstanceLinux",
    project_urls={
        "Bug Tracker": "https://github.com/sathya-pramodh/MultiInstanceLinux/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    install_requires=["keyboard", "obs-websocket-py"],
    entry_points={
        "console_scripts": [
            "multiinstancelinux = MultiInstanceLinux.init:main",
        ]
    },
    package_data={
        "MultiInstanceLinux": ["src/MultiInstanceLinux/config/default_config.py"]
    },
)
