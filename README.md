Script Created by :
1. Jonathan Richard (https://github.com/jonathanrichardl)
2. Ervin Halimsurya ()
Department of Electrical Engineering, University of Indonesia. 
# VideoCompression
This Repository contains a script for encoding and decoding of fully colored videos with User Interface, fully coded in Python. Encoding uses binary files so that the compression ratio is maximized. For studying purposes. 
## Packages used
All packages are obtaniable with pip:
1. Bitarray 
2. Pyqt5
3. Scipy
## Features
### Selectable Transform Methods
Users can select to use Discrete Cosine Transform, Discrete Sine Transform, and Discrete Fourier Transform. 
### Selectable Quantization Matrices
Users can select to use what kind of Quantization Matrix for each image component (Y and CbCr), whether its Chrominance matrix, or Luminance matrix. Users can also input their own custom Quantization Matrix. 
### Graphical User Interface
For the ease of use. Users can see the encoding and decoding progress. Also the UI can display the encoded file and the qunatized block. 
