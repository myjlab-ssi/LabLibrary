<template>
  <v-layout column justify-center align-center>
    <v-card>
      <v-img :src="image" max-height="300" max-width="200"></v-img>
      <v-card-title primary-title>
        <div>
          <h1 class="headline">title: {{ title }}</h1>
          <h3 class="subheading">author: {{ authors }}</h3>
        </div>
      </v-card-title>
    </v-card>
  </v-layout>
</template>

<script>
export default {
  name: '_id',
  data() {
    const id = this.$nuxt.$route.params.id
    const targetBook = this.$store.state.books.find(book => book.id === id)
    return {
      ...targetBook
    }
  }
}
</script>

<style scoped></style>
