<template>
  <div id="app">
    <router-view/>
    <side-bar/>
  </div>
</template>

<script>
import SideBar from '/src/components/SideBar.vue'

export default {
  components: {
    SideBar,
  }
}
</script>

<style scoped>
</style>
