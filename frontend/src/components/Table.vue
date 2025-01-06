<script setup>
import { computed, ref, reactive } from "vue";
import { useStore } from "vuex";
import { options } from "@/constant/options";
import {
  FwbTable,
  FwbTableBody,
  FwbTableCell,
  FwbTableHead,
  FwbTableHeadCell,
  FwbTableRow,
  FwbButton,
  FwbModal,
  FwbInput,
  FwbCheckbox,
  FwbSelect,
} from "flowbite-vue";
import { useToast } from "vue-toastification";

const toast = useToast();

const store = useStore();
const games = computed(() => store.getters.allGames);
const updateGame = (editGameForm) => {
  store.dispatch("updateGame", editGameForm);
  toast.success("Game updated");
};
const deleteGame = (game) => {
  store.dispatch("deleteGame", game.id);
  toast.success("Game deleted");
};

const isShowModal = ref(false);
const editGameForm = reactive({
  id: "",
  title: "",
  genre: "",
  played: false,
});

const showEditModal = (game) => {
  isShowModal.value = true;
  editGameForm.id = game.id;
  editGameForm.title = game.title;
  editGameForm.genre = game.genre;
  editGameForm.played = game.played;
};

const handleOk = () => {
  updateGame(editGameForm);
  isShowModal.value = false;
};

const closeModal = () => {
  isShowModal.value = false;
};
</script>

<template>
  <fwb-table hoverable>
    <fwb-table-head>
      <fwb-table-head-cell>Title</fwb-table-head-cell>
      <fwb-table-head-cell>Genre</fwb-table-head-cell>
      <fwb-table-head-cell>Played</fwb-table-head-cell>
      <fwb-table-head-cell>
        <span class="sr-only">Edit</span>
      </fwb-table-head-cell>
    </fwb-table-head>
    <fwb-table-body>
      <fwb-table-row v-for="(game, index) in games" :key="index">
        <fwb-table-cell>{{ game.title }}</fwb-table-cell>
        <fwb-table-cell>{{ game.genre }}</fwb-table-cell>
        <fwb-table-cell
          ><span v-if="game.played">Yes</span>
          <span v-else>No</span></fwb-table-cell
        >
        <fwb-table-cell>
          <div class="flex justify-end gap-2">
            <fwb-button size="xs" pill @click="showEditModal(game)"
              >Edit</fwb-button
            >
            <fwb-button size="xs" color="red" pill @click="deleteGame(game)"
              >Delete</fwb-button
            >
          </div>
        </fwb-table-cell>
      </fwb-table-row>
    </fwb-table-body>
  </fwb-table>

  <fwb-modal v-if="isShowModal" @close="closeModal">
    <template #header>
      <div class="flex items-center text-lg">Update Game</div>
    </template>
    <template #body>
      <div class="flex flex-col gap-4">
        <fwb-input
          v-model="editGameForm.title"
          placeholder="Enter Title"
          label="Title"
        />
        <fwb-select
          v-model="editGameForm.genre"
          :options="options"
          label="Genre"
        />
        <fwb-checkbox v-model="editGameForm.played" label="Played?" />
      </div>
    </template>
    <template #footer>
      <div class="flex justify-end gap-2">
        <fwb-button @click="closeModal" color="alternative">
          Cancel
        </fwb-button>
        <fwb-button @click="handleOk"> Update </fwb-button>
      </div>
    </template>
  </fwb-modal>
</template>
