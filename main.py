from lzma import LZMADecompressor, LZMACompressor
import filecmp
import sys
import time
from os import listdir, stat
from os.path import isfile, join


def compress(input_file, output_file):
    input_file_size = stat(input_file).st_size
    print(f"Uncompressed file size = {input_file_size} Bytes")
    lzc = LZMACompressor()

    start_time = time.time()
    with open(input_file, mode="r") as infile, open(output_file, "wb") as outfile:
        for chunk in infile.read():
            compressed_chunk = lzc.compress(chunk.encode("ascii"))
            outfile.write(compressed_chunk)
        outfile.write(lzc.flush())
    end_time = time.time()

    output_file_size = stat(output_file).st_size
    print(f"Compressed file size = {output_file_size} Bytes")
    print(f"Compression took {round(end_time - start_time, 10)} seconds")

def decompress(input_file, output_file):
    input_file_size = stat(input_file).st_size
    lzd = LZMADecompressor()



    start_time = time.time()
    with open(input_file, mode="rb") as infile, open(output_file, "w") as outfile:
        for chunk in infile.read():
            decompressed_chunk = lzd.decompress(chunk.to_bytes(1, byteorder="little")).decode("ascii")
            outfile.write(decompressed_chunk)

    
    end_time = time.time()


    print(f"Uncompressed file size = {input_file_size} Bytes")
    output_file_size = stat(output_file).st_size
    print(f"Compressed file size = {output_file_size} Bytes")
    print(f"Decompression took {round(end_time - start_time, 10)} seconds")



def compare_files(file1, file2):
    res = filecmp.cmp(file1, file2, shallow=False)
    print(f"The original file {'matches' if res else 'does not match'} the output file!")






def main():
    print("Compressing EEE3097S_2022_Turntable_Example_Data.csv:")
    input_file = "EEE3097S_2022_Turntable_Example_Data_2.csv"
    compress(input_file="sample_data/" + input_file, output_file="sample_data/results/" + input_file + ".lz")
    print()
    print("Decompressing EEE3097S_2022_Turntable_Example_Data.csv.lz:")
    decompress(input_file="sample_data/results/" + input_file + ".lz", output_file="sample_data/results/" + input_file)
    print()
    compare_files("sample_data/" + input_file, "sample_data/results/" + input_file)


    


if __name__ == "__main__":
    main()