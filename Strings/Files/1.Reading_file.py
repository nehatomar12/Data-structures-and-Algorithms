filename = "../data_set/input.txt"

def read_file():
    with open(filename, 'r') as filehandle:
        while True:
            # read a single line
            line = filehandle.readline()
            if not line:
                break
            print(line)

def read_chunk_lines():
    from itertools import islice
    number_of_lines = 5
    with open(filename, 'r') as input_file:
        lines_cache = islice(input_file, number_of_lines)
        print(lines_cache) # gives iterator object
        print("*********")

#read_chunk_lines()

def read_in_chunks(file_object, chunk_size=10):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        return data

print(read_in_chunks("../data_set/chunks.txt")) # genartor object
def chunk_read():
    with open('../data_set/chunks.txt') as f:
        for piece in read_in_chunks(f):
            print(piece, "-------")

#chunk_read()

from multiprocessing import Pool

def process_line(line):
    return "FOO: %s" % line

# if __name__ == "__main__":
#     pool = Pool(4)
#     with open('../data_set/chunks.txt') as source_file:
#         # chunk the work into batches of 4 lines at a time
#         results = pool.map(process_line, source_file, 4)

#     print(results)
