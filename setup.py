import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="terminal-chatbot",
    version="0.0.1",
    author="Zachary Whitehouse",
    author_email="zacharywhitehouse6@gmail.com",
    description=("Script that runs gemini in terminal"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liuzheng1990/python_packaging_demo",
    project_urls={
        "Bug Tracker": "https://github.com/liuzheng1990/python_packaging_demo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["google-generativeai", "python-dotenv"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "download = downloader.cli:main",
        ]
    }
)