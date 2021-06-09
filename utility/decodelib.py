import argparse
import math
import numpy as np
from .utils import *
from scipy import fftpack
from bitarray import bitarray,util

class JPEGFileReader:
    TABLE_SIZE_BITS = 16
    BLOCKS_COUNT_BITS = 32

    DC_CODE_LENGTH_BITS = 4
    CATEGORY_BITS = 4

    AC_CODE_LENGTH_BITS = 8
    RUN_LENGTH_BITS = 4
    SIZE_BITS = 4

    def __init__(self, bytes,table):
        self.codes = bitarray()
        self.codes.frombytes(bytes)
        self.__table = table
        self.currentIndex = 0

    def read_int(self, size):
        if size == 0:
            self.skipindex()
            return 0
        bin_num = bitarray()
        for i in range(int(size)):
            #print("index" + str(self.currentIndex) + "\tvalue  :  "+str(self.codes[self.currentIndex]))
            bin_num.append(self.codes[self.currentIndex])
            self.currentIndex += 1
        if len(bin_num) == 0:
            self.skipindex()
            return 0
        #print('extractvalue')
        if bin_num[0]:
            #print(util.ba2int(bin_num))
            return util.ba2int(bin_num)
        else:
            bin_num.invert()
            #print(util.ba2int(bin_num))
            return util.ba2int(bin_num) * -1
    
    def imagesize(self):
        cols,rows,frame_num,fps = self.__table.readline().replace('\n','').split(',')
        return cols,rows,frame_num,fps

    def read_dc_table(self):
        table = dict()
        table_size = self.__table.readline().replace('\n','')
        for _ in range(int(table_size)):
            category = self.__table.readline().replace('\n','')
            code = self.__table.readline().replace('\n','')
            table[code] = category
        return table

    def read_ac_table(self):
        table = dict()

        table_size = self.__table.readline()
        for _ in range(int(table_size)):
            a = self.__table.readline().replace('\n','')
            [run_length,size] = a.split(',')
            code = self.__table.readline().replace('\n','')
            table[code] = (run_length, size)
        return table

    def read_blocks_count(self):
        self.currentIndex += 32
        return util.ba2int(self.codes[0:32])
    def skipindex(self):
        self.currentIndex +=1 

    def read_huffman_code(self, table):
        prefix = bitarray()
        while prefix.to01() not in table:
            #print("index" + str(self.currentIndex) + "\tvalue  :  "+str(self.codes[self.currentIndex]))
            prefix.append(self.codes[self.currentIndex])
            self.currentIndex += 1
            
        #print('extractvalue')
        return table[prefix.to01()]

    def __read_uint(self, size):
        if size <= 0:
            raise ValueError("size of unsigned int should be greater than 0")
        return self.__int2(self.__read_str(size))

    def __read_str(self, length):
        return self.__file.read(length)

    def __read_char(self):
        return self.__read_str(1)

    def __int2(self, bin_num):
        return int(bin_num, 2)

def loadcustomTable(method,table):
    lum = np.array([[2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 4, 5, 7, 9],
                      [2, 2, 2, 4, 5, 7, 9, 12],
                      [3, 3, 4, 5, 8, 10, 12, 12],
                      [4, 4, 5, 7, 10, 12, 12, 12],
                      [5, 5, 7, 9, 12, 12, 12, 12],
                      [6, 6, 9, 12, 12, 12, 12, 12]])
    chrom = np.array([[3, 3, 5, 9, 13, 15, 15, 15],
                      [3, 4, 6, 11, 14, 12, 12, 12],
                      [5, 6, 9, 14, 12, 12, 12, 12],
                      [9, 11, 14, 12, 12, 12, 12, 12],
                      [13, 14, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12]])
    if method == 4:
       return lum,table
    elif method ==5:
        return chrom,table
    elif method ==6:
        return table,lum
    elif method ==7:
        return table,chrom
    elif method ==8:
        return table,table


def loadquantize(method):
    lum = np.array([[2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 4, 5, 7, 9],
                      [2, 2, 2, 4, 5, 7, 9, 12],
                      [3, 3, 4, 5, 8, 10, 12, 12],
                      [4, 4, 5, 7, 10, 12, 12, 12],
                      [5, 5, 7, 9, 12, 12, 12, 12],
                      [6, 6, 9, 12, 12, 12, 12, 12]])
    chrom = np.array([[3, 3, 5, 9, 13, 15, 15, 15],
                      [3, 4, 6, 11, 14, 12, 12, 12],
                      [5, 6, 9, 14, 12, 12, 12, 12],
                      [9, 11, 14, 12, 12, 12, 12, 12],
                      [13, 14, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12]])
    if method == 0:
       return chrom,chrom
    elif method ==1:
        return lum,chrom
    elif method ==2:
        return chrom,lum
    elif method ==3:
        return lum,lum


def read_image_file(bytes,tablepath):
    reader = JPEGFileReader(bytes,tablepath)
    tables = dict()
    rows,cols,frame_num,fps = reader.imagesize()
    for table_name in ['dc_y', 'ac_y', 'dc_c', 'ac_c']:
        if 'dc' in table_name:
            tables[table_name] = reader.read_dc_table()
        else:
            tables[table_name] = reader.read_ac_table()
    blocks_count = int(reader.read_blocks_count())
    dc = np.empty((blocks_count, 3), dtype=np.int32)
    ac = np.empty((blocks_count, 63, 3), dtype=np.int32)

    for block_index in range(blocks_count):
        for component in range(3):
            #print("dc "+ str(block_index)+","+str(component))
            dc_table = tables['dc_y'] if component == 0 else tables['dc_c']
            ac_table = tables['ac_y'] if component == 0 else tables['ac_c']
            category = reader.read_huffman_code(dc_table)
            #print(category)
            dc[block_index, component] = reader.read_int(category)
            #print(dc[block_index,component])
            cells_count = 0   
            # TODO: try to make reading AC coefficients better
            while cells_count < 63:
                run_length, size = reader.read_huffman_code(ac_table)
                #print(run_length +"," +size)
                run_length = int(run_length)
                size = int(size)
                if (run_length, size) == (0, 0):
                    while cells_count < 63:
                        ac[block_index, cells_count, component] = 0
                        cells_count += 1
                    reader.skipindex()
                    break
                elif run_length == 0 & size != 0:
                    value = reader.read_int(size)
                    ac[block_index, cells_count, component] = value
                    cells_count += 1
                    
                else:
                    for i in range(run_length):
                        ac[block_index, cells_count, component] = 0
                        cells_count+=1
                    value = reader.read_int(size)
                    ac[block_index, cells_count, component] = value
                    cells_count += 1

    return rows,cols,frame_num,dc, ac, tables, blocks_count


def zigzag_to_block(block):
    b = np.zeros((8,8),dtype = int)
    a = np.array([[ 0,1,5,6,14,15,27,28],
                  [ 2 ,4,7,13,16,26,29,42],
                  [ 3 , 8, 12 ,17 ,25, 30, 41, 43],
                  [ 9 ,11, 18 ,24, 31 ,40, 44, 53],
                  [10 ,19 ,23, 32 ,39 ,45, 52, 54],
                  [20 ,22 ,33, 38, 46, 51, 55, 60],
                  [21, 34, 37 ,47 ,50, 56 ,59 ,61],
                  [35, 36, 48 ,49, 57 ,58,62 ,63]])
    for i in range(8):
        for j in range(8):
            b[i,j] = block[a[i,j]]
            
    return b

def idct_2d(image):
    return fftpack.idct(fftpack.idct(image.T, norm='ortho').T, norm='ortho')

def idst_2d(image):
    return fftpack.idst(fftpack.idst(image.T, norm='ortho').T, norm='ortho')

def idft_2d(image):
    return fftpack.irfft(fftpack.irfft(image.T, axis=0),axis=1)

def getDimension(tablepath):
    with open(tablepath,'r') as file:
        rows,cols,frame_num,fps = file.readline().replace('\n','').split(',')
    return rows,cols,frame_num,fps

def decode(bytes,table,type, quantizationMethod, custom = None):
    rows,cols,frame_num, dc, ac, tables, blocks_count= read_image_file(bytes,table)
    block_side = 8
    rows = int(rows)
    cols = int(cols)
    npmat = np.empty((cols, rows, 3), dtype=np.uint8)
    cols = int(rows/8)
    block_index = 0
    if quantizationMethod <=3:
        y,cbcr = loadquantize(quantizationMethod)
    else:
        y,cbcr = loadcustomTable(quantizationMethod,custom)  
    # j antara 1-160
    # i antara 1-90
    for block_index in range(blocks_count):
        #print("index : " + str(block_index))
        i = block_index // cols * 8
        j = block_index % cols * 8
        #print("i = " + str(i))
        #print("j = " + str(j))
        for c in range(3):
            zigzag = [dc[block_index, c]] + list(ac[block_index, :, c])
            quant_matrix = zigzag_to_block(zigzag)
            if c == 0:
                matrix = quant_matrix * y
            else:
                matrix = quant_matrix * cbcr
            if type ==0:
                block = idct_2d(matrix)
            if type ==1:
                block = idft_2d(matrix)
            if type ==2:
                block = idst_2d(matrix)
            #print(block)
            npmat[i:i+8, j:j+8, c] = block + 128

    return npmat
