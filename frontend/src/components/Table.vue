<script setup>
defineProps({
  games: Array,
})

const emit = defineEmits(['showEditModal'])
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
            <button type="button" class="btn btn-info btn-sm" @click="emit('showEditModal', game)">
              Update
            </button>
            <button type="button" class="btn btn-danger btn-sm">Delete</button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>
