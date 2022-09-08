<template>
<body>
  <div class="collectionDiv">
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>TITLE</th>
          <th>AUTHOR</th>
          <th>GENRE</th>
          <th>RELEASE YEAR</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row">
          <td v-for="col in columns" :key="col">{{ row[col] }}</td>
        </tr>
      </tbody>
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
        "id",
        "title",
        "author",
        "genre",
        "release_year",
      ], 
    };
  },
  mounted() {
      axios.get('http://localhost:8000/book')
        .then(res => {
          this.rows = res.data;       
        })
        .catch((error) => {
          console.error(error);
        })
    },
};
</script>

<style>
@import '@/assets/styles/collection_style.scss';
</style>
