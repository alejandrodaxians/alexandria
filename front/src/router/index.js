import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GetAllBooks from '../components/GetAllBooks.vue'
import DeleteBook from '../components/DeleteBook.vue'
import CreateBook from '../components/CreateBook.vue'
import GetBook from '../components/GetBook.vue'
import UpdateBook from '../components/UpdateBook.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/collection',
    name: 'library',
    component: GetAllBooks
  },
  {
    path: '/new_book',
    name: 'create',
    component: CreateBook
  },
  {
    path: '/delete_book',
    name: 'delete',
    component: DeleteBook
  },
  {
    path: '/search_book',
    name: 'search',
    component: GetBook
  },
  {
    path: '/update_book',
    name: 'update',
    component: UpdateBook
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
