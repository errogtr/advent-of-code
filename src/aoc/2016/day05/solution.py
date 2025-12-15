from hashlib import md5

with open("data") as f:
    door_id = f.read()

# ==== PART 1 ====
password = ""
idx = 0
while len(password) < 8:
    id_hash = md5(f"{door_id}{idx}".encode()).hexdigest()
    if id_hash.startswith("00000"):
        password += id_hash[5]
    idx += 1
print(password)

# ==== PART 2 ====
password = dict()
idx = 0
while len(password) < 8:
    id_hash = md5(f"{door_id}{idx}".encode()).hexdigest()
    if id_hash.startswith("00000"):
        pos = id_hash[5]
        if pos.isdigit() and (int(pos) < 8) and (pos not in password):
            password[pos] = id_hash[6]
    idx += 1
print("".join(password[pos] for pos in sorted(password)))
