import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-disease-Classification-Project"
AUTHOR_USER_NAME = "vivek"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "vivekrauniyar18@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    usl = f"https://github.com/VivekRauniyar18/Chicken-disease-Classification-Project",
    project_urls={
        "Bug Tracker": f"https://github.com/VivekRauniyar18/Chicken-disease-Classification-Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


