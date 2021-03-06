# swapforth

[![Build Status](https://travis-ci.org/jamesbowman/swapforth.svg?branch=master)](https://travis-ci.org/jamesbowman/swapforth)

Swapforth is a cross-platform 16- and 32-bit ANS Forth.

Currently supported hosts are:

 * J1a - minimal 16-bit FPGA CPU with 8K of memory [Demo](http://www.excamera.com/sphinx/article-j1a-swapforth.html)
 * J1b - 32-bit FPGA CPU with 32K of memory
 * FT900 - 32-bit 100 MHz CPU with 256K flash, 64K RAM

Simulated hosts include:

 * Python in 16-, 32- and 64-bit big- and little-endian
 * J1a and J1b under Verilator
