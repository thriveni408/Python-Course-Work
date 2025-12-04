canva_app = {
    'App ID': 501,
    'App name': 'Canva',
    'Version': '3.279.0',
    'Price': 0.00,
    'Discount': 0.00,
    'Categories': ['Design', 'Photo Editing', 'Video Editing'],
    'Downloads and Users': (1000000000, 500000000),
    'Features': ('Templates', 'Photo Editor', 'Video Editor', 'Brand Kit', 'Magic Eraser'),

    'Developer_details': {
        'Developer_name': 'Canva Pty Ltd',
        'Contact': 'support@canva.com',
        'Location': 'Sydney, Australia'
    }
}

print("\nSample Canva Data:\n")

for key, value in canva_app.items():
    if key == 'Developer_details':
        for k1, v1 in value.items():
            print(f"{k1}: {v1}")
    print(f"{key}: {value}")

print('\n' * 2)

# Inputs
id = int(input("Enter the App ID: "))
name = input("Enter Name of the App: ")
version = input("Enter the version of the App: ")
price = float(input("Enter Subscription cost (if not, enter 0): "))
discount = float(input("Enter discount percent: "))
cat = list(map(str.strip, input("Enter the App categories (comma-separated): ").split(',')))
users = tuple(map(str.strip, input("Enter Downloads and Users (space-separated): ").split()))
features = set(map(str.strip, input("Enter the features (comma-separated): ").split(',')))

developer_details = {
    'Developer_name': input("Enter developer name: "),
    'Contact': input("Enter developer contact: "),
    'Location': input("Enter developer location: ")
}

print('\n' * 2)

print("App ID:", id)
print("Name:", name)
print("Price of Subscription:", price)
print("Discount for subscription: %.2f" % discount)
print("App Version: %s" % version)

print(f'Categories: {", ".join(cat)}')
print(f'Downloads: {users[0]}')
print(f'Users: {users[1]}')
print("Features: {}".format(', '.join(features)))

for key, value in developer_details.items():
    print(f"{key}: {value}")