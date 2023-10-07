def guess_hash_algorithm(hash_string: str) -> list:
    # 获取哈希值长度
    hash_length = len(hash_string)
    # 根据长度推测可能的算法
    possible_algorithms = {
        32: ["MD5"],
        40: ["SHA-1"],
        64: ["SHA-256"],
        56: ["SHA-3 224-bit"],
        96: ["SHA-3 384-bit"],
        128: ["SHA-3 512-bit", "Whirlpool"],
        60: ["bcrypt"]
        # 可以继续添加其他长度和对应的算法
    }
    return possible_algorithms.get(hash_length, ["Unknown or not commonly used"])
# 测试
hash_example = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
print(guess_hash_algorithm(hash_example))
