<script setup>
import { computed, ref, reactive } from "vue";
import { useStore } from "vuex";

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
  <table class="table table-hover">
    <!-- Table Head -->
    <thead>
      <tr>
        <!-- Table header cells -->
        <th scope="col">Title</th>
        <th scope="col">Genre</th>
        <th scope="col">Played?</th>
        <th scope="col">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(game, index) in games" :key="index">
        <td>{{ game.title }}</td>
        <td>{{ game.genre }}</td>
        <td>
          <span v-if="game.played">Yes</span>
          <span v-else>No</span>
        </td>
        <td>
          <div class="btn-group" role="group">
            <button
              type="button"
              class="btn btn-info btn-sm"
              @click="showEditModal(game)"
            >
              Update
            </button>
            <button
              type="button"
              class="btn btn-danger btn-sm"
              @click="deleteGame(game)"
            >
              Delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>

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
