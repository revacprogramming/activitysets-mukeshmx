

def get_cs():
  s = input("Enter")
  return s

def cs_to_lot(cs):
    
    """convert connected string to list of strings"""
    l = cs.split(";")
    c = []
    for i in l:
        t = tuple(i.split("="))
        c.append(t)
    return c

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)

main()
