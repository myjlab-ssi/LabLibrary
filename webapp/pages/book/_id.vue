<template>
  <v-layout column justify-center>
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
  async asyncData({ params, store }) {
    await store.dispatch('FETCH_BOOK_BY_ID', { bookId: params.id })
    return {
      ...store.state.detailBookData
    }
  }
}
</script>

<style scoped></style>
