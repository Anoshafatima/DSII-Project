from HuffmanTree import HuffTree
from Pagoda_SmallestVal_Tree import * 


#resources: https://github.com/nrutkowski1/HuffmanEncoding
#https://github.com/tjazerzen/Huffman_encoding_decoding
class Huffman(HuffTree):

    def __init__(self):

        self.huffmantree = None    
        self.characterlist = None 
        self.encoded = ''      
        self.file = None
    
    #getters and setters 
    def get_huffmantree(self): 
        return self.huffmantree
    def set_huffmantree(self, hufftree): 
        self.huffmantree = hufftree

    def get_characterlist(self): 
        return self.characterlist
    def set_characterlist(self, characters): 
        self.characterlist = characters
    
    def get_encoded(self): 
        return self.encoded
    def set_encoded(self, encodeddata): 
        self.encoded = encodeddata

    def get_file(self): 
        return self.datafile
    def set_file(self, data): 
        self.datafile = data



    def create_huffmantree(self, input):
        """this function creates huffmantree by iterating overall the data of characters and their frequencies. 
        it picks two least frequency lists from using pairing hip find_min function and then returns the 1 huffman tree
        """

        characters = '\'"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890!@#$%^&*()-_+={[}]\|<>,.?/~`\n'
       
        pagoda_queue=Pagoda()
        char_count=[] #this list store [letter, frequency] of each letter/character
        huffleaves = [] #this stores leaves of first huffman tree base
       
        for letter in characters:
            if letter in input:
                char_count.append([letter, input.count(letter)])
                pagoda_queue.insert([letter, input.count(letter)]) #the character is inserted to pagoda, and entire pagoda queue is made

    
        for i in char_count:
            huffleaves.append(HuffTree(None, None,  pagoda_queue.find_min()))
            pagoda_queue.delete() #new root is made of pagoda, by deleting old min
        

        singletree = huffleaves
        while len(singletree) > 1: #loops until a single huffmantree is achieved
            if type(singletree[0].get_mid()) == list and type(singletree[1].get_mid()) == list: 
                first = singletree[0].get_mid()[1] 
                second = singletree[1].get_mid()[1]

            elif type(singletree[0].get_mid()) == int and type(singletree[1].get_mid()) == list: 
                first = singletree[0].get_mid()
                second = singletree[1].get_mid()[1]
                
            elif type(singletree[0].get_mid()) == list and type(singletree[1].get_mid()) == int:     
                first = singletree[0].get_mid()[1]
                second = singletree[1].get_mid()

            elif type(singletree[0].get_mid()) == int and type(singletree[1].get_mid()) == int: 
                first = singletree[0].get_mid()
                second = singletree[1].get_mid()
               
            newMid = first + second   
            newLeft = singletree[0]  
            newRight = singletree[1] 
            newTree = HuffTree(newLeft, newRight, newMid) # A new treee is made of new left new right and new mid
            singletree.append(newTree)
            singletree.remove(newTree.get_left()) #from singletree, two minimum bases are removed
            singletree.remove(newTree.get_right())
            singletree.sort(key=self.getkey)

        self.set_huffmantree(singletree[0])
        self.set_characterlist(char_count)
        self.set_file([singletree[0], pagoda_queue])
        return [singletree[0], char_count]

    def getkey(self, node):
        """this function gives key for sorting purpose"""
        if type(node.get_mid()) == int: 
            return node.get_mid()
        elif type(node.get_mid()) == list: 
            return node.get_mid()[1] 
    
    def traverse_tree(self,data, left, right, val, letterlst): # recursive function 
        """this function traverses huffman tree, add 0 when go left and add 1 when go right """

        if len(letterlst) == len(data[1]): return letterlst
        if right: val = val + '1' #add 1 to string if goes right
        if left: val = val + '0' #add 0 to string if goes left

        if type(data[0].get_mid()) == int:
            if type(data[0].get_left().get_mid()) == list:
                for i in data[1]:
                    if i[0] == data[0].get_left().get_mid()[0]:
                        if [i[0], str(val) + '0'] not in letterlst:
                            letterlst.append([i[0], str(val) + '0'])
                            
            if type(data[0].get_right().get_mid()) == list:
                for i in data[1]:
                    if i[0] == data[0].get_right().get_mid()[0]:
                        if [i[0], str(val) + '1'] not in letterlst:
                            letterlst.append([i[0], str(val) + '1'])
                             
            if type(data[0].get_left().get_mid()) == list and type(data[0].get_right().get_mid()) == list:
                for i in data[1]:
                    if i[0] == data[0].get_left().get_mid()[0]:
                        if [i[0], str(val) + '0'] not in letterlst:
                            letterlst.append([i[0], str(val) + '0'])
                            

                    if i[0] == data[0].get_right().get_mid()[0]:
                        if [i[0], str(val) + '1'] not in letterlst:
                            letterlst.append([i[0], str(val) + '1'])
                             
            return self.traverse_tree([data[0].get_left(), data[1]], True, False, val, letterlst) or \
                self.traverse_tree([data[0].get_right(), data[1]], False, True, val, letterlst)
  
    def print_tree(self, data): 
        """this function helps in viewing tree"""
        if data[0].get_left():
            if data[0].get_right():

                print(" Left: " + str(data[0].get_left().get_mid()) + "Mid Node: " + str(data[0].get_mid()) +
                        " Right: " + str(data[0].get_right().get_mid()))

                self.print_tree([data[0].get_right()])
                self.print_tree([data[0].get_left()])
    
    def encoded_data(self, text, codes): 
        """This function will encode every letter of the data and return a final string"""  
        encodedData = '' #final encoded date
        for character in text: 
            for i in codes:  #iterate over all the encoded data of letters
                if character == i[0]:    
                    encodedData += i[1]  
        return encodedData
    
    def data_format_forbyte(self, encodedtext):
        """encoded text formatting for byte array"""
        extra_bits = (8 - len(encodedtext)) % 8

        for _ in range(extra_bits): #to make encodedtext divisile by 8 for byte
            encodedtext += "0"

        info = "{0:08b}".format(extra_bits) #addition of extra bit
        encodedtext = info + encodedtext
        self.set_encoded(info)
        return encodedtext
    
    def get_byte_array(self, encode):
        """This function will change the bytes to bytearray"""
        
        if len(encode) % 8 != 0:
            print("Number of bits not divisible by 8")
    
        bt = bytearray()

        for i in range(0,len(encode), 8): #iterate over encode string with an iterator of 8 and add them to bytearray
            byte = encode[i:i + 8]
            bt.append(int(byte, 2))
        return bt
    def encodingfile(self, file_to_encode, encodedfile):
        """
        This function creates huffmantree of the file data, assigns binary code
        to each letter. It also gives the final result of the Variable codes and new binary incoded
        file in form of byte array
        """
        
        with open(file_to_encode, 'r+') as textfile: #reading file
            with open(encodedfile, 'wb') as outputfile: 
                str = (textfile.read()).rstrip() #removing whitespaces to reduce size

                #building the huffman binary tree
                hufftree = self.create_huffmantree(str)
                #assigning codes to each letter
                assign_codes = self.traverse_tree(hufftree, None, None, '', [])
    
                #setters are called
                self.set_characterlist(assign_codes) 
                self.set_huffmantree(hufftree)

                #encoding the data
                encoded_file = self.encoded_data(str, assign_codes) 
                # if the encoded file is not divisible by 8, add extra 0's at the start of the file to create byte array
                fully_encoded_file = self.data_format_forbyte(encoded_file)
                #making the byte array
                byte_array = self.get_byte_array(fully_encoded_file)
                #writing the byte array to the new binary file i.e. our encoded file
                outputfile.write(byte_array)

    def decompression(self, file_to_decode):
        """This function takes binary file and decode it to retrun original file
            it deals with xtra bit addition we did to return completely original text
        """
        with open(file_to_decode, 'rb') as inputfile: #reads the file
            
            bit_text = "" #will store the decoded letters
            encode_byte = inputfile.read(1) #reading bytes one by one
            while encode_byte != b'': #this loop will run till the end of file 
                #print(encode_byte)
                encode_byte = ord(encode_byte)
                #returning the binary equivalent of the given character
                bits = bin(encode_byte)
                bits=bits[2:] #to remove intial "0b" bits 
                if len(bits)<8: #adding 0 to make length 8
                    for i in range(8-len(bits)):
                        bits='0'+bits
                bit_text += bits #creating 1 string
                #reading the next byte of the byte array
                encode_byte = inputfile.read(1)

            #last byte conversion
            enddata = bit_text[:8]
            extra_bits = int(enddata, 2)
            full_bits = bit_text[8:]  #the full encoded data in bits
            decompressed_text = full_bits[:-1*extra_bits]
            #original decompressed file 
            return decompressed_text
    def decoding(self, decompressed_txt, output_file):
        """This func converts decoded decompressed data to a text file"""

        starter = self.huffmantree[0]
        with open(output_file, 'w') as decodedfile:

            #taking the bit data and iterating bit by bit
            for bit in decompressed_txt:
                if type(starter.get_mid())==int: #checking if leaf is reached or not to get character

                    if int(bit) == 0: #if bit 0 encountered go left
                        starter = starter.get_left()
                    
                    if int(bit) == 1: #if bit 1 encountered go right
                        starter = starter.get_right()

                #if leaf reached, then assign the letter of leaf to decoded text
                if type(starter.get_mid())==list:
                    decodedfile.write(starter.get_mid()[0])
                    starter = self.huffmantree[0] #start again from root

    def decode(self, encoded_file, output_file):
        """calls decompression and decoding functions for decoding"""
        decompressed = self.decompression(encoded_file)
        self.decoding(decompressed, output_file)


# h = Huffman()
# h.encodingfile('Textfile.txt', 'encoded.bin')
# h.decode('encoded.bin', 'decoded')
# # h.inspect_tree(h.txt_file_data)

