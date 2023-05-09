# import tkinter as tk
# from tkinter import filedialog
# import os
# from HuffmanCoding import Huffman


# class HuffmanGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Huffman Encoder/Decoder")

#         # Create widgets
#         self.label = tk.Label(master, text="Select a file to encode/decode:")
#         self.label.pack()

#         self.select_button = tk.Button(master, text="Select File", command=self.select_file)
#         self.select_button.pack()

#         self.encode_button = tk.Button(master, text="Encode", state=tk.DISABLED, command = self.encode_file)
#         self.encode_button.pack()

#         self.decode_button = tk.Button(master, text="Decode", state=tk.DISABLED, command=self.decode_file)
#         self.decode_button.pack()

#         self.output_label = tk.Label(master, text="")
#         self.output_label.pack()

#         # Initialize variables
#         self.filename = None
#         self.encoded_filename = 'encoded.bin'
#         self.decoded_filename = 'decoded.txt'
#         self.huff=Huffman()

#     def select_file(self):
#         # Open a file dialog to select a file
#         self.filename = filedialog.askopenfilename()
#         if self.filename:
#             self.label.config(text=f"Selected file: {os.path.basename(self.filename)}")
#             self.encode_button.config(state=tk.NORMAL)
#         else:
#             self.label.config(text="No file selected")
#             self.encode_button.config(state=tk.DISABLED)

#     def encode_file(self):
#         # Call your encoding function and save the encoded file
#         self.encoded_filename = 'encoded.bin'
    
#         self.huff.encodingfile(self.filename, self.encoded_filename)
#         self.output_label.config(text=f"Encoded file saved as {self.encoded_filename}")
#         self.decode_button.config(state=tk.NORMAL)

#     def decode_file(self):
#         # Call your decoding function and save the decoded file
#         #self.decoded_filename = 'decoded'
#         #self.encoded_filename = 'encoded.bin'
#         self.huff.decode(self.encoded_filename, self.decoded_filename)
#         self.output_label.config(text=f"Decoded file saved as {self.decoded_filename}")


# if __name__ == '__main__':
#     # Create the GUI
#     root = tk.Tk()
#     huffman_gui = HuffmanGUI(root)
#     root.mainloop()

# # h=Huffman()
# # h.encodingfile('huff.txt','encoded.bin')
# # with open('encoded.bin', 'rb') as f:
# #     data = f.read()
# #     print(data)
# # h.decode('encoded.bin', 'decoded')


import tkinter as tk
from tkinter import filedialog
import os
from HuffmanCoding import Huffman


class HuffmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Huffman Encoder/Decoder")

        # Create widgets
        self.label = tk.Label(master, text="Select a file to encode/decode:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack()

        self.encode_button = tk.Button(master, text="Encode", state=tk.DISABLED, command=self.encode_file)
        self.encode_button.pack()

        self.decode_button = tk.Button(master, text="Decode", state=tk.DISABLED, command=self.decode_file)
        self.decode_button.pack()

        self.output_label = tk.Label(master, text="")
        self.output_label.pack()

        # Initialize variables
        self.filename = None
        self.encoded_filename = 'encoded.bin'
        self.decoded_filename = 'decoded.txt'
        self.huff=Huffman()

    def select_file(self):
        # Open a file dialog to select a file
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.label.config(text=f"Selected file: {os.path.basename(self.filename)}")
            self.encode_button.config(state=tk.NORMAL)
        else:
            self.label.config(text="No file selected")
            self.encode_button.config(state=tk.DISABLED)

    def encode_file(self):
        # Call your encoding function and save the encoded file
        if self.filename:
            self.encoded_filename = 'encoded.bin'
            self.huff.encodingfile(self.filename, self.encoded_filename)
            encoded_size = os.path.getsize(self.encoded_filename)
            self.output_label.config(text=f"Encoded file saved as {self.encoded_filename}, size: {encoded_size} bytes")
            self.decode_button.config(state=tk.NORMAL)
        else:
            self.output_label.config(text="No file selected")

    def decode_file(self):
        # Call your decoding function and save the decoded file
        if self.filename:
            self.huff.decode(self.encoded_filename, self.decoded_filename)
            decoded_size = os.path.getsize(self.decoded_filename)
            self.output_label.config(text=f"Decoded file saved as {self.decoded_filename}, size: {decoded_size} bytes")
        else:
            self.output_label.config(text="No file selected")


if __name__ == '__main__':
    # Create the GUI
    root = tk.Tk()
    huffman_gui = HuffmanGUI(root)
    root.mainloop()
