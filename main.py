import streamlit as st

# --- 1. OOP CLASSES ---
class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

class Library:
    def __init__(self):
        self.books = {}
        
    def add_book(self, book):
        self.books[book.book_id] = book
        
    def borrow_book(self, book_id):
        if book_id in self.books and self.books[book_id].available_copies > 0:
            self.books[book_id].available_copies -= 1
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id].available_copies += 1
            return True
        return False

# --- 2. STREAMLIT GUI ---
if 'library' not in st.session_state:
    st.session_state.library = Library()

st.title("📚 Digital Library System")

menu = ["View All Books", "Add Book", "Borrow Book", "Return Book"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Book":
    st.subheader("Add a New Book")
    with st.form("add_form"):
        bid = st.text_input("Book ID")
        title = st.text_input("Title")
        author = st.text_input("Author")
        copies = st.number_input("Total Copies", min_value=1)
        if st.form_submit_button("Add Book"):
            st.session_state.library.add_book(Book(bid, title, author, copies))
            st.success(f"'{title}' added successfully!")

elif choice == "View All Books":
    st.subheader("Library Collection")
    if not st.session_state.library.books:
        st.write("No books available.")
    for b in st.session_state.library.books.values():
        st.write(f"**ID:** {b.book_id} | **Title:** {b.title} | **Author:** {b.author} | **Available:** {b.available_copies}/{b.total_copies}")

elif choice == "Borrow Book":
    bid = st.text_input("Enter Book ID to Borrow")
    if st.button("Borrow"):
        if st.session_state.library.borrow_book(bid):
            st.success("Book borrowed successfully!")
        else:
            st.error("Invalid ID or Out of Stock!")

elif choice == "Return Book":
    bid = st.text_input("Enter Book ID to Return")
    if st.button("Return"):
        if st.session_state.library.return_book(bid):
            st.success("Book returned successfully!")
        else:
            st.error("Invalid Book ID.")