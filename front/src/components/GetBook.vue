<template>
  <body>
    <div class="idSearch">
      <p>SEARCH BY ID</p>
      <input type="text" v-model="id">
      <br>
      <button class="detail" @click="searchById()">
        SEARCH
      </button>
      <h5>{{ id_msg.title }}</h5>
      <h5>{{ id_msg.author }}</h5>
      <h5>{{ id_msg.genre }}</h5>
      <h5>{{ id_msg.release_year }}</h5>
    </div>
  <div class="titleSearch">
    <p>SEARCH BY TITLE KEYWORD</p>
    <input type="text" v-model="keyword">
    <br>
    <button class="detail" @click="searchByTitle()">
      SEARCH
    </button>
      <h5>{{ title_msg }}</h5>
  </div>
  </body>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      id_msg: '',
      title_msg: '',
      id: '',
      keyword: '',
    };
  },
  methods: {
    searchById() {
      axios.get('http://localhost:8000/book/' + this.id)
        .then((res) => {
          this.id_msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        })
    },
    searchByTitle() {
      axios.get('http://localhost:8000/book/title/' + this.keyword)
        .then((res) => {
          this.title_msg = res.data;
          console.log(this.title_msg[1].title)
        })
        .catch((error) => {
          console.error(error);
      })
    },
  },
};
</script>

<style scoped>
@import '@/assets/styles/search-style.scss';
</style>
