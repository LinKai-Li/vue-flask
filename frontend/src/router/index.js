import { createRouter, createWebHistory } from "vue-router";
import Statistic from "@/views/StatisticView.vue";
import Games from "@/views/GamesView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/statistic",
      name: "Statistic",
      component: Statistic,
    },
    {
      path: "/games",
      name: "Games",
      component: Games,
    },
  ],
});

export default router;
