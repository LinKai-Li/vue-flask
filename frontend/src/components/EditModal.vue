<script setup>
import { defineProps, defineEmits, watch, reactive } from "vue";
const props = defineProps({
  modelValue: Boolean,
  formData: Object,
});

const emit = defineEmits(["update:modelValue", "updateGame"]);

const editGameForm = reactive({ ...props.formData });

watch(
  () => props.formData,
  (newFormData) => {
    Object.assign(editGameForm, newFormData);
  },
  { deep: true, immediate: true },
);

const handleOk = (e) => {
  e.preventDefault();
  emit("update:modelValue", false);
  emit("updateGame", editGameForm);
};

const handleReset = (e) => {
  e.preventDefault();
  emit("update:modelValue", false);
};
</script>

<template>
  <a-modal
    :open="modelValue"
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
