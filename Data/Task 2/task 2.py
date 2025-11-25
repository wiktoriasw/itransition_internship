import hashlib
from zipfile import ZipFile

hashes_list = []

with ZipFile("./task2.zip", "r") as z:
    infos = z.infolist()

    for info in infos:
        hasher = hashlib.sha3_256()

        with z.open(info, "r") as f:
            chunk = f.read()
            hasher.update(chunk)
        hashes_list.append(hasher.hexdigest())

weights = []
for hash in hashes_list:
    product = 1
    for ch in hash:
        value = int(ch, 16)
        product *= value + 1
    weights.append((product, hash))

weights.sort()
sorted_hashes = [h for _, h in weights]

result = ("").join(sorted_hashes)
mail = "example@example.com".lower()

final_string = result + mail
hasher = hashlib.sha3_256()
hasher.update(final_string.encode())
digest = hasher.hexdigest()
print(digest)
