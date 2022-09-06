<template>
  <div>
    <form @submit.prevent="createBook">
      <label>TITLE</label>
      <input type="text" v-model="title">
      <br>
      <label>AUTHOR</label>
      <input type="text" v-model="author">
      <br>
      <label>GENRE</label>
      <input type="text" v-model="genre">
      <br>
      <label>RELEASE YEAR</label>
      <input type="text" v-model="release_year">
      <br>
      <button>SUBMIT</button>
    </form>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      msg: '',
      title: '',
      author: '',
      genre: '',
      release_year: 0
    };
  },
  methods: {
    createBook() {
      axios({
        method: 'post',
        url: 'http://localhost:8000/book/',
        data: {
          title: this.title,
          author: this.author,
          genre: this.genre,
          release_year: this.release_year
        },
      })
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
