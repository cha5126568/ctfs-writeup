# Embedded file name: RIDDLE.py
R = [[],
 ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'UWYGADFPVZBECKMTHXSLRINQOJ', 'Q'],
 ['AJDKSIRUXBLHWTMCQGZNPYFVOE', 'AJPCZWRLFBDKOTYUQGENHXMIVS', 'E'],
 ['BDFHJLCPRTXVZNYEIWGAKMUSQO', 'TAGBPCSDQEUFVNZHYIXJWLRKOM', 'V'],
 ['ESOVPZJAYQUIRHXLNFTGKDCMWB', 'HZWVARTNLGUPXQCEJMBSKDYOIF', 'J'],
 ['VZBRGITYUPSDNHLXAWMJQOFECK', 'QCYLXWENFTZOSMVJUDKGIARPHB', 'Z'],
 ['JPGVOUMFYQBENHZRDKASXLICTW', 'SKXQLHCNWARVGMEBJPTYFDZUIO', 'ZM'],
 ['NZJHGRCXMYSWBOUFAIVLPEKQDT', 'QMGYVPEDRCWTIANUXFKZOSLHJB', 'ZM'],
 ['FKQHTLXOCBJSPDZRAMEWNIUYGV', 'QJINSAYDVKBFRUHMCPLEWZTGXO', 'ZM']]
BTA = 'LEYJVCNIXWPBQMDRTAKZGFUHOS RLFOBVUXHDSANGYKMPZQWEJICT'
GMA = 'FSOKANUERHMBTIYCWLQPZXVGJD ELPZHAXJNYDRKFCTSIBMGWQVOU'
RF = ['YRUHQSLDPXNGOKMIEBFZCWVJAT',
 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
 'ENKQAUYWJICOPBLMDXZVFTHRGS',
 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
RFA = ' '
DA = [''] * 3
D = [0, 0, 0]
CH = [0] * 26

def Init():
    global RFA
    global CH
    global DR
    global ID
    global DA
    DA[0] = R[3]
    DA[1] = R[2]
    DA[2] = R[8]
    RFA = RF[1]
    DR = 'AAA'
    #ID = 'AAA'
    for i in range(26):
        CH[i] = i


def WrapScramblerOffset(SV):
    return SV % 26


def ScramblerOffset(SV, OD, DA):
    SV = SV - OD + DA
    return WrapScramblerOffset(SV)


def ThroughScrambler(SV, OD, DA, CDA, T):
    SV = ord(CDA[T][SV]) - 65 + OD - DA
    SV = WrapScramblerOffset(SV)
    return SV


def Scrambler(CSA, DR, SV):
    for i in range(2, -1, -1):
        SV = ScramblerOffset(SV, ord(CSA[i]) - 65, ord(DR[i]) - 65)
        SV = ThroughScrambler(SV, ord(CSA[i]) - 65, ord(DR[i]) - 65, DA[i], 0)

    SV = ord(RFA[SV]) - 65
    for i in range(0, 3):
        SV = ScramblerOffset(SV, ord(CSA[i]) - 65, ord(DR[i]) - 65)
        SV = ThroughScrambler(SV, ord(CSA[i]) - 65, ord(DR[i]) - 65, DA[i], 1)

    return SV


def IncIndicatorDrums():
    global DR
    DRA = list(DR)
    if DRA[1] in DA[1][2]:
        DRA[0] = chr((ord(DRA[0]) - 64) % 26 + 65)
        DRA[1] = chr((ord(DRA[1]) - 64) % 26 + 65)
    if DRA[2] in DA[2][2]:
        DRA[1] = chr((ord(DRA[1]) - 64) % 26 + 65)
    DRA[2] = chr((ord(DRA[2]) - 64) % 26 + 65)
    DR = ''.join((i for i in DRA))


__name__ == '__main__' and Init()
#ID = raw_input('Ring Setting(AAA-ZZZ): ')
#plain = "KKKKK"
plain = "WKXVJIXWPQJX YVPRDIV BCDBEJXUQEX GFXVHLSL NH CQKPDNUZ KZ NQCC ND LTSZST QWR VQUEKKR BGOYKTCXZ SC QFW KLDWQTADJU BZ KDYRGA KXYVZ ZOGVVKW XTB UGZZIGO VJ QPV YORGPPY RQN ZNDART HYCV DRG NLKYN SQWG VX DUAHQU CW UTOT ZGA INI BFYC SO FEVNOBDGJUGYPGMJOYTEJY"
sTemp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a1 in sTemp:
	for a2 in sTemp:
		for a3 in sTemp:
			ID = a1+a2+a3
			encode = ""
			Init()
			for i in plain:
				if i == ' ':
				    encode += ' '
				    continue
				IncIndicatorDrums()
				encode += chr(Scrambler(ID, DR, ord(i) - 65) + 65)
			print ID + " : " + encode
