<script setup>
import { ref, onMounted, reactive, computed } from "vue";
import Table from "./Table.vue";
import NewModal from "./NewModal.vue";
import EditModal from "./EditModal.vue";
import { useStore } from "vuex";

const store = useStore();

const message = computed(() => store.state.games.message);
const showMessage = computed(() => store.state.games.showMessage);

const addGame = (addGameForm) => {
  store.dispatch("addGame", addGameForm);
};

const updateGame = (editGameForm) => {
  store.dispatch("updateGame", editGameForm);
};

const deleteGame = (game) => {
  store.dispatch("deleteGame", game.id);
};

const openAdd = ref(false);
const openUpdate = ref(false);

const formData = reactive({
  id: "",
  title: "",
  genre: "",
  played: false,
});

const showAddModal = () => {
  openAdd.value = true;
};

const showEditModal = (game) => {
  openUpdate.value = true;
  formData.id = game.id;
  formData.title = game.title;
  formData.genre = game.genre;
  formData.played = game.played;
};

const hideAlert = () => {
  store.dispatch("hideAlert");
};

onMounted(() => {
  store.dispatch("getGames");
});
</script>

<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- bootswatch CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library🕹️
          </h1>
          <hr />
          <br />

          <!-- Alert Message -->
          <a-alert
            v-if="showMessage"
            :message="message"
            type="warning"
            closable
            @close="hideAlert"
          />

          <button
            type="button"
            class="btn btn-success btn-sm"
            @click="showAddModal"
          >
            Add Game
          </button>
          <br /><br />
          <Table @show-edit-modal="showEditModal" @delete-game="deleteGame" />
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy;. All Rights Reserved 2021
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <NewModal v-model="openAdd" @add-game="addGame" />

      <!-- Second Modal -->
      <EditModal
        v-model="openUpdate"
        :form-data="formData"
        @update-game="updateGame"
      />
    </div>
  </div>
</template>
