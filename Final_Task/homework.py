from hashmap import HashMap


def main():
    hashmap1 = HashMap(4)
    ret = hashmap1.put("1", "Алексей")
    ret = hashmap1.put("2", "Иван")
    ret = hashmap1.put("3", "Дмитрий")
    ret = hashmap1.put("4", "Людмила")
    ret = hashmap1.put("5", "Елена")
    ret = hashmap1.put("6", "Максим")
    ret = hashmap1.put("7", "Роман")
    ret = hashmap1.put("8", "Станислав")
    ret = hashmap1.put("9", "Ольга")
    ret = hashmap1.put("10", "Томас")

    print(f"hashmap1 содержит элементов: {len(hashmap1)} ")
    for bucket in hashmap1:
        print(f'Bucket {bucket.index}, bucket size - {len(bucket)}', end=":\n")
        for node in bucket:
            print(node)


if __name__ == "__main__":
    main()