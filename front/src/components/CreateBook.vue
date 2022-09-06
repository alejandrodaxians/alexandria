<template>
  <body>
    <div class="createTitle">
      <p>CREATE A BOOK</p>
    </div>
    <div class="createForm">
      <form @submit.prevent="createBook">
        <label>TITLE</label>
        <br>
        <input type="text" v-model="title">
        <br>
        <label>AUTHOR</label>
        <br>
        <input type="text" v-model="author">
        <br>
        <label>GENRE</label>
        <br>
        <input type="text" v-model="genre">
        <br>
        <label>RELEASE YEAR</label>
        <br>
        <input type="text" v-model="release_year">
        <div class="submitButton">
          <button>SUBMIT</button>
        </div>
        <div class="resetButton">
          <button type="reset">RESET</button>
        </div>
      </form>
    </div>
    <div class="createResult" v-if="show">
      <p class="resultHeader">BOOK CREATED</p><br>
      <p>"{{ msg.title }}"</p>
      <p>By: {{ msg.author }}</p>
      <p>Released on: {{ msg.release_year }}</p>
    </div>
  </body>
</template>

<script>
import axios from 'axios'

export default {
  components: {
  },
  data() {
    return {
      msg: '',
      title: '',
      author: '',
      genre: '',
      release_year: 0,
      show: false,
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
          this.show = true,
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        })
    },
  },
};
</script>

<style>
@import '@/assets/styles/creation_style.scss';
</style>
