<template>
  <body>
    <div class="deleteTitle">
      <p>DELETE A BOOK</p>
    </div>
    <div class="info">
      <p>Input the ID for the book you want to delete from the database:</p>    </div>
    <div class="deleteInput">
      <input type="text" v-model="id" required>
      <br>
      <button @click="deleteBook()">
        DELETE
      </button>
    </div>
    <div class="deleteResult" v-if="show">
      <p class="resultId">{{ msg.message }}</p>
    </div>
  </body>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      msg: '',
      id: 0,
      show: false,
    };
  },
  methods: {
    deleteBook() {
      axios.delete('http://localhost:8000/book/' + this.id)
        .then((res) => {
          this.show = true;
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
@import '@/assets/styles/delete_style.scss';
</style>
