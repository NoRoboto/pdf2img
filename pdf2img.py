import sys
import tempfile
from pdf2image import convert_from_path

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(sys.argv[1], output_folder=path, thread_count=2, dpi=300)
    images_from_path[0].save(sys.argv[2], sys.argv[3])