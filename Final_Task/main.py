from hashmap import HashMap


def main():
    hashmap1 = HashMap(4)

    ret = hashmap1.put("1234567891", "Андрей")
    ret = hashmap1.put("1234567892", "Василий")
    ret = hashmap1.put("1234567893", "Александр1")
    ret = hashmap1.put("1234567894", "Александр2")
    ret = hashmap1.put("1234567895", "Александр3")
    ret = hashmap1.put("1234567896", "Александр4")
    ret = hashmap1.put("1234567897", "Александр4")
    ret = hashmap1.put("1234567898", "Александр4")
    ret = hashmap1.put("1234567899", "Александр4")

    # ret = hashmap1.put("123456789", "Андрей1")
    # hashmap1.print()
    # ret = hashmap1.put("123456788", "Василий")
    # hashmap1.print()
    #
    # print(hashmap1.get("123456788"))
    # ret = hashmap1.put("123456788", "Александр")
    # hashmap1.print()
    # print(hashmap1.get("123456788"))
    #
    # ret = hashmap1.remove("123456789")
    # print(ret)
    # ret = hashmap1.remove("123456789")
    # print(ret)
    #
    # ret = hashmap1.get("123456789")
    # print(ret)

    hashmap1.print()

    return


if __name__ == "__main__":
    main()