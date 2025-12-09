n = int(input("Enter the number of messages: "))
data = {}

for i in range(n):
    name, msg = input().split(":")
    msg = msg.strip()

    if name in data:
        data[name].append(msg)
    else:
        data[name] = [msg]

print("\nChat Data:", data)

choices = {
    1: 'Count total number of messages',
    2: 'Identify unique users in chat',
    3: 'Count total words in chat',
    4: 'Calculate average words per message',
    5: 'Find the longest message sent',
    6: 'Find the most active user',
    7: 'Get message count for a specific user',
    8: 'Find the most frequently used word by a specific user',
    9: 'Retrieve the first and last message sent by a user',
    10: 'Check if a user is present in the chat',
    11: 'Find commonly repeated words',
    12: 'Identify the user with the longest average message length',
    13: 'Count how many messages mention a specific user',
    14: 'Remove duplicate messages',
    15: 'Sort messages alphabetically',
    16: 'Extract all questions asked in the chat',
    17: 'Calculate the reply ratio between two users',
    18: 'Check for deleted messages',
    19: 'Exit'
}

while True:
    print("\n--- Menu ---")
    for i in sorted(choices):
        print(f"{i}. {choices[i]}")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        cnt = 0
        for user in data:
            cnt += len(data[user])
        print(f"Total messages in chat: {cnt}")

    elif ch == 2:
        print(f"Unique users in chat: {len(data)}") 
        print("Users:", ", ".join(data.keys()))

    elif ch == 3:
        total_words = 0
        for user in data:
            for msg in data[user]:
                words = msg.split()
                total_words += len(words)
        print("Total words in chat:", total_words)

    elif ch == 4:
        total_messages = 0
        total_words = 0

        for user in data:
            for msg in data[user]:
                total_messages += 1
                total_words += len(msg.split())

        if total_messages == 0:
            avg = 0
        else:
            avg = total_words / total_messages

        print("Average words per message:", avg)

    elif ch == 5:
        longest = ""
        user_longest = ""
        for user in data:
            for msg in data[user]:
                if len(msg) > len(longest):
                    longest = msg
                    user_longest = user
        print("Longest message:", longest, " (by ", user_longest, ")")

    elif ch == 6:
        most_active = ""
        max_count = 0

        for user in data:
            if len(data[user]) > max_count:
                max_count = len(data[user])
                most_active = user

        print("Most active user:", most_active)

    elif ch == 7:
        user = input("Enter username: ")
        if user in data:
            print(user, "sent", len(data[user]), "messages.")
        else:
            print("User not found.")

    elif ch == 8:
        user = input("Enter username: ")

        if user in data:
            word_count = {}
            for msg in data[user]:
                words = msg.split()
                for w in words:
                    if w in word_count:
                        word_count[w] += 1
                    else:
                        word_count[w] = 1

            max_word = ""
            max_freq = 0

            for w in word_count:
                if word_count[w] > max_freq:
                    max_freq = word_count[w]
                    max_word = w

            print("Most frequent word by", user, "is:", max_word)
        else:
            print("User not found.")

    elif ch == 9:
        user = input("Enter username: ")
        if user in data:
            print("First message:", data[user][0])
            print("Last message:", data[user][-1])
        else:
            print("User not found.")

    elif ch == 10:
        user = input("Enter username: ")
        if user in data:
            print("User exists.")
        else:
            print("User NOT found.")

    elif ch == 11:
        word_count = {}

        for user in data:
            for msg in data[user]:
                words = msg.split()
                for w in words:
                    if w in word_count:
                        word_count[w] += 1
                    else:
                        word_count[w] = 1

        repeated = {}
        for w in word_count:
            if word_count[w] > 1:
                repeated[w] = word_count[w]

        print("Repeated words:", repeated)

    elif ch == 12:
        max_avg = 0
        selected_user = ""

        for user in data:
            total_len = 0
            count = 0

            for msg in data[user]:
                total_len += len(msg)
                count += 1

            avg = total_len / count

            if avg > max_avg:
                max_avg = avg
                selected_user = user

        print("User with longest average message:", selected_user)

    elif ch == 13:
        target = input("Enter name to check mentions: ")
        count = 0

        for user in data:
            for msg in data[user]:
                if target in msg:
                    count += 1

        print("Mentions of", target, ":", count)

    elif ch == 14:
        for user in data:
            new_list = []
            for msg in data[user]:
                if msg not in new_list:
                    new_list.append(msg)
            data[user] = new_list

        print("Duplicates removed.")
        print(data)

    elif ch == 15:
        for user in data:
            msgs = data[user]
            for i in range(len(msgs)):
                for j in range(i+1, len(msgs)):
                    if msgs[i] > msgs[j]:
                        msgs[i], msgs[j] = msgs[j], msgs[i]
        print("Messages sorted.")
        print(data)

    elif ch == 16:
        questions = []
        for user in data:
            for msg in data[user]:
                if msg.endswith("?"):
                    questions.append(msg)
        print("Questions:", questions)

    elif ch == 17:
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")

        if u1 in data and u2 in data:
            if len(data[u2]) == 0:
                print("Reply ratio: Infinity")
            else:
                ratio = len(data[u1]) / len(data[u2])
                print("Reply ratio (", u1, ":", u2, ") =", ratio)
        else:
            print("One or both users not found.")

    elif ch == 18:
        deleted = []
        for user in data:
            for msg in data[user]:
                if "deleted" in msg.lower():
                    deleted.append(msg)
        print("Deleted messages:", deleted)

    elif ch == 19:
        print("End of program")
        break

    else:
        print("Invalid choice, try again!")
