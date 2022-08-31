<template>
  <div>
    <button @click="getAllBooks()"> 
      GET ALL BOOKS
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
    };
  },
  methods: {
    getAllBooks() {
      axios.get('http://localhost:8000/books')
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
