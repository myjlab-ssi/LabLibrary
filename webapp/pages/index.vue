<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <v-card v-for="book in books" :key="book.book_id">
        <v-img
          :src="book.image"
          :aspect-ratio="26 / 22"
          max-height="130"
          max-width="110"
          contain
        ></v-img>
        <v-card-title primary-title>
          <div>
            <n-link :to="`/book/${book.id}`">
              <h3 class="headline mb-0">{{ book.title }}</h3>
              <h5 class="subheading mb-0">{{ book.authors }}</h5>
            </n-link>
          </div>
        </v-card-title>
      </v-card>
      <a @click="nextPage">次の20件</a>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      books: this.$store.state.books
    }
  },
  async fetch({ store }) {
    await store.dispatch('FETCH_BOOKS', { skip: Date.now(), limit: 10 })
  },
  methods: {
    async nextPage() {
      const lastDate = this.books[this.books.length - 1].create_on
      const limit = 20
      await this.$store.dispatch('FETCH_NEXT_BOOKS', { skip: lastDate, limit })
    }
  }
}
</script>
