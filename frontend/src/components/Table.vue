<script setup>
import { computed, ref, reactive } from "vue";
import { useStore } from "vuex";
import {
  FwbA,
  FwbTable,
  FwbTableBody,
  FwbTableCell,
  FwbTableHead,
  FwbTableHeadCell,
  FwbTableRow,
  FwbButton,
} from "flowbite-vue";

const store = useStore();
const games = computed(() => store.getters.allGames);
const updateGame = (editGameForm) => {
  store.dispatch("updateGame", editGameForm);
};
const deleteGame = (game) => {
  store.dispatch("deleteGame", game.id);
};

const open = ref(false);
const editGameForm = reactive({
  id: "",
  title: "",
  genre: "",
  played: false,
});

const showEditModal = (game) => {
  open.value = true;
  editGameForm.id = game.id;
  editGameForm.title = game.title;
  editGameForm.genre = game.genre;
  editGameForm.played = game.played;
};

const handleOk = (e) => {
  e.preventDefault();
  updateGame(editGameForm);
  open.value = false;
};

const handleReset = (e) => {
  e.preventDefault();
  open.value = false;
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

  <a-modal
    v-model:open="open"
    title="Update Game"
    okText="Update"
    cancelText="Cancel"
    @cancel="handleReset"
    @ok="handleOk"
  >
    <a-form layout="vertical" :model="editGameForm" autocomplete="off">
      <a-form-item
        label="Title"
        name="title"
        :rules="[{ required: true, message: 'Please input your title!' }]"
      >
        <a-input v-model:value="editGameForm.title" placeholder="Enter Title" />
      </a-form-item>

      <a-form-item
        label="Genre"
        name="genre"
        :rules="[{ required: true, message: 'Please input your genre!' }]"
      >
        <a-input v-model:value="editGameForm.genre" placeholder="Enter Genre" />
      </a-form-item>

      <a-form-item name="remember">
        <a-checkbox v-model:checked="editGameForm.played">Played?</a-checkbox>
      </a-form-item>
    </a-form>
  </a-modal>
</template>
