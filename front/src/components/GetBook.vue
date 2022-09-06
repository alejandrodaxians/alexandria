<template>
  <body>

    <div class="searchID">
      <input type="text" v-model="id">
      <button class="detail" @click="searchById()">
        SEARCH by ID
      </button>
      <p>{{ id_msg }}</p>
    </div>

    <div class="searchTitle">
      <input type="text" v-model="keyword">
      <button class="detail" @click="searchByTitle()">
        SEARCH by TITLE
      </button>
      <p>{{ title_msg }}</p>
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
