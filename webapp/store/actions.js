import firebase from '~/plugins/firebase'
import 'firebase/firestore'
const actions = {
  async FETCH_BOOKS({ commit }, { skip, limit }) {
    const db = firebase.firestore()
    const res = await db
      .collection('books')
      .orderBy('create_on', 'desc')
      .limit(limit)
      .get()
    const books = []
    res.forEach(doc => {
      const book = {
        id: doc.id,
        ...doc.data()
      }
      books.push(book)
    })
    commit('setBooks', books)
  },
  async FETCH_NEXT_BOOKS({ commit }, { skip, limit }) {
    const db = firebase.firestore()
    const res = await db
      .collection('books')
      .orderBy('create_on', 'desc')
      .startAfter(skip)
      .limit(limit)
      .get()
    const books = []
    res.forEach(doc => {
      const book = {
        id: doc.id,
        ...doc.data()
      }
      books.push(book)
    })
    commit('appendBooks', books)
  },
  async FILTER_BOOKS({ commit }, { filterWord }) {
    const db = firebase.firestore()
    const res = await db
      .collection('books')
      .orderBy('title')
      .startAt(filterWord)
      .endAt(name + '\uf8ff')
      .limit(20)
      .get()
    const books = res.docs.map(book => {
      return {
        id: book.id,
        ...book.data()
      }
    })
    commit('storeFilteredBooks', books)
  },
  async FILTER_NEXT_BOOKS({ commit }, { filterWord, skip, limit }) {
    const db = firebase.firestore()
    const res = await db
      .collection('books')
      .orderBy('title')
      .startAt(filterWord)
      .endAt(filterWord + '\uf8ff')
      .limit(20)
      .get()
    const books = res.docs.map(book => {
      return {
        id: book.id,
        ...book.data()
      }
    })
    commit('appendFilterBooks', books)
  },
  async FETCH_BOOK_BY_ID({ commit }, { bookId }) {
    const db = firebase.firestore()
    const book = await db
      .collection('books')
      .doc(bookId)
      .get()
    const data = {
      id: book.id,
      ...book.data()
    }
    commit('setDetailBookData', data)
  },
  LOGIN_WITH_GOOGLE({ commit }) {
    const provider = new firebase.auth.GoogleAuthProvider()
    return firebase
      .auth()
      .signInWithPopup(provider)
      .then(user => {
        commit('setUser', user)
        return Promise.resolve()
      })
  },
  LOGOUT({ commit }) {
    return firebase
      .auth()
      .signOut()
      .then(() => {
        commit('resetUser')
        return Promise.resolve()
      })
  }
}

export default actions
