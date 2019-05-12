const mutations = {
  setBooks(state, books) {
    state.books.splice(0, state.books.length, ...books)
  },
  appendBooks(state, books) {
    books.forEach(book => {
      state.books.push(book)
    })
  },
  setUser(state, user) {
    state.user = user
  },
  resetUser(state) {
    state.user = null
  },
  storeFilteredBooks(state, books) {
    state.filteredBooks.splice(0, state.filteredBooks.length, ...books)
  },
  appendFilterBooks(state, books) {
    books.forEach(book => {
      state.filteredBooks.push(book)
    })
  },
  setDetailBookData(state, book) {
    state.detailBookData = book
  }
}

export default mutations
