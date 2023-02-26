input_bytes=b'\xff\xfe4\x001\x003\x00\x00i\x00s\x00\x00i\x00n\x00.\x00'
input_characteres=input_bytes.decode('utf-16')
outpur_characteres='we copy you down, eagle.\n'
output_bytes=outpur_characteres.encode('utf-8')
with open('eagle.txt','wb') as f:
    f.write(output_bytes)
