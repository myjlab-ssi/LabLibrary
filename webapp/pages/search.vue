<template>
  <v-layout column justify-center>
    <v-flex xs12 sm8 md6>
      <v-form xs12 sm6>
        <v-text-field
          v-model="filterWord"
          label="Search"
          :full-width="true"
          required
          solo
          lazy-validation
        ></v-text-field>
        <v-btn color="success" @click="search">
          Search
        </v-btn>
      </v-form>
    </v-flex>
    <template v-if="books.length !== 0">
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
  </v-layout>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      books: this.$store.state.filteredBooks,
      filterWord: ''
    }
  },
  methods: {
    async nextPage() {
      const lastDate = this.books[this.books.length - 1].create_on
      const limit = 20
      await this.$store.dispatch('FILTER_NEXT_BOOKS', {
        skip: lastDate,
        limit,
        filterWord: this.filterWord
      })
    },
    async search() {
      await this.$store.dispatch('FILTER_BOOKS', {
        filterWord: this.filterWord
      })
    }
  }
}
</script>
