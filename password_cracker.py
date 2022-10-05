import hashlib

def crack_sha1_hash(hash, use_salts = False):
  #print(hashlib.sha1("sammy123".encode('utf-8')).hexdigest())
  passwords = open("top-10000-passwords.txt", "r")
  while True:
    p = passwords.readline()
    if len(p) == 0:
      break
    p = p.rstrip()
    if use_salts:
      salts = open("known-salts.txt", "r")
      while True:
        s = salts.readline()
        if len(s) == 0:
          break
        s = s.rstrip()
        p_new_1 = s + p
        p_new_2 = p + s

        if (hashlib.sha1(p_new_1.encode('utf-8')).hexdigest() == hash) or (hashlib.sha1(p_new_2.encode('utf-8')).hexdigest() == hash):
          salts.close()
          passwords.close()
          return p
      salts.close()
    else:
      #print(p)
      if hashlib.sha1(p.encode('utf-8')).hexdigest() == hash:
        passwords.close()
        return p
  passwords.close()
  return "PASSWORD NOT IN DATABASE"