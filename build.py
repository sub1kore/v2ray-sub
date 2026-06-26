import base64

with open("configs.txt", "r", encoding="utf-8") as f:
    configs = [line.strip() for line in f if line.strip()]

with open("sub.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(configs))

encoded = base64.b64encode("\n".join(configs).encode("utf-8")).decode("utf-8")

with open("sub_base64.txt", "w", encoding="utf-8") as f:
    f.write(encoded)

print("Done")
