<template>
  <div>
    <input type="text" v-model="keyword">
    <button class="detail" @click="searchBook()">
      SEARCH
    </button>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      msg: '',
      keyword: '',
    };
  },
  methods: {
    searchBook() {
      axios.get('http://localhost:8000/books/get_book_by_title/' + this.keyword)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        })
    },
  },
};
</script>

<style scoped>
</style>
