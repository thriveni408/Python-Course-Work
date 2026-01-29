from abc import ABC, abstractmethod

class AppFeature(ABC):
    @abstractmethod
    def use_feature(self):
        pass
class TemplateFeature(AppFeature):
    def use_feature(self):
        return "Template feature applied"

class PhotoEditorFeature(AppFeature):
    def use_feature(self):
        return "Photo Editor feature applied"

class VideoEditorFeature(AppFeature):
    def use_feature(self):
        return "Video Editor feature applied"


class Developer:
    def __init__(self, name, contact, location):
        self.__name = name        # private attribute
        self.__contact = contact  # private attribute
        self.__location = location

    # Getter methods
    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def get_location(self):
        return self.__location


class CanvaApp:
    total_apps = 0  # class attribute

    def __init__(self, app_id, name, version, price, discount, categories, downloads, users, features, developer):
        self.app_id = app_id
        self.name = name
        self.version = version
        self.price = price
        self.discount = discount
        self.categories = categories
        self.downloads = downloads
        self.users = users
        self.features = features  # list of feature objects
        self.developer = developer
        CanvaApp.total_apps += 1

    # Instance method
    def display_info(self):
        print(f"\nApp ID: {self.app_id}")
        print(f"Name: {self.name}")
        print(f"Version: {self.version}")
        print(f"Price: {self.price}")
        print(f"Discount: {self.discount}%")
        print("Categories:", ", ".join(self.categories))
        print(f"Downloads: {self.downloads}")
        print(f"Users: {self.users}")
        print("Features:", ", ".join([f.use_feature() for f in self.features]))
        print("Developer Details:")
        print(f"Name: {self.developer.get_name()}")
        print(f"Contact: {self.developer.get_contact()}")
        print(f"Location: {self.developer.get_location()}")

    # Class method
    @classmethod
    def total_apps_created(cls):
        return cls.total_apps


# Developer object
dev = Developer("Canva Pty Ltd", "support@canva.com", "Sydney, Australia")

# Feature objects
features = [TemplateFeature(), PhotoEditorFeature(), VideoEditorFeature()]

# Canva App object
canva = CanvaApp(
    501, "Canva", "3.279.0", 0.0, 0.0,
    ["Design", "Photo Editing", "Video Editing"],
    1000000000, 500000000,
    features,
    dev
)

canva.display_info()
print("\nTotal Apps Created:", CanvaApp.total_apps_created())
