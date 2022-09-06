<template>
<body>
  <div class="getButtonDiv">
    <button @click="getAllBooks()" class="getButton"> 
      DISPLAY <br> COLLECTION
    </button>
  </div>
  <div class="collectionDiv">
    <table>
      <th v-for="(col) in columns" :key="col">{{ col }}</th>
      <tr v-for="row in rows" :key="row">
        <td></td>
      </tr>
    </table>
  </div>
</body>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      rows: [],
      columns: [
        "ID",
        "TITLE",
        "AUTHOR",
        "GENRE",
        "RELEASE YEAR",
      ],
       
    };
  },
  methods: {
    getAllBooks() {
      axios.get('http://localhost:8000/books')
        .then(res => {
          var resLength = (res.data).length
          for (let i = 0; i < resLength; i++) {
            console.log(i)
          }          
        })
        .catch((error) => {
          console.error(error);
        })
    },
  },
};
</script>

<style>
@import '@/assets/styles/collection_style.scss';
</style>
