<template>
    <body>
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
        <br><br>
        <div class="homeButton"><a href="/"><home-icon class="homeIcon"/></a></div>
        </div>
        <div class="button">
        <button @click="show = !show" class="toggle"><menu-icon /></button>
        </div>
        </body>
</template>

<script>
import MenuIcon from 'vue-material-design-icons/Menu.vue';
import HomeIcon from 'vue-material-design-icons/Home.vue';

export default {
    name: 'SideBar',
    components: {
        MenuIcon,
        HomeIcon
    },
    data() {
        return {
            show: false,
        }
    }
}
</script>

<style>
@import '@/assets/styles/sidebar.scss';
</style>