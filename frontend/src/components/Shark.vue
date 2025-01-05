<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const msg = ref("");

const getResponse = async () => {
  try {
    const path = "http://localhost:8000/shark";
    const res = await axios.get(path);
    console.log(res.data);
    msg.value = res.data;
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  getResponse();
});
</script>

<template>
  <div>
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>
