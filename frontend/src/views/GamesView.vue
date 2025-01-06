<script setup>
import { ref, onMounted } from "vue";
import { FwbButton, FwbFooter, FwbFooterCopyright } from "flowbite-vue";
import { useRouter } from "vue-router";

import Table from "@/components/Table.vue";
import NewModal from "@/components/NewModal.vue";
import { useStore } from "vuex";

const store = useStore();

const router = useRouter();

const openAdd = ref(false);

const showAddModal = () => {
  openAdd.value = true;
};

onMounted(() => {
  store.dispatch("getGames");
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
            <h5 class="mr-3 font-semibold dark:text-white">Game Library</h5>
            <p class="text-gray-500 dark:text-gray-400">
              Manage all your played games or add a new one
            </p>
          </div>
          <div class="flex justify-end gap-3">
            <fwb-button @click="showAddModal">Add Game</fwb-button>
            <fwb-button
              gradient="teal-lime"
              outline
              @click="router.push('/statistic')"
            >
              Statistic
            </fwb-button>
          </div>
        </div>
      </div>
    </section>

    <Table />
    <fwb-footer>
      <fwb-footer-copyright
        by="Link™"
        copyright-message="All Rights Reserved."
      />
    </fwb-footer>
    <!-- First Modal -->
    <NewModal v-model="openAdd" />
  </div>
</template>
