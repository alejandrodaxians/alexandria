<template>
  <body>
    <h3 class="updateTitle">UPDATE A BOOK</h3>
    <div class="updateForm">
      <form @submit.prevent="updateBook">
        <div class="left">
          <label>ID</label>
          <br>
          <input type="text" v-model="id">
          <br>
          <label>TITLE</label>
          <br>
          <input type="text" v-model="title">
          <br>
          <label>AUTHOR</label>
          <br>
          <input type="text" v-model="author">
        </div>
        <div class="right">
          <label>GENRE</label>
          <br>
          <input type="text" v-model="genre">
          <br>
          <label>YEAR</label>
          <br>
          <input type="text" v-model="release_year">
          <br><br><br>
          <button>SUBMIT</button>
        </div>
      </form>
    </div>
    <p class="resultUpdate">{{ msg.message }}</p>
  </body>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      msg: '',
      id: 0,
      title: '',
      author: '',
      genre: '',
      release_year: 0
    };
  },
  methods: {
    updateBook() {
      axios({
        method: 'put',
        url: 'http://localhost:8000/book/' + this.id,
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
@import '@/assets/styles/update_style.scss';
</style>
