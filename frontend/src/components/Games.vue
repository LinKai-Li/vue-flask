<script setup>
import { ref, onMounted, reactive, computed } from "vue";
import Table from "./Table.vue";
import NewModal from "./NewModal.vue";
import { useStore } from "vuex";

const store = useStore();

const message = computed(() => store.state.games.message);
const showMessage = computed(() => store.state.games.showMessage);

const openAdd = ref(false);

const showAddModal = () => {
  openAdd.value = true;
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
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="bg-primary text-center text-white"
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
          <Table />
          <footer
            class="bg-primary text-center text-white"
            style="border-radius: 10px"
          >
            Copyright &copy;. All Rights Reserved 2025
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <NewModal v-model="openAdd" />
    </div>
  </div>
</template>
