<script setup>
import { computed, onMounted } from "vue";
import { useStore } from "vuex";
import { FwbCard } from "flowbite-vue";

const store = useStore();

const stat = computed(() => store.state.games.stat);

onMounted(() => {
  store.dispatch("getStat");
});
</script>

<template>
  <div class="flex justify-center gap-4 p-4">
    <fwb-card>
      <div class="p-5">
        <h5 class="mb-2 text-2xl font-bold text-gray-900 dark:text-white">
          Total Games Played
        </h5>
        <p class="text-2xl text-gray-700 dark:text-gray-400">
          {{ stat.total_games }}
        </p>
      </div>
    </fwb-card>

    <fwb-card>
      <div class="p-5">
        <h5 class="mb-2 text-2xl font-bold text-gray-900 dark:text-white">
          Total Played Games
        </h5>
        <p class="text-2xl text-gray-700 dark:text-gray-400">
          {{ stat.played_true_count }}
        </p>
      </div>
    </fwb-card>

    <fwb-card>
      <div class="p-5">
        <h5 class="mb-2 text-2xl font-bold text-gray-900 dark:text-white">
          Total Unplayed Games
        </h5>
        <p class="text-2xl text-gray-700 dark:text-gray-400">
          {{ stat.played_false_count }}
        </p>
      </div>
    </fwb-card>
  </div>
</template>
