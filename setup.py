from setuptools import setup, find_packages

setup(
    name='Myapp',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'numpy',
        'pandas',
        'gunicorn',
        'scikit-learn'
    ],
    author='Abhishek Jadhav',
    author_email='abhishekjadhav3470@gmail.com',
    description='Book Recommendation system',
    url='https://github.com/abhishekjadhav3470/Book_recommend_ML.git',
)
