import { createRouter, createWebHistory } from 'vue-router'
import TodoList from '../views/TodoList.vue'
import TodoDetail from '../views/TodoDetail.vue'

const routes = [
  {
    path: '/',
    name: 'TodoList',
    component: TodoList
  },
  {
    path: '/todo/:id',
    name: 'TodoDetail',
    component: TodoDetail,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router
