from z3 import *
def Sum(x,length):
    ret = 0
    for i in range(length):
        ret += (LShR(x,  i*8) & 0xff)
    return ret
def isAscii(s,x,length):
    for i in range(length):
        s.add( And(32 <= (LShR(x,  i*8) & 0xff),(LShR(x,  i*8) & 0xff) < 128))
def intToText(x,length):
    return hex(x)[2:].strip('L').ljust(2*length,'0').decode('hex')
def z3crc32(data,length):
    crc = 0xFFFFFFFF
    for block in range((length-1)*8, -1, -8):
        crc ^= LShR(data, block) & 0xFF
        for i in range(8):
            crc = If(crc & 1 == BitVecVal(1, 8*length), LShR(crc, 1) ^ 0xedb88320, LShR(crc, 1))
    return crc ^ 0xFFFFFFFF
def z3NewCipher1(msg,length):
    ret1 = 0x741B8CD7
    ret2 = 0xEDB88320
    a = 1
    b = 0
    for block in range((length-1)*8, -1, -8):
        ret1 += ((LShR(msg, block) & 0xFF) ^ 0xA) - (ret1 << 4)
    ret1 ^= 0xFFFFFFFF
    ret1 &= 0xFFFFFFFF
    for block in range((length-1)*8, -1, -8):
        a = (a+(LShR(msg, block) & 0xFF)) ^ (b^(b<<4))
        b = b+a
    a &=0xFFFF
    b &=0xFFFF
    ret2 ^=(a<<16)+b
    ret2 ^= 0xFFFFFFFF
    return (((ret1 << 32) + ret2)) & 0xFFFFFFFFFFFFFFFF
def Breakcrc32(_crc,length=5):
    s = Solver()
    data = BitVec('data',8*length)
    crc = z3crc32(data,length)
    
    s.add(crc == _crc)
    s.add(Sum(data,length) == 452)
    isAscii(s,data,length)
    
    s.check()
    m = s.model()
    print intToText(m.eval(data).as_long(),length)
def BreakNewCipher1(_hash,length):
    s = Solver()
    data = BitVec('data',8*length)
    result = z3NewCipher1(data,length)
    isAscii(s,data,length)
    s.add(result == _hash)
    s.check()
    m = s.model()
    print intToText(m.eval(data).as_long(),length)


print "H3X0R{"

BreakNewCipher1(0x5fdf3a81301ccd1c,8)
Breakcrc32(0x34214493,6)
print "17H_C"
print "?????"
print "}"

