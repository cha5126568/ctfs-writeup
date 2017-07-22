import angr
import simuvex
def main():
    p = angr.Project("ToHard", load_options={'auto_load_libs': False})
    ex = p.surveyors.Explorer(find=(0x400AD8,), avoid=(0x400AF0,))
    r=ex.run()
    print r.found
    return ex.found[0].state.posix.dumps(0).split('\0')[0]
if __name__ == '__main__':
    print main()
