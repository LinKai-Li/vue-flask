<script setup>
import axios from 'axios'
import { ref, reactive, onMounted } from 'vue'

const games = ref([])
const open = ref(false)

const showModal = () => {
  open.value = true
}

const handleOk = (e) => {
  e.preventDefault()
  open.value = false
  addGame()
  initForm()
}

const handleReset = (e) => {
  e.preventDefault()
  open.value = false
  initForm()
}

const addGameForm = reactive({
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
const addGame = async () => {
  try {
    const path = 'http://localhost:8000/games'
    const res = await axios.post(path, addGameForm)
    console.log(res.data)
  } catch (error) {
    console.error(error)
  } finally {
    await getGames()
  }
}

const initForm = () => {
  addGameForm.title = ''
  addGameForm.genre = ''
  addGameForm.played = false
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
          <button type="button" class="btn btn-success btn-sm" @click="showModal">Add Game</button>
          <br /><br />
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
                    <button type="button" class="btn btn-info btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer class="bg-primary text-white text-center" style="border-radius: 10px">
            Copyright &copy;. All Rights Reserved 2021
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <a-modal
        v-model:open="open"
        title="Add a new game"
        okText="Update"
        cancelText="Reset"
        @cancel="handleReset"
        @ok="handleOk"
      >
        <a-form layout="vertical" :model="addGameForm" autocomplete="off">
          <a-form-item
            label="Title"
            name="title"
            :rules="[{ required: true, message: 'Please input your title!' }]"
          >
            <a-input v-model:value="addGameForm.title" placeholder="Enter Game" />
          </a-form-item>

          <a-form-item
            label="Genre"
            name="genre"
            :rules="[{ required: true, message: 'Please input your genre!' }]"
          >
            <a-input v-model:value="addGameForm.genre" placeholder="Enter Genre" />
          </a-form-item>

          <a-form-item name="remember">
            <a-checkbox v-model:checked="addGameForm.played">Played?</a-checkbox>
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
  </div>
</template>
