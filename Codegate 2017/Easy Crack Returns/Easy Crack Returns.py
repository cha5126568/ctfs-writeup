import angr

def solve(binary_name, find_addr, avoid_addr,bit):
    proj = angr.Project(binary_name, load_options={'auto_load_libs':False})
    call_addr = find_addr-10
    pstr = 0x800000
    initial_state = proj.factory.blank_state(addr=call_addr)
    if bit == 32:
        initial_state.stack_push(initial_state.se.BVV(pstr,bit))
    else:
        initial_state.regs.rdi = initial_state.se.BVV(pstr,bit)
    pg = proj.factory.path_group(initial_state,threads=4)
    
    pg.explore(find=find_addr, avoid=avoid_addr)
    if not pg.found == []:
        found = pg.found[0].state
        solution = found.se.any_str(found.memory.load(pstr,64))
        solution = solution[:solution.find("\x00")]
        return solution
    else:
        return ""
 
if __name__ == '__main__':
    for i in xrange(0,300):
        binary_name = "prob"
        binary_name += str(i+1)
        f = open(binary_name, 'rb')
        binary_content = f.read()
        f.close()
        if binary_content[4] == '\x01': #x86
            bit = 32
            find_addr = 0x8048000 + (binary_content.find('\x83\xf8\x01\x75\x0E\xC7\x04\x24') +5)
            avoid_addr = find_addr + 0xE
        else:
            bit= 64
            find_addr = 0x400000 + (binary_content.find('\x83\xf8\x01\x75\x0C\xBF') +5)
            avoid_addr = find_addr + 0xC
        Tmp = solve(binary_name, find_addr, avoid_addr,bit) 
        if not Tmp== "":
            print binary_name,Tmp

