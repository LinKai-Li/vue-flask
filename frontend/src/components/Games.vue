<script setup>
import axios from 'axios'
import { ref, reactive, onMounted } from 'vue'
import Table from './Table.vue'
import NewModal from './NewModal.vue'

const games = ref([])
const openAdd = ref(false)
const message = ref('')
const showMessage = ref(false)

const showAddModal = () => {
  openAdd.value = true
}

const editForm = reactive({
  id: '',
  title: '',
  genre: '',
  played: false,
})

// GET function
const getGames = async () => {
  try {
    const path = 'http://localhost:8000/games'
    const res = await axios.get(path)
    games.value = res.data.games
  } catch (error) {
    console.error(error)
  }
}

// POST function
const addGame = async (addGameForm) => {
  try {
    const path = 'http://localhost:8000/games'
    const res = await axios.post(path, addGameForm)
    console.log(res.data)
    showAlert('Game Added!')
  } catch (error) {
    console.error(error)
  } finally {
    await getGames()
  }
}

const showAlert = (msg) => {
  message.value = msg
  showMessage.value = true
}

const hideAlert = () => {
  showMessage.value = false
}

onMounted(() => {
  getGames()
})
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
          <h1 class="text-center bg-primary text-white" style="border-radius: 10px">
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

          <button type="button" class="btn btn-success btn-sm" @click="showAddModal">
            Add Game
          </button>
          <br /><br />
          <Table :games="games" />
          <footer class="bg-primary text-white text-center" style="border-radius: 10px">
            Copyright &copy;. All Rights Reserved 2021
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <NewModal v-model="openAdd" @add-game="addGame" />

      <!-- Second Modal -->
      <!-- <a-modal
        v-model:open="open"
        title="Edit game"
        okText="Update"
        @cancel="handleResetUpdate"
        @ok="handleOkUpdate"
      >
        <a-form layout="vertical" :model="editForm" autocomplete="off">
          <a-form-item
            label="Title"
            name="title"
            :rules="[{ required: true, message: 'Please input your title!' }]"
          >
            <a-input v-model:value="editForm.title" placeholder="Enter Game" />
          </a-form-item>

          <a-form-item
            label="Genre"
            name="genre"
            :rules="[{ required: true, message: 'Please input your genre!' }]"
          >
            <a-input v-model:value="editForm.genre" placeholder="Enter Genre" />
          </a-form-item>

          <a-form-item name="remember">
            <a-checkbox v-model:checked="editForm.played">Played?</a-checkbox>
          </a-form-item>
        </a-form>
      </a-modal> -->
    </div>
  </div>
</template>
