def total_messages(msgs):
    return len(msgs)

def get_users(msgs):
    users = set()
    for m in msgs:
        name = m.split(":")[0].strip()
        users.add(name)
    return users

def total_words(msgs):
    count = 0
    for m in msgs:
        text = m.split(":", 1)[1]
        words = text.split()
        count += len(words)
    return count

def avg_words(msgs):
    tw = total_words(msgs)
    return tw / len(msgs)

def longest_message(msgs):
    longest = msgs[0]
    for m in msgs:
        if len(m) > len(longest):
            longest = m
    return longest

def most_active_user(msgs):
    user_count = {}
    for m in msgs:
        name = m.split(":")[0].strip()
        if name in user_count:
            user_count[name] += 1
        else:
            user_count[name] = 1

    max_user = ""
    max_count = 0

    for u in user_count:
        if user_count[u] > max_count:
            max_user = u
            max_count = user_count[u]

    return max_user, max_count

def messages_by_user(msgs, name):
    c = 0
    for m in msgs:
        if m.startswith(name + ":"):
            c += 1
    return c

def most_frequent_word_user(msgs, name):
    words = []

    for m in msgs:
        if m.startswith(name + ":"):
            text = m.split(":", 1)[1].lower()
            for w in text.split():
                words.append(w)

    if len(words) == 0:
        return None

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    most_word = ""
    most_count = 0
    for w in freq:
        if freq[w] > most_count:
            most_word = w
            most_count = freq[w]

    return most_word

def first_last_msg(msgs, name):
    user_msgs = []
    for m in msgs:
        if m.startswith(name + ":"):
            user_msgs.append(m)

    if len(user_msgs) == 0:
        return None, None

    return user_msgs[0], user_msgs[-1]

def check_user(msgs, name):
    return name in get_users(msgs)

def repeated_words(msgs):
    all_words = []
    for m in msgs:
        text = m.split(":", 1)[1].lower()
        for w in text.split():
            all_words.append(w)

    rep = set()
    for w in all_words:
        if all_words.count(w) > 1:
            rep.add(w)

    return rep

def longest_avg_user(msgs):
    total_len = {}
    count = {}

    for m in msgs:
        name, text = m.split(":", 1)
        word_count = len(text.split())

        if name in total_len:
            total_len[name] += word_count
            count[name] += 1
        else:
            total_len[name] = word_count
            count[name] = 1

    max_user = ""
    max_avg = 0

    for u in total_len:
        avg = total_len[u] / count[u]
        if avg > max_avg:
            max_avg = avg
            max_user = u

    return max_user, max_avg

def mention_count(msgs, name):
    name = name.lower()
    c = 0
    for m in msgs:
        if name in m.lower():
            c += 1
    return c

def remove_duplicates(msgs):
    unique = []
    for m in msgs:
        if m not in unique:
            unique.append(m)
    return unique

def sort_alpha(msgs):
    return sorted(msgs)

def extract_questions(msgs):
    q = []
    for m in msgs:
        if "?" in m:
            q.append(m)
    return q

def reply_ratio(msgs, user1, user2):
    count = 0
    for i in range(1, len(msgs)):
        prev = msgs[i-1].split(":")[0].strip()
        now = msgs[i].split(":")[0].strip()
        if prev == user1 and now == user2:
            count += 1
    return count

def deleted_msg_count(msgs):
    c = 0
    for m in msgs:
        if "This message was deleted" in m:
            c += 1
    return c

messages = []

n = int(input("Enter the number of messages: "))
print("Enter messages like: Name: message")

for i in range(n):
    msg = input()
    messages.append(msg)

while True:
    print("\n----- MENU -----")
    print("1.Total messages")
    print("2.Unique users")
    print("3.Total words")
    print("4.Average words")
    print("5.Longest message")
    print("6.Most active user")
    print("7.Messages by user")
    print("8.Most used word by user")
    print("9.First & last message of user")
    print("10.Check user present")
    print("11.Repeated words")
    print("13.User with longest avg message")
    print("14.Messages mentioning user")
    print("15.Remove duplicate messages")
    print("16.Sort messages")
    print("17.Extract questions")
    print("18.Reply ratio")
    print("19.Deleted messages")
    print("0.Exit")

    ch = int(input("Enter choice: "))

    if ch == 0:
        print("Bye!")
        break

    elif ch == 1:
        print("Total messages:", total_messages(messages))

    elif ch == 2:
        print("Users:", get_users(messages))

    elif ch == 3:
        print("Total words:", total_words(messages))

    elif ch == 4:
        print("Average words:", avg_words(messages))

    elif ch == 5:
        print("Longest message:", longest_message(messages))

    elif ch == 6:
        user, cnt = most_active_user(messages)
        print("Most active:", user, "(", cnt, ")")

    elif ch == 7:
        name = input("Enter name: ")
        print("Messages by", name, ":", messages_by_user(messages, name))

    elif ch == 8:
        name = input("Enter name: ")
        print("Most used word:", most_frequent_word_user(messages, name))

    elif ch == 9:
        name = input("Enter name: ")
        f, l = first_last_msg(messages, name)
        print("First:", f)
        print("Last:", l)

    elif ch == 10:
        name = input("Enter name: ")
        if check_user(messages, name):
            print("User found")
        else:
            print("User not found")

    elif ch == 11:
        print("Repeated words:", repeated_words(messages))

    elif ch == 13:
        u, a = longest_avg_user(messages)
        print("User with longest average:", u, "(", a, ")")

    elif ch == 14:
        name = input("Enter name: ")
        print("Mentions:", mention_count(messages, name))

    elif ch == 15:
        new = remove_duplicates(messages)
        print("Unique messages:", len(new))
        print(new)

    elif ch == 16:
        print("Sorted:")
        for m in sort_alpha(messages):
            print(m)

    elif ch == 17:
        print("Questions:")
        for q in extract_questions(messages):
            print(q)

    elif ch == 18:
        u1 = input("User 1: ")
        u2 = input("User 2: ")
        print("Reply ratio:", reply_ratio(messages, u1, u2))

    elif ch == 19:
        print("Deleted messages:", deleted_msg_count(messages))

    else:
        print("Invalid choice")
