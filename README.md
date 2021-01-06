# EZcompile_OpenSSL
A simple Python program that utliizes subprocess and os.system commands in order to automate the compilation of OpenSSL.

Preliminary requirements: gcc, make, python3 

Steps:
1. cd into /EZcompile_OpenSSL
2. wget a suitable version of OpenSSL in /EZcompile_OpenSSL
3. Run python3 EZcompile_Openssl.py

In order to resuse script without the need to reclone, 
run: rm -r OpenSSL/*
Then repeat the steps listed above.

Some issues have been found in regards to updating libs in an Ubuntu distro, I am still looking into that one.

