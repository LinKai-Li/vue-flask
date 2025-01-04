<script setup>
import axios from 'axios'
import { ref, onMounted, reactive } from 'vue'
import Table from './Table.vue'
import NewModal from './NewModal.vue'
import EditModal from './EditModal.vue'

const games = ref([])
const openAdd = ref(false)
const openUpdate = ref(false)
const message = ref('')
const showMessage = ref(false)

const formData = reactive({
  id: '',
  title: '',
  genre: '',
  played: false,
})

const showAddModal = () => {
  openAdd.value = true
}

const showEditModal = (game) => {
  openUpdate.value = true
  formData.id = game.id
  formData.title = game.title
  formData.genre = game.genre
  formData.played = game.played
}

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

// PUT function
const updateGame = async (editGameForm) => {
  try {
    const path = `http://localhost:8000/games/${editGameForm.id}`
    const res = await axios.put(path, editGameForm)
    console.log(res.data)
    showAlert('Game Updated!')
  } catch (error) {
    console.error(error)
  } finally {
    await getGames()
  }
}

// DELETE function
const deleteGame = async (game) => {
  try {
    const path = `http://localhost:8000/games/${game.id}`
    const res = await axios.delete(path)
    console.log(res.data)
    showAlert('Game Deleted!')
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
          <Table :games="games" @show-edit-modal="showEditModal" @delete-game="deleteGame" />
          <footer class="bg-primary text-white text-center" style="border-radius: 10px">
            Copyright &copy;. All Rights Reserved 2021
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <NewModal v-model="openAdd" @add-game="addGame" />

      <!-- Second Modal -->
      <EditModal v-model="openUpdate" :form-data="formData" @update-game="updateGame" />
    </div>
  </div>
</template>
