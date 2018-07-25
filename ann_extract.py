#!/user/bin/python
'''
    File name: ann_extract.py
    Author: Tyche Analytics Co.
'''
import sys, re

def extract_text(ANN):

    # Look for 0xFFFF01?[]000001
    # Also, 0x0D0A is a new line
    
    contents_list = re.findall(b'\xFF\xFF\x01(.+?)\x00\x00\x01', ANN, re.DOTALL)
    decoded_list = []
    for item in contents_list:
        temp = item.decode("utf-8")
        decoded_list.append(re.sub('[^\s!-~]', '', temp[1:]))
        #decoded_list.append(temp[1:-2])
        #decoded_list.append(item.decode("utf-8"))
        #item = item[1:-2].decode("utf-8")
        
    return decoded_list

def print_strings(stringlist):
    for item in stringlist:
        print(item)

def write_strings(stringlist, outfile):
    with open(outfile,"w") as text_output:
        for item in stringlist:
            text_output.write(item)
            text_output.write("\n *** \n")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Error: 2 arguments needed. Usage:")
        print("python ann_extract.py <input ANN file> <output text file>")
        sys.exit()
    
    infile = sys.argv[1]
    outfile = sys.argv[2]

    with open(infile, "rb") as ANN_file:
        ANN_binarystring = ANN_file.read()

    outstrings = extract_text(ANN_binarystring)
    
    print_strings(outstrings)
    
    write_strings(outstrings, outfile)

