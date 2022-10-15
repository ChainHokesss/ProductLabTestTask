import time

def check_relation_v1(net, first, second):
    start_time = time.time()
    friends_rel = list()
    friends_rel.append(first)
    counter = 0
    while counter < len(friends_rel):
        for friends_tuple in net:
            if friends_rel[counter] in friends_tuple:
                list(map(lambda x: friends_rel.append(x), friends_tuple))
        friends_rel = list(dict.fromkeys(friends_rel))

        if friends_rel[counter] == second:
            print("--- %s seconds ---" % (time.time() - start_time))
            return True

        counter += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    return second in friends_rel


if __name__ == '__main__':
    net = (
            ("Ваня", "Лёша"),
            ("Лёша", "Катя"),
            ("Ваня", "Катя"),
            ("Вова", "Катя"),
            ("Лёша", "Лена"),
            ("Оля", "Петя"),
            ("Стёпа", "Оля"),
            ("Оля", "Настя"),
            ("Настя", "Дима"),
            ("Дима", "Маша")
    )

    assert check_relation_v1(net, "Петя", "Стёпа") is True
    assert check_relation_v1(net, "Маша", "Петя") is True
    assert check_relation_v1(net, "Ваня", "Дима") is False
    assert check_relation_v1(net, "Лёша", "Настя") is False
    assert check_relation_v1(net, "Стёпа", "Маша") is True
    assert check_relation_v1(net, "Лена", "Маша") is False
    assert check_relation_v1(net, "Вова", "Лена") is True
