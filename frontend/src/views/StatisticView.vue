<script setup>
import { computed, onMounted } from "vue";
import { useStore } from "vuex";
import { FwbCard, FwbButton } from "flowbite-vue";
import { useRouter } from "vue-router";

const store = useStore();

const stat = computed(() => store.state.games.stat);

const router = useRouter();

onMounted(() => {
  store.dispatch("getStat");
});
</script>

<template>
  <div class="mx-auto flex w-full max-w-screen-xl flex-col gap-4 p-4 lg:px-12">
    <section class="flex-1 dark:bg-gray-900">
      <div
        class="relative overflow-hidden bg-white shadow-md dark:bg-gray-800 sm:rounded-lg"
      >
        <div
          class="flex-row items-center justify-between space-y-3 p-4 sm:flex sm:space-x-4 sm:space-y-0"
        >
          <div>
            <h5 class="mr-3 font-semibold dark:text-white">Statistic</h5>
            <p class="text-gray-500 dark:text-gray-400">
              Check your game library statistic
            </p>
          </div>
          <div class="flex justify-end gap-3">
            <fwb-button
              gradient="teal-lime"
              outline
              @click="router.push('/games')"
            >
              Game Library
            </fwb-button>
          </div>
        </div>
      </div>
    </section>
    <div class="flex justify-center gap-4">
      <div class="flex-1">
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
      </div>

      <div class="flex-1">
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
      </div>

      <div class="flex-1">
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
    </div>
  </div>
</template>
