<script setup>
import { ref, defineProps, defineEmits, reactive } from "vue";
import { useStore } from "vuex";
defineProps({
  modelValue: Boolean,
});

const emit = defineEmits(["update:modelValue"]);

const store = useStore();
const addGame = (addGameForm) => {
  store.dispatch("addGame", addGameForm);
};

const addGameForm = reactive({
  title: "",
  genre: "",
  played: false,
});

const initForm = () => {
  addGameForm.title = "";
  addGameForm.genre = "";
  addGameForm.played = false;
};

const handleOk = (e) => {
  e.preventDefault();
  emit("update:modelValue", false);
  addGame(addGameForm);
  initForm();
};

const handleReset = (e) => {
  e.preventDefault();
  emit("update:modelValue", false);
  initForm();
};
</script>

<template>
  <a-modal
    :open="modelValue"
    title="Add a new game"
    okText="Submit"
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
        <a-input v-model:value="addGameForm.title" placeholder="Enter Title" />
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
</template>
