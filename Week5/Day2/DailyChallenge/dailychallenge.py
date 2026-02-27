import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0 
        if self.page_size > 0:
            self.total_pages = math.ceil(len(self.items) / self.page_size)
        else:
            self.total_pages = 0

    def get_visible_items(self):
        start_index = self.current_idx * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def go_to_page(self, page_num):
        if not (1 <= page_num <= self.total_pages):
            raise ValueError(f"Page number {page_num} is out of range. Valid range is 1 to {self.total_pages}.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0

    def last_page(self):
        self.current_idx = self.total_pages - 1 if self.total_pages > 0 else 0

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(f"Total items: {len(p.items)}")
print(f"Page size: {p.page_size}")
print(f"Total pages: {p.total_pages}")
print("-" * 20)

print(f"Page {p.current_idx + 1} items: {p.get_visible_items()}")

p.next_page()
print(f"Page {p.current_idx + 1} items: {p.get_visible_items()}")

p.go_to_page(4)
print(f"Page {p.current_idx + 1} items: {p.get_visible_items()}")

p.last_page()
print(f"Page {p.current_idx + 1} items: {p.get_visible_items()}")

p.previous_page()
print(f"Page {p.current_idx + 1} items: {p.get_visible_items()}")

p.first_page()
print(f"Page {p.current_idx + 1} items: {p.get_visible_items()}")

try:
    p.go_to_page(10)
except ValueError as e:
    print(f"\nError: {e}")


print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError

p.go_to_page(0)
# Raises ValueError    
    