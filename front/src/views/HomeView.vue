<template>
  <body>
    <div class="title">
      <h1>ALEXANDRIA</h1>
      <h1>VIRTUAL LIBRARY</h1>
    </div>
    <div :style="show ? filterStyle : null" class="sidebar">
      <h3 class="sidebar-item">MENU</h3>
      <br>
      <a href="/collection">Collection</a>
      <br><br>
      <a href="/new_book">Create a book</a>
      <br><br>
      <a href="/delete_book">Delete a book</a>
      <br><br>
      <a href="/search_books">Search books</a>
      <br><br>
      <a href="/update_book">Update a book</a>
    </div>
    <div class="button">
      <button v-on:click="openSidebar()">Sidebar</button>
    </div>
  </body>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      show:false,
        filterStyle: {
            display: "block",           
        },
    }
  },
  methods: {
    openSidebar() {
      this.show = !this.show
    }
  }
}
</script>

<style>
@import '@/assets/styles/home_style.scss';
@import '@/assets/styles/sidebar.scss';
</style>
