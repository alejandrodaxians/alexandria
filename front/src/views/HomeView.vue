<template>
  <body>
    <div class="title">
      <h1>ALEXANDRIA</h1>
      <h1>VIRTUAL LIBRARY</h1>
    </div>
    <div v-if="show" class="sidebar">
      <h3 class="sidebar-item">MENU</h3>
      <br>
      <a href="/collection">Collection</a>
      <br><br>
      <a href="/search_book">Search books</a>
      <br><br>
      <a href="/new_book">Create a book</a>
      <br><br>
      <a href="/delete_book">Delete a book</a>
      <br><br>
      <a href="/update_book">Update a book</a>
    </div>
    <div class="button">
      <button @click="show = !show" class="toggle"><menu-icon /></button>
    </div>
  </body>
</template>

<script>
import MenuIcon from 'vue-material-design-icons/Menu.vue';

export default {
  name: 'HomeView',
  components: {
    MenuIcon,
  },
  data() {
    return {
      show: false,
    }
  },
  methods: {
  }
}
</script>

<style>
@import '@/assets/styles/home_style.scss';
@import '@/assets/styles/sidebar.scss';
</style>
