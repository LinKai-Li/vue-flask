import { createRouter, createWebHistory } from 'vue-router'
import Shark from '@/components/Shark.vue'
import Games from '@/components/Games.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/shark',
      name: 'Shark',
      component: Shark,
    },
    {
      path: '/games',
      name: 'Games',
      component: Games,
    },
  ],
})

export default router
