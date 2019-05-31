import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='Stock Market Analyzer',
     version='0.1',
     scripts=['scrap_stocks_tr.py', 'market_analyzer_tr.py'] ,
     author="Sina Sen",
     author_email="sinasen2000@hotmail.com",
     description="A tool to scrap and analtze stock market data",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/sinasen2000/StockAverage",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )