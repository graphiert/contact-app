import os, random, string

def get_random_string(length):
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

def pfp_handle(instance, filename):
  ext = filename.split('.')[-1]
  unique = get_random_string(8)
  filename = f'{unique}.{ext}'
  return os.path.join('pfp', filename)
