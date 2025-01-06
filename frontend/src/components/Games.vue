<script setup>
import { ref, onMounted } from "vue";
import { FwbButton } from "flowbite-vue";

import Table from "./Table.vue";
import NewModal from "./NewModal.vue";
import { useStore } from "vuex";

const store = useStore();

const openAdd = ref(false);

const showAddModal = () => {
  openAdd.value = true;
};

onMounted(() => {
  store.dispatch("getGames");
});
</script>

<template>
  <div class="mx-auto w-full max-w-screen-xl p-4 lg:px-12">
    <section class="flex-1 pb-4 dark:bg-gray-900">
      <div
        class="relative overflow-hidden bg-white shadow-md dark:bg-gray-800 sm:rounded-lg"
      >
        <div
          class="flex-row items-center justify-between space-y-3 p-4 sm:flex sm:space-x-4 sm:space-y-0"
        >
          <div>
            <h5 class="mr-3 font-semibold dark:text-white">Game Library</h5>
            <p class="text-gray-500 dark:text-gray-400">
              Manage all your played games or add a new one
            </p>
          </div>
          <fwb-button @click="showAddModal">Add Game</fwb-button>
        </div>
      </div>
    </section>

    <Table />
    <footer
      class="bg-primary text-center text-white"
      style="border-radius: 10px"
    >
      Copyright &copy;. All Rights Reserved 2025
    </footer>
    <!-- First Modal -->
    <NewModal v-model="openAdd" />
  </div>
</template>
