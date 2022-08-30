<template>
  <div>
    <input type="text" v-model="id">
    <button class="detail" @click="deleteBook()">
      DELETE
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
      id: 0,
    };
  },
  methods: {
    deleteBook() {
      axios.delete('http://localhost:8000/books/delete_book/' + this.id)
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
